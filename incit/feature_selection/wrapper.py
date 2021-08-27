import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_selection import SequentialFeatureSelector


class WrapperSelector(BaseEstimator, TransformerMixin):
    """ """
    def __init__(self, estimator, k_features: int, forward: bool, scoring: str, n_jobs=-1):
        if not isinstance(k_features, int):
            raise TypeError("Error: el parametro k_features debe ser tipo int.")
        if not isinstance(forward, bool):
            raise TypeError("Error: el parametro forward debe ser tipo bool.")
        if not isinstance(scoring, str):
            raise TypeError("Error: el parametro scoring debe ser tipo str.")
        self.estimator = estimator
        self.k_features = k_features
        self.forward = forward
        self.scoring = scoring
        self.n_jobs = n_jobs
        self.selector = None

    def fit(self, X: pd.DataFrame, y: pd.Series, **kwargs):
        """

        Parameters
        ----------
        X : pd.DataFrame :
            
        y : pd.Series :
            
        **kwargs :
            
        X: pd.DataFrame :
            
        y: pd.Series :
            

        Returns
        -------

        
        """
        params = {
            "estimator": self.estimator,
            "k_features": self.k_features,
            "forward": self.forward,
            "scoring": self.scoring,
            "n_jobs": self.n_jobs
        }
        self.selector = SequentialFeatureSelector(**params, **kwargs)
        self.selector.fit(X, y,)
        return self.selector

    def transform(self, X: pd.DataFrame, y: pd.Series = None) -> pd.DataFrame:
        """

        Parameters
        ----------
        X: pd.DataFrame :
            
        y: pd.Series :
             (Default value = None)

        Returns
        -------

        """
        cols = X.columns[self.selector.get_support()]
        X = pd.DataFrame(self.selector.transform(X), columns=cols)
        return X
