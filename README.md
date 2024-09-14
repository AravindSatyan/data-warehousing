# Data Cleaner

Data Cleaner 🧹 is a Python package created to simplify cleaning data frames from DoL Performance Data. As an international student juggling campus jobs, adjusting to a new culture, and pushing through a master’s program, life can get super busy. 🏫🌍

That’s why I built this package—to help others save time ⏳ and focus on what really matters: landing that dream job 🎯. With this tool, you can easily type in the job you’re aiming for and get a detailed comparison of companies, roles, and locations that match your needs.

At the heart of it 💙, this package is all about cutting down the hours spent cleaning through massive datasets so you can focus on making informed, life-changing decisions 🔑 for your future! 🚀
PS: Experienced folks can work their way too because H1b's are issued to everyone.

## Installation

You can install the package using pip:

```bash
pip install h1b-processor

from clean_h1b import data_cleaner

# Create an instance of data_cleaner
processor = data_cleaner(keywords = 'data')

# Process the DataFrame
processed_df = processor.process()

# Display the processed DataFrame
print(processed_df)

#if you want csv, then:
processed_df.to_csv('outputfile.csv')

# Display the processed DataFrame
print(processed_df) #optional

```
Some examples are:

Physician:
![image](https://github.com/user-attachments/assets/d6975628-c5a9-400e-b036-4c0c0eccae36)

Attorney:
![image](https://github.com/user-attachments/assets/39e8b788-9611-4d4c-b351-438c623465a2)

Software Engineer:
![image](https://github.com/user-attachments/assets/16d465dd-86f1-40b7-9676-42a32a3d34d6)

Financial Analyst:
![image](https://github.com/user-attachments/assets/ca1bce41-9ba9-46d6-866d-3f18bffefd28)

Psychologist:
![image](https://github.com/user-attachments/assets/e0ab969d-c602-40ef-a8b3-0552f05a924f)

Experienced Folks, listen up 📢 🏫 🌍
Partner:
![image](https://github.com/user-attachments/assets/da558123-71dd-4318-a59c-fbb7d434262c)
