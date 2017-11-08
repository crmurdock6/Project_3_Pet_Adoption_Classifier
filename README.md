## Project McNulty

##### Back story:

Using either data from the web (API or scraped) or one of the optional supplied data sets, what can we learn via supervised learning techniques? Extend your findings with a flask website.

##### Data:

 * **acquisition**: download, api's, scraping
 * **storage**: PostgreSQL

##### Skills:

   * supervised learning
   * SQL
   * Flask

### Project Workflow

For project 3, I focused on predicting the probability of a dog being adopted
from a shelter. There are 1.6 million dogs that go unadopted every year and, as I have adopted
a dog, was curious to see if there is any way we can determine what animals might need special attention and why.

For this classification project, data from an animal shelter in Houston was used (see data folder
for raw data files) and multiple models were built. The code, with data cleaning modules in the code subfolder, was broken up in the code folder as follows:

1. Part_1_Animal_Outcomes_Data_Exploration.ipynb
2. Part_2_Intake_Data_Exploration.ipynb
3. Part_3_psql_queries.ipynb
4. Part_4_Modeling_Including_Time_In_Shelter.ipynb
5. Part_5_Modeling_from_Day_1.ipynb

Finally, a flask app was made that will allow users to input features, hit submit, and return whether the animal will be adopted or not and the percentage!
