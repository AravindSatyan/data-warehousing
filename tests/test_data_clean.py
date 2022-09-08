
import pandas as pd  
from data_cleaner import DataFrameProcessor 

def test_process():
    data = {
        'Unnamed: 6': [None, None],
        'START DATE': ['01/01/2020', '02/01/2021'],
        'LOCATION': ['City, ST', 'Town, TS'],
        'EMPLOYER': ['CompanyA', 'CompanyB'],
        'BASE SALARY': ['100000', '120000']
    }
    df = pd.DataFrame(data)
    processor = DataFrameProcessor(df)
    processed_df = processor.process()
    assert 'Unnamed: 6' not in processed_df.columns
    assert 'year' in processed_df.columns
    assert 'state' in processed_df.columns
    assert processed_df['BASE SALARY'].dtype == 'int64'
    assert processed_df['year'].dtype == 'int64'
