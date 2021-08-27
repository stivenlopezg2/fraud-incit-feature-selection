import pandas as pd
from sklearn.feature_selection import VarianceThreshold


class FilterSelector:
    """

    """
    def __init__(self, threshold: float = 1.0):
        if not isinstance(threshold, float):
            raise TypeError("Error: el parametro threshold debe ser de tipo float.")
        self.threshold = threshold

    def apply_variance_selector(self, data: pd.DataFrame):
        """

        Parameters
        ----------
        data: pd.DataFrame :
            

        Returns
        -------

        """
        X = data.select_dtypes(include="number")
        threshold = float(1 - self.threshold)
        selector = VarianceThreshold(threshold=threshold).fit(X)
        cols_to_drop = data.columns[~selector.get_support()]
        return cols_to_drop

    def apply_quasiconstant_selector(self, data: pd.DataFrame):
        """

        Parameters
        ----------
        data: pd.DataFrame :
            

        Returns
        -------

        """
        quasi_constants = []
        for col in data.columns.tolist():
            if data[col].dtype in [int, float]:
                most_freq = data[col].value_counts(normalize=True).sort_values(ascending=False).values[0]
                if most_freq > self.threshold:
                    quasi_constants.append(col)
            else:
                continue
        return quasi_constants

    def apply_correlation_selector(self, corr_matrix: pd.DataFrame):
        """

        Parameters
        ----------
        corr_matrix: pd.DataFrame :
            

        Returns
        -------

        """
        col_corr = set()
        for col_i in range(len(corr_matrix.columns)):
            for col_j in range(col_i):
                if abs(corr_matrix.iloc[col_i, col_j]) > self.threshold:
                    col_corr.add(corr_matrix.columns[col_i])
        return col_corr

