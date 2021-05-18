"""CompatibleAdaBoostClassifier: Re-implements AdaBoost in imbalanced_ensemble style.
"""

# Authors: Zhining Liu <zhining.liu@outlook.com>
# License: MIT

import numpy as np

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble._forest import BaseForest
from sklearn.tree import BaseDecisionTree
from sklearn.utils import check_random_state
from sklearn.utils.validation import _check_sample_weight


from ..base import ImbalancedEnsembleClassifierMixin, MAX_INT
from ...utils._validation_data import check_eval_datasets
from ...utils._validation_param import (check_train_verbose, 
                                        check_eval_metrics)
from ...utils._validation import _deprecate_positional_args
from ...utils._docstring import (Substitution, FuncSubstitution, 
                                 FuncGlossarySubstitution,
                                 _get_parameter_docstring, 
                                 _get_example_docstring)

# # For local test
# import sys
# sys.path.append("../..")
# from ensemble.base import ImbalancedEnsembleClassifierMixin, MAX_INT
# from utils._validation_data import check_eval_datasets
# from utils._validation_param import (check_train_verbose, 
#                                      check_eval_metrics)
# from utils._validation import _deprecate_positional_args
# from utils._docstring import (Substitution, FuncSubstitution, 
#                               _get_parameter_docstring, 
#                               _get_example_docstring)


# Properties
_method_name = 'CompatibleAdaBoostClassifier'

_properties = {
    'ensemble_type': 'boosting',
    'training_type': 'iterative',
}

_super = AdaBoostClassifier


