from __future__ import absolute_import, division, print_function

import logging
import os
import json
import random
import glob
import torch
import tqdm
import torch.utils.data

import numpy as np
from unilm.old_school_transformers import (
    BertTokenizer,
    RobertaTokenizer,
    XLMRobertaTokenizer,
)
import s2s_ft.s2s_loader as seq2seq_loader
from s2s_ft.modeling_decoding import BertForSeq2SeqDecoder, BertConfig
TOKENIZER_CLASSES = {
    'bert': BertTokenizer,
    'roberta': RobertaTokenizer,
    'xlm-roberta': XLMRobertaTokenizer,
}

logger = logging.getLogger(__name__)


class Seq2seqDatasetForBert(torch.utils.data.Dataset):
    def __init__(
            self, features, max_source_len, max_target_len,
            vocab_size, cls_id, sep_id, pad_id, mask_id,
            random_prob, keep_prob, offset, num_training_instances, 
            span_len=1, span_prob=1.0):
        self.features = features
        self.max_source_len = max_source_len
        self.max_target_len = max_target_len
        self.offset = offset
        if offset > 0:
            logger.info("  ****  Set offset %d in Seq2seqDatasetForBert ****  ", offset)
        self.cls_id = cls_id
        self.sep_id = sep_id
        self.pad_id = pad_id
        self.random_prob = random_prob
        self.keep_prob = keep_prob
        self.mask_id = mask_id
        self.vocab_size = vocab_size
        self.num_training_instances = num_training_instances
        self.span_len = span_len
        self.span_prob = span_prob

    def __len__(self):
        return int(self.num_training_instances)

    def __trunk(self, ids, max_len):
        if len(ids) > max_len - 1:
            ids = ids[:max_len - 1]
        ids = ids + [self.sep_id]
        return ids

    def __pad(self, ids, max_len):
        if len(ids) < max_len:
            return ids + [self.pad_id] * (max_len - len(ids))
        else:
            assert len(ids) == max_len
            return ids

    def __getitem__(self, idx):
        idx = (self.offset + idx) % len(self.features)
        feature = self.features[idx]
        source_ids = self.__trunk([self.cls_id] + feature["source_ids"], self.max_source_len)
        target_ids = self.__trunk(feature["target_ids"], self.max_target_len)
        pseudo_ids = []
        for tk_id in target_ids:
            p = random.random()
            if p < self.keep_prob:
                pseudo_ids.append(tk_id)
            elif p < self.keep_prob + self.random_prob:
                pseudo_ids.append(random.randint(0, self.vocab_size - 1))
            else:
                pseudo_ids.append(self.mask_id)

        num_source_tokens = len(source_ids)
        num_target_tokens = len(target_ids)

        source_ids = self.__pad(source_ids, self.max_source_len)
        target_ids = self.__pad(target_ids, self.max_target_len)
        pseudo_ids = self.__pad(pseudo_ids, self.max_target_len)

        if self.span_len > 1:
            span_ids = []
            span_id = 1
            while len(span_ids) < num_target_tokens:
                p = random.random()
                if p < self.span_prob:
                    span_len = random.randint(2, self.span_len)
                    span_len = min(span_len, num_target_tokens - len(span_ids))
                else:
                    span_len = 1
                span_ids.extend([span_id] * span_len)
                span_id += 1
            span_ids = self.__pad(span_ids, self.max_target_len)
            return source_ids, target_ids, pseudo_ids, num_source_tokens, num_target_tokens, span_ids
        else:
            return source_ids, target_ids, pseudo_ids, num_source_tokens, num_target_tokens


def batch_list_to_batch_tensors(batch):
    batch_tensors = []
    for x in zip(*batch):
        if isinstance(x[0], torch.Tensor):
            batch_tensors.append(torch.stack(x))
        else:
            batch_tensors.append(torch.tensor(x, dtype=torch.long))
    return batch_tensors


def get_max_epoch_model(output_dir):
    fn_model_list = glob.glob(os.path.join(output_dir, "model.*.bin"))
    fn_optim_list = glob.glob(os.path.join(output_dir, "optim.*.bin"))
    if (not fn_model_list) or (not fn_optim_list):
        return None
    os.path.basename(output_dir)
    both_set = set([int(os.path.basename(fn).split('.')[1]) for fn in fn_model_list]
                   ) & set([int(os.path.basename(fn).split('.')[1]) for fn in fn_optim_list])
    if both_set:
        return max(both_set)
    else:
        return None


