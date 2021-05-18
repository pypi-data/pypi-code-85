﻿"""Class to perform over-sampling using ADASYN."""
# Adapted from imbalanced-learn

# Authors: Guillaume Lemaitre <g.lemaitre58@gmail.com>
#          Christos Aridas
#          Zhining Liu <zhining.liu@outlook.com>
# License: MIT

import numpy as np
from scipy import sparse

from sklearn.preprocessing import normalize
from sklearn.utils import check_random_state
from sklearn.utils import _safe_indexing


from .base import BaseOverSampler
from ...utils._docstring import _n_jobs_docstring, Substitution
from ...utils._docstring import _random_state_docstring
from ...utils._validation import (_deprecate_positional_args,
                                  check_neighbors_object)

# # For local test
# import sys
# sys.path.append("../..")
# from sampler.over_sampling.base import BaseOverSampler
# from utils._docstring import _n_jobs_docstring, Substitution
# from utils._docstring import _random_state_docstring
# from utils._validation import (_deprecate_positional_args,
#                                check_neighbors_object)

@Substitution(
    sampling_strategy=BaseOverSampler._sampling_strategy_docstring,
    n_jobs=_n_jobs_docstring,
    random_state=_random_state_docstring,
)
class ADASYN(BaseOverSampler):
    """Oversample using Adaptive Synthetic (ADASYN) algorithm.

    This method is similar to SMOTE but it generates different number of
    samples depending on an estimate of the local distribution of the class
    to be oversampled.

    Read more in the `User Guide <https://imbalanced-learn.org/stable/over_sampling.html#smote-adasyn>`_.

    Parameters
    ----------
    {sampling_strategy}

    {random_state}

    n_neighbors : int or estimator object, default=5
        If ``int``, number of nearest neighbours to used to construct synthetic
        samples.  If object, an estimator that inherits from
        :class:`~sklearn.neighbors.base.KNeighborsMixin` that will be used to
        find the k_neighbors.

    {n_jobs}

    See Also
    --------
    SMOTE : Over-sample using SMOTE.

    SVMSMOTE : Over-sample using SVM-SMOTE variant.

    BorderlineSMOTE : Over-sample using Borderline-SMOTE variant.

    Notes
    -----
    The implementation is based on [1]_.

    Supports multi-class resampling. A one-vs.-rest scheme is used.

    References
    ----------
    .. [1] He, Haibo, Yang Bai, Edwardo A. Garcia, and Shutao Li. "ADASYN:
       Adaptive synthetic sampling approach for imbalanced learning," In IEEE
       International Joint Conference on Neural Networks (IEEE World Congress
       on Computational Intelligence), pp. 1322-1328, 2008.

    Examples
    --------
    >>> from collections import Counter
    >>> from sklearn.datasets import make_classification
    >>> from imbalanced_ensemble.sampler.over_sampling import \
ADASYN # doctest: +NORMALIZE_WHITESPACE
    >>> X, y = make_classification(n_classes=2, class_sep=2,
    ... weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0,
    ... n_features=20, n_clusters_per_class=1, n_samples=1000,
    ... random_state=10)
    >>> print('Original dataset shape %s' % Counter(y))
    Original dataset shape Counter({{1: 900, 0: 100}})
    >>> ada = ADASYN(random_state=42)
    >>> X_res, y_res = ada.fit_resample(X, y)
    >>> print('Resampled dataset shape %s' % Counter(y_res))
    Resampled dataset shape Counter({{0: 904, 1: 900}})
    """

    @_deprecate_positional_args
    def __init__(
        self,
        *,
        sampling_strategy="auto",
        random_state=None,
        n_neighbors=5,
        n_jobs=None,
    ):
        super().__init__(sampling_strategy=sampling_strategy)
        self.random_state = random_state
        self.n_neighbors = n_neighbors
        self.n_jobs = n_jobs

    def _validate_estimator(self):
        """Create the necessary objects for ADASYN"""
        self.nn_ = check_neighbors_object(
            "n_neighbors", self.n_neighbors, additional_neighbor=1
        )
        self.nn_.set_params(**{"n_jobs": self.n_jobs})

    def _fit_resample(self, X, y, sample_weight=None):
        self._validate_estimator()
        random_state = check_random_state(self.random_state)

        X_resampled = [X.copy()]
        y_resampled = [y.copy()]

        for class_sample, n_samples in self.sampling_strategy_.items():
            if n_samples == 0:
                continue
            target_class_indices = np.flatnonzero(y == class_sample)
            X_class = _safe_indexing(X, target_class_indices)

            self.nn_.fit(X)
            nns = self.nn_.kneighbors(X_class, return_distance=False)[:, 1:]
            # The ratio is computed using a one-vs-rest manner. Using majority
            # in multi-class would lead to slightly different results at the
            # cost of introducing a new parameter.
            n_neighbors = self.nn_.n_neighbors - 1
            ratio_nn = np.sum(y[nns] != class_sample, axis=1) / n_neighbors
            if not np.sum(ratio_nn):
                raise RuntimeError(
                    "Not any neigbours belong to the majority"
                    " class. This case will induce a NaN case"
                    " with a division by zero. ADASYN is not"
                    " suited for this specific dataset."
                    " Use SMOTE instead."
                )
            ratio_nn /= np.sum(ratio_nn)
            n_samples_generate = np.rint(ratio_nn * n_samples).astype(int)
            # rounding may cause new amount for n_samples
            n_samples = np.sum(n_samples_generate)
            if not n_samples:
                raise ValueError(
                    "No samples will be generated with the provided ratio settings."
                )

            # the nearest neighbors need to be fitted only on the current class
            # to find the class NN to generate new samples
            self.nn_.fit(X_class)
            nns = self.nn_.kneighbors(X_class, return_distance=False)[:, 1:]

            enumerated_class_indices = np.arange(len(target_class_indices))
            rows = np.repeat(enumerated_class_indices, n_samples_generate)
            cols = random_state.choice(n_neighbors, size=n_samples)
            diffs = X_class[nns[rows, cols]] - X_class[rows]
            steps = random_state.uniform(size=(n_samples, 1))

            if sparse.issparse(X):
                sparse_func = type(X).__name__
                steps = getattr(sparse, sparse_func)(steps)
                X_new = X_class[rows] + steps.multiply(diffs)
            else:
                X_new = X_class[rows] + steps * diffs

            X_new = X_new.astype(X.dtype)
            y_new = np.full(n_samples, fill_value=class_sample, dtype=y.dtype)
            X_resampled.append(X_new)
            y_resampled.append(y_new)

        if sparse.issparse(X):
            X_resampled = sparse.vstack(X_resampled, format=X.format)
        else:
            X_resampled = np.vstack(X_resampled)
        y_resampled = np.hstack(y_resampled)
        
        # If given sample_weight
        if sample_weight is not None:
            # sample_weight is already validated in self.fit_resample()
            sample_weight_new = \
                np.empty(y_resampled.shape[0] - y.shape[0], dtype=np.float64)
            sample_weight_new[:] = np.mean(sample_weight)
            sample_weight_resampled = np.hstack([sample_weight, sample_weight_new]).reshape(-1, 1)
            sample_weight_resampled = \
                np.squeeze(normalize(sample_weight_resampled, axis=0, norm='l1'))
            return X_resampled, y_resampled, sample_weight_resampled
        else: return X_resampled, y_resampled

    def _more_tags(self):
        return {
            "X_types": ["2darray"],
        }

# %%

if __name__ == "__main__":
    from collections import Counter
    from sklearn.datasets import make_classification

    X, y = make_classification(n_classes=3, class_sep=2,
        weights=[0.1, 0.3, 0.6], n_informative=3, n_redundant=1, flip_y=0,
        n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=10)
    print('Original dataset shape %s' % Counter(y))

    origin_distr = Counter(y)
    target_distr = {2: 600, 1: 400, 0: 300}
    
    print ('ADASYN Resampling ...')
    smote = ADASYN(random_state=42, sampling_strategy=target_distr)
    X_res, y_res, weight_res = smote.fit_resample(X, y, sample_weight=y)
    # X_res, y_res, weight_res = smote.fit_resample(X, y, sample_weight='a')

    print('Resampled dataset shape %s' % Counter(y_res))
    print('Test resampled weight shape %s' % Counter(weight_res))

# %%

