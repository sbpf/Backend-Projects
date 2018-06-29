Description:
This project focuses on adding the authentication and authorization for an app, using oauth2.0

Steps to Create client ID and client secret for OAuth2.0 on Google:
------------------------------------------------------------------
Go to your app's page in the Google APIs Console — https://console.developers.google.com/apis
Choose Credentials from the menu on the left.
Create an OAuth Client ID.
When you're presented with a list of application types, choose Web application.
Follow through the settings and add info as necessary
You will then be able to get the client ID and client secret.
Download the client secret as a JSON data file once you have created it, rename it as "client_secrets.json"


To execute:
------------
1) Download all the files
2) execute database_setup.py to setup the database
3) execute lotsofmenus.py to add records to tables
4) place the client_secrets.json file in the same folder as the project.py
5) run project.py to start the server
6) access the application on localhost port 5000


Steps followed to add the google-sign on feature:
---------------------------------------------------
1) Necessary imports as mentioned in projects.py
2) Fetch the client_id from the client_secrets json file
3) Connect to the database and create database session
4) Create anti-forgery state token
5) Write a callback function that is executed when the user logs in, and implement the following:
   ->Validate the state token
   ->Obtain authorization code
   ->check that the access token in valid
   ->verify that the access token is used for intended user
   ->store the access token in the session object for later use
6) implement necessary authorization in all the route methods to check if there is a user logged in
and customize all the data operations based on the user_id of the logged in user