def load_and_cache_examples(
        example_file, tokenizer, local_rank, cached_features_file, shuffle=True):
    # Make sure only the first process in distributed training process the dataset, and the others will use the cache
    if local_rank not in [-1, 0]:
        torch.distributed.barrier()

    if cached_features_file is not None and os.path.exists(cached_features_file):
        logger.info("Loading features from cached file %s", cached_features_file)
        features = torch.load(cached_features_file)
    else:
        logger.info("Creating features from dataset file at %s", example_file)

        examples = []
        with open(example_file, mode="r", encoding="utf-8") as reader:
            for line in reader:
                examples.append(json.loads(line))
        features = []

        for example in tqdm.tqdm(examples):
            if isinstance(example["src"], list):
                source_tokens = example["src"]
                target_tokens = example["tgt"]
            else:
                source_tokens = tokenizer.tokenize(example["src"])
                target_tokens = tokenizer.tokenize(example["tgt"])
            features.append({
                    "source_ids": tokenizer.convert_tokens_to_ids(source_tokens),
                    "target_ids": tokenizer.convert_tokens_to_ids(target_tokens),
                })

        if shuffle:
            random.shuffle(features)

        if local_rank in [-1, 0] and cached_features_file is not None:
            logger.info("Saving features into cached file %s", cached_features_file)
            torch.save(features, cached_features_file)

    # Make sure only the first process in distributed training process the dataset, and the others will use the cache
    if local_rank == 0:
        torch.distributed.barrier()

    return features


def build_components(
    seed=123,
    model_type="xlm-roberta",
    tokenizer_name="xlm-roberta-base",
    config_path=None,
    model_path=None,
    beam_size=1,
    do_lower_case=False,
    cache_dir=None,
    max_seq_length=512,
    max_tgt_length=48,
    pos_shift=False,
    forbid_ignore_word=".",
    forbid_duplicate_ngrams=True,
    length_penalty=0.0,
    ngram_size=3,
    min_len=0,
    mode="s2s",
    fp16=False,
    use_cuda_if_available=True,
):
    device = torch.device(
        "cuda"
        if torch.cuda.is_available() and use_cuda_if_available is True else "cpu"
    )
    n_gpu = torch.cuda.device_count()
    if n_gpu > 1:
        n_gpu = 1
        print("WARNING: n_gpu > 1. Has been set to 1")

    if seed > 0:
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        if n_gpu > 0:
            torch.cuda.manual_seed_all(seed)
    else:
        random_seed = random.randint(0, 10000)
        logger.info("Set random seed as: {}".format(random_seed))
        random.seed(random_seed)
        np.random.seed(random_seed)
        torch.manual_seed(random_seed)
        if n_gpu > 0:
            torch.cuda.manual_seed_all(seed)

    # -> Tokenizer
    tokenizer = TOKENIZER_CLASSES[model_type].from_pretrained(
        tokenizer_name,
        do_lower_case=do_lower_case,
        cache_dir=cache_dir if cache_dir else None,
        model_max_length=max_seq_length
    )

    # -> Config
    config_file = config_path if config_path else os.path.join(model_path, "config.json")
    logger.info("Read decoding config from: %s" % config_file)
    config = BertConfig.from_json_file(config_file)

    # -> Preprocessing pipeline
    if model_type == "roberta":
        vocab = tokenizer.encoder
    elif model_type == "xlm-roberta":
        vocab = tokenizer.get_vocab()
    else:
        vocab = tokenizer.vocab
    bi_uni_pipeline = [
        seq2seq_loader.Preprocess4Seq2seqDecoder(
            list(vocab.keys()),
            tokenizer.convert_tokens_to_ids,
            max_seq_length,
            max_tgt_length=max_tgt_length,
            pos_shift=pos_shift,
            source_type_id=config.source_type_id, target_type_id=config.target_type_id,
            cls_token=tokenizer.cls_token, sep_token=tokenizer.sep_token, pad_token=tokenizer.pad_token
        )
    ]

    mask_word_id, eos_word_ids, sos_word_id = tokenizer.convert_tokens_to_ids(
        [tokenizer.mask_token, tokenizer.sep_token, tokenizer.sep_token]
    )
    forbid_ignore_set = None
    if forbid_ignore_word:
        w_list = []
        for w in forbid_ignore_word.split('|'):
            if w.startswith('[') and w.endswith(']'):
                w_list.append(w.upper())
            else:
                w_list.append(w)
        forbid_ignore_set = set(tokenizer.convert_tokens_to_ids(w_list))

    # -> Model
    print(model_path)
    model_recover_path = model_path.strip()
    logger.info("***** Recover model: %s *****", model_recover_path)
    model = BertForSeq2SeqDecoder.from_pretrained(
        model_recover_path,
        config=config,
        mask_word_id=mask_word_id,
        search_beam_size=beam_size,
        length_penalty=length_penalty, eos_id=eos_word_ids, sos_id=sos_word_id,
        forbid_duplicate_ngrams=forbid_duplicate_ngrams, forbid_ignore_set=forbid_ignore_set,
        ngram_size=ngram_size, min_len=min_len, mode=mode,
        max_position_embeddings=max_seq_length, pos_shift=pos_shift,
    )

    if fp16:
        model.half()
    model.to(device)
    if n_gpu > 1:
        model = torch.nn.DataParallel(model)

    torch.cuda.empty_cache()
    model.eval()

    return config, tokenizer, model, bi_uni_pipeline, device
