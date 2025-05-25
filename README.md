# Schedule Scraper
This tool is designed to scrape the data from the official PUCP website. Specifically, it is focuse on the schedules, so it will be easier to manipulate the data in order to genate schedules for studentes with their own preferences. The reason for this tool is because as I was inspecting the website, it looks like the data is fetched in the server, so its not visible on the frontend in a comprenhensive file.

## Data Structure
The output data will be presented in a comprenhensive json data. However, in the future will be interesting to explore a reltaional data structure. 

### Structure of the data
The data is diplayed in tables in the PUCP website 13 columns and multiple rows. 
The columns are the following:
- **Curso**: The name of the course.
- **Sección**: The section of the course.
