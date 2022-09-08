# Data Cleaner 

Data Cleaner is a Python package for cleaning data frames that you obtain from h1bdata.info

## Installation

You can install the package using pip:

```bash
pip install pip install cleanh1b 


usage

import pandas as pd
from data_cleaner import DataFrameProcessor

# Load your DataFrame
keyword='data engineer'
keyword='+'.join(keyword.split())
url='https://h1bdata.info/index.php?em=&job={}&city=&year=All+Years'.format(keyword)
data = requests.get(url)
soup=BeautifulSoup(data.content,'html.parser')
table = soup.find('table')
df_sub = pd.read_html(str(table))[0]

# Create an instance of DataFrameProcessor
processor = DataFrameProcessor(df)

# Process the DataFrame
processed_df = processor.process()

# Display the processed DataFrame
print(processed_df)

