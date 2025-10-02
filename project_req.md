# Custom SRP Dashboard Project Requirements  

## Mission Statement:  
  
With energy costs on the rise around the country, it is more important than ever to closly monitor electricity use and cost. The information from the SRP.net shows the daily and hourly cost and energy use /(In USD and kWh respectivly/). That is the only information that can be gained at first glance from the webpage. I want to expand information and analysis of the usage data and create a custom dashboard to display that analysis.  
  
## Requirements:  
1: -> Backend  
2: -> Frontend  
  
### Data
1.0: Data pipeline and handeling  
1.01: Import data from SRP.net  
1.02: Convert that data into a format so that analysis can be performed on it  
1.03: Store data in a location that can be accessed and sorted  
  
### Analysis
1.1: Analysis    
1.11: Calculate mean, min, max, and standard deviation of data set   
1.12: Identify the days that are above the average energy use   
1.13: Identify days of the week that consitently show above average use   
1.14: Identify hours that see high energy use   
1.15: Identify hours within the high use days that are high in energy use   
  
### Plotting
1.3: Figues:  
1.31: Plot the energy cost over specified date range, days on the y axis, cost on the x axix,
    add temperature on x axis.  
1.31.1: Plot the days as a bar chart and add the temperature as a line graph
1.3.2: Bar graph of days of the week in chronological order in x axis, and count of times above     average on the y axis  
1.33: Plot hourly data of top 4 high use days 
  
  
## TODO: 

- FIX MY F****** VARIABLE NAMES
- Graph high use days 
- Identify days + 1/2 std
- Possibly generate the "average" day (get mean of use during hours and graph the means)
- Possibly generate the "average" high use day
- Calculate what hours in the day have highest use