@Substitution(
    example=_get_example_docstring(_method_name)
)
class CompatibleAdaBoostClassifier(ImbalancedEnsembleClassifierMixin, 
                                   AdaBoostClassifier):
    """AdaBoost classifier re-implemented in imbalanced-ensemble style.

    An AdaBoost [1] classifier is a meta-estimator that begins by fitting a
    classifier on the original dataset and then fits additional copies of the
    classifier on the same dataset but where the weights of incorrectly
    classified instances are adjusted such that subsequent classifiers focus
    more on difficult cases.

    This class implements the algorithm known as AdaBoost-SAMME [2].

    Parameters
    ----------
    base_estimator : object, default=None
        The base estimator from which the boosted ensemble is built.
        Support for sample weighting is required, as well as proper
        ``classes_`` and ``n_classes_`` attributes. If ``None``, then
        the base estimator is :class:`~sklearn.tree.DecisionTreeClassifier`
        initialized with `max_depth=1`.

    n_estimators : int, default=50
        The maximum number of estimators at which boosting is terminated.
        In case of perfect fit, the learning procedure is stopped early.

    learning_rate : float, default=1.
        Learning rate shrinks the contribution of each classifier by
        ``learning_rate``. There is a trade-off between ``learning_rate`` and
        ``n_estimators``.

    algorithm : {{'SAMME', 'SAMME.R'}}, default='SAMME.R'
        If 'SAMME.R' then use the SAMME.R real boosting algorithm.
        ``base_estimator`` must support calculation of class probabilities.
        If 'SAMME' then use the SAMME discrete boosting algorithm.
        The SAMME.R algorithm typically converges faster than SAMME,
        achieving a lower test error with fewer boosting iterations.

    random_state : int, RandomState instance or None, default=None
        Controls the random seed given at each `base_estimator` at each
        boosting iteration.
        Thus, it is only used when `base_estimator` exposes a `random_state`.
        Pass an int for reproducible output across multiple function calls.

    Attributes
    ----------
    base_estimator_ : estimator
        The base estimator from which the ensemble is grown.

    estimators_ : list of classifiers
        The collection of fitted sub-estimators.
        
    estimators_n_training_samples_ : list of ints
        The number of training samples for each fitted 
        base estimators.

    classes_ : ndarray of shape (n_classes,)
        The classes labels.

    n_classes_ : int
        The number of classes.

    estimator_weights_ : ndarray of floats
        Weights for each estimator in the boosted ensemble.

    estimator_errors_ : ndarray of floats
        Classification error for each estimator in the boosted
        ensemble.
        
    estimators_n_training_samples_ : list of ints
        The number of training samples for each fitted 
        base estimators.

    feature_importances_ : ndarray of shape (n_features,)
        The impurity-based feature importances if supported by the
        ``base_estimator`` (when based on decision trees).

    See Also
    --------
    CompatibleBaggingClassifier : Bagging re-implemented in imbalanced-ensemble style.

    References
    ----------
    .. [1] Y. Freund, R. Schapire, "A Decision-Theoretic Generalization of
           on-Line Learning and an Application to Boosting", 1995.

    .. [2] J. Zhu, H. Zou, S. Rosset, T. Hastie, "Multi-class AdaBoost", 2009.
    
    Examples
    --------
    {example}
    """
    
    def __init__(self,
                base_estimator=None,
                n_estimators:int=50,
                learning_rate:float=1.,
                algorithm:str='SAMME.R',
                random_state=None):

        super(CompatibleAdaBoostClassifier, self).__init__(
            base_estimator=base_estimator,
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            algorithm=algorithm,
            random_state=random_state)

        self.__name__ = _method_name
        self._properties = _properties


    @_deprecate_positional_args
    @FuncSubstitution(
        eval_datasets=_get_parameter_docstring('eval_datasets'),
        eval_metrics=_get_parameter_docstring('eval_metrics'),
        train_verbose=_get_parameter_docstring('train_verbose', **_properties),
    )
    def fit(self, X, y, 
            *,
            sample_weight=None,
            eval_datasets: dict = None,
            eval_metrics: dict = None,
            train_verbose: bool or int or dict = True,
            ):
        """Build a boosted classifier from the training set (X, y).

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The training input samples. Sparse matrix can be CSC, CSR, COO,
            DOK, or LIL. COO, DOK, and LIL are converted to CSR.

        y : array-like of shape (n_samples,)
            The target values (class labels).

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, the sample weights are initialized to
            ``1 / n_samples``.
        
        %(eval_datasets)s
        
        %(eval_metrics)s
        
        %(train_verbose)s

        Returns
        -------
        self : object
        """

        # Check that algorithm is supported.
        if self.algorithm not in ('SAMME', 'SAMME.R'):
            raise ValueError("algorithm %s is not supported" % self.algorithm)

        # Check parameters.
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be greater than zero")

        if (self.base_estimator is None or
                isinstance(self.base_estimator, (BaseDecisionTree,
                                                 BaseForest))):
            DTYPE = np.float64  # from fast_dict.pxd
            dtype = DTYPE
            accept_sparse = 'csc'
        else:
            dtype = None
            accept_sparse = ['csr', 'csc']
        
        check_x_y_args = {
            'accept_sparse': accept_sparse,
            'ensure_2d': True,
            'allow_nd': True,
            'dtype': dtype,
            'y_numeric': False,
        }
        X, y = self._validate_data(X, y, **check_x_y_args)

        # Check evaluation data
        self.eval_datasets_ = check_eval_datasets(eval_datasets, X, y, **check_x_y_args)

        self.classes_, y = np.unique(y, return_inverse=True)
        self.n_classes_ = len(self.classes_)
        
        # Store original class distribution
        self.origin_distr_ = dict(Counter(y))
        self.target_distr_ = dict(Counter(y))

        self.eval_metrics_ = check_eval_metrics(eval_metrics)

        self.train_verbose_ = check_train_verbose(
            train_verbose, self.n_estimators, **self._properties)
        
        self._init_training_log_format()

        # Check sample weight
        sample_weight = _check_sample_weight(sample_weight, X, np.float64)
        sample_weight /= sample_weight.sum()
        if np.any(sample_weight < 0):
            raise ValueError("sample_weight cannot contain negative weights")
        
        self.raw_sample_weight_ = sample_weight
        
        sample_weight = copy(self.raw_sample_weight_)    

        self._validate_estimator()

        # Check random state
        random_state = check_random_state(self.random_state)

        # Clear any previous fit results.
        self.estimators_ = []
        self.estimator_weights_ = np.zeros(self.n_estimators, dtype=np.float64)
        self.estimator_errors_ = np.ones(self.n_estimators, dtype=np.float64)
        self.estimators_n_training_samples_ = np.zeros(self.n_estimators, dtype=np.int)
        
        # Genrate random seeds array
        seeds = random_state.randint(MAX_INT, size=self.n_estimators)
        self._seeds = seeds

        for iboost in range(self.n_estimators):
            # Boosting step
            sample_weight, estimator_weight, estimator_error = self._boost(
                iboost,
                X, y,
                sample_weight,
                random_state)

            self.estimator_weights_[iboost] = estimator_weight
            self.estimator_errors_[iboost] = estimator_error
            self.estimators_n_training_samples_[iboost] = y.shape[0]
            
            # Print training infomation to console.
            self._training_log_to_console(iboost, y)
            
            # Early termination.
            if sample_weight is None:
                break
            
            # Stop if error is zero.
            if estimator_error == 0:
                print (
                    f"Training early-stop at iteration {iboost+1}"
                    f" (training error is 0)."
                    )
                break

            sample_weight_sum = np.sum(sample_weight)

            # Stop if the sum of sample weights has become non-positive.
            if sample_weight_sum <= 0:
                break

            if iboost < self.n_estimators - 1:
                # Normalize.
                sample_weight /= sample_weight_sum

        return self


    @FuncGlossarySubstitution(_super.decision_function, 'classes_')
    def decision_function(self, X):
        return super().decision_function(X)


    @FuncGlossarySubstitution(_super.predict_log_proba, 'classes_')
    def predict_log_proba(self, X):
        return super().predict_log_proba(X)


    @FuncGlossarySubstitution(_super.predict_proba, 'classes_')
    def predict_proba(self, X):
        return super().predict_proba(X)


    @FuncGlossarySubstitution(_super.staged_decision_function, 'classes_')
    def staged_decision_function(self, X):
        return super().staged_decision_function(X)


    @FuncGlossarySubstitution(_super.staged_predict_proba, 'classes_')
    def staged_predict_proba(self, X):
        return super().staged_predict_proba(X)


