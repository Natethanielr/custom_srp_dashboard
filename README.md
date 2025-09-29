# Electricity Usage 

## Purpose 

The information I get from the srp dashboard is good, but I wanted more indepth information about electricity use. The goal of this project is to get a more substantial view of usage trends, identify days and times of above average usage, and create a plan to reduce electricty costs. 

## Structure
srp/
|
|-- data/
|
|-- notebooks/
|   --srp.ipynb
|-- src
|   --import_data.py
|   --analysis.py
|--tests
|   --testing.py
The jupyter notebook contains the base for this project. In that notebook, I explore trends and write the baseline code for the rest of the project. The accompanying python code is a cleaned up, streamlined code base to later be integrated into a dashboard. 

# Data
Contains the csv files downloaded from srp.net. The hourly totals cannot be downloaded as one data set, so they are combined then saved as a new csv. 

# Notebooks
Includes the main srp.ipynb that has the core of the project, the exploritory code, and main ideas for the code. 

# src
Source for the python pipeline. 

## import_data.py
Defines the functions for importing, cleaning, and moduifying the srp csv into dataframes to beo later be integrated into a dashboard. 
There must be a better way to do this, both functions are almost identical. The only difference is that the hourly cost need an additional interval column, and the order of operations of coverting usage date to date time matters in this context. Did not matter when it was in the notebook, but now that I have the damn function the order fucks shit up. 
# Data
Contains the csv files downloaded from srp.net. The hourly totals cannot be downloaded as one data set, so they are combined then saved as a new csv. 

# Notebooks
Includes the main srp.ipynb that has the core of the project, the exploritory code, and main ideas for the code. 

# src
Source for the python pipeline. 

## import_data.py
Defines the functions for importing, cleaning, and moduifying the srp csv into dataframes to be used in the rest of the project. The code should be self documenting, but main idea is read -> convert to df ->drop n/a ->add datetime 
