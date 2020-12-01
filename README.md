# W6-Api-sentiment-project
**CREATING MY OWN API**
### 1. PROJECT
The purpose of this project is to create my own API with different endpoints so that through the GET method, customers are able to get the necessary information they need. To do this the steps to follow are:
    
1. Search for a dataset in the Kaggle platform.

2. Open in Jupyter Notebook the chosen dataset and clean it and keep the data I consider necessary.

3. Once the dataset is clean, I link it to MongoDB Compass to start working on the API. 

4. Using the Flask library I have been able to develop the API.

### 2. PROJECT STRUCTURE 
From the text editor Visual Code I organize the whole project in different folders to have it organized and to be able to see it in a visual way. The folders are the following:

- 'Data': there you can find the dataset, both in a cdv format, and a .json to be able to enter it in MongoDB.

- 'Config': inside is a configuration .py where I make the connection with MongoDB and where I import the link (saved in a .env file, which is a hidden file).

- 'Tools': there are three files:
    1. init.py: where I indicate the path that has to follow to get the dataset.
    2. getdata.py: I make the first query to the database for a person's phrases.
    3. postdata.py: I define a function to be able to add data to the Mongo database. 

- 'Notebooks': I add the Jupyter Notebooks where I develop the project a little bit and I make sure it works properly with the functions previously set in the Visual Code. It should be emphasized that one of them is the analysis of polarity, that is, a sentimental analysis of each of the speakers in the debate (the database). 

- 'miapi.py': I develop the whole project in this folder. I import functions and it is where I perform the GET and POST methods of the API itself. 