# %%

if __name__ == '__main__':
    from collections import Counter
    from copy import copy
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
    
    # X, y = make_classification(n_classes=2, class_sep=2, # 2-class
    #     weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0,
    #     n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=10)
    X, y = make_classification(n_classes=3, class_sep=2, # 3-class
        weights=[0.1, 0.3, 0.6], n_informative=3, n_redundant=1, flip_y=0,
        n_features=20, n_clusters_per_class=1, n_samples=2000, random_state=10)

    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.5, random_state=42)

    origin_distr = dict(Counter(y_train)) # {2: 600, 1: 300, 0: 100}
    print('Original training dataset shape %s' % origin_distr)

    init_kwargs_default = {
        'base_estimator': None,
        'n_estimators': 100,
        'learning_rate': 1.,
        'algorithm': 'SAMME.R',
        'random_state': 42,
        # 'random_state': None,
    }
    fit_kwargs_default = {
        'X': X_train,
        'y': y_train,
        'sample_weight': None,
        'eval_datasets': {'valid': (X_valid, y_valid)},
        'eval_metrics': {
            'acc': (accuracy_score, {}),
            'balanced_acc': (balanced_accuracy_score, {}),
            'weighted_f1': (f1_score, {'average':'weighted'}),},
        'train_verbose': {
            'granularity': 10,
            'print_distribution': True,
            'print_metrics': True,},
    }

    ensembles = {}

    init_kwargs, fit_kwargs = copy(init_kwargs_default), copy(fit_kwargs_default)
    adaboost_comp = CompatibleAdaBoostClassifier(**init_kwargs).fit(**fit_kwargs)
    ensembles['adaboost_comp'] = adaboost_comp


    # %%
    from visualizer import ImbalancedEnsembleVisualizer

    visualizer = ImbalancedEnsembleVisualizer(
        eval_datasets = None,
        eval_metrics = None,
    ).fit(
        ensembles = ensembles,
        granularity = 5,
    )
    fig, axes = visualizer.performance_lineplot(
        on_ensembles=None,
        on_datasets=None,
        split_by=[],
        n_samples_as_x_axis=False,
        sub_figsize=(4, 3.3),
        sup_title=True,
        alpha=0.8,
    )
    fig, axes = visualizer.confusion_matrix_heatmap(
        on_ensembles=None,
        on_datasets=None,
        sub_figsize=(4, 3.3),
    )

    # %%
