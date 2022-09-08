import pandas as pd 


class DataFrameProcessor:
    def __init__(self, df):
        self.df = df

    def process(self):
        self.df.pop('Unnamed: 6')
        self.df['year'] = self.df['START DATE'].str.strip().str[-4:]
        self.df['state'] = self.df['LOCATION'].str.strip().str[-2:]
        self.df = self.df.dropna()
        self._remove_adsbygoogle()
        self.df['BASE SALARY'] = pd.to_numeric(self.df['BASE SALARY'])
        self.df['year'] = pd.to_numeric(self.df['year'])
        return self.df

    def _remove_adsbygoogle(self):
        pattern_clean = ".adsbygoogle."
        filter = self.df['EMPLOYER'].str.contains(pattern_clean)
        self.df = self.df[~filter]
