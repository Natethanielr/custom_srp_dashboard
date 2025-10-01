# Custom SRP Dashboard  
  
## Purpose:   
  
With energy costs on the rise around the country, it is more important than ever to closly monitor electricity use and cost. The information from the SRP.net shows the daily and hourly cost and energy use /(In USD and kWh respectivly/). That is the only information that can be gained at first glance from the webpage. I want to expand information and analysis of the usage data and create a custom dashboard to display that analysis. Primarily, I am interested in identifying days which have consitently above average energy usage, and, specifically, during what times I am seeing high usage. This information will help me identify where I can reduce energy use, and also determine if differnt price structures from SRP would be benificial. Currently, the project is only set up for personal use, however, I plan to expand the functionality to allow it to be used generally.  
  
  
## Built With: 

- Python 
- Jupyter Notebook 
- Front end somehow 
  
  
## Structure
srp/  
|  
|-- data/  
|  
|-- notebooks/  
    |     --srp.ipynb  
|-- src  
    |     --import_data.py  
    |     --analysis.py  
    |     --figures.py
|--tests  
    |     --testing.py  
  
  
## Notes on files: 
This is a personal repo built primaraly for practice and learning. As a result, the jupyter noreboo in the file exist as a history of the begining. I began working on this as a data analystics project just to look at what my own data. I have left the notebook in the repo because much of the analysis and plotting code came from that notebook. If I decide to make this a public tool, there will be a new repo created that has a cleaner structure. There is not yet a well defined data pipeline and relys on file paths on unix machines. 
  
You can only download one month at a time of daily data from SRP. Because of this, in the data folder there is a script to combine files to make one csv will all the hourly data. 

## What is project_req.md: 

This is under development, project req is a way for me to track project requirements and todos. I come from a systems engineering background, and that is evident in the way the requirements are written and structured. 


