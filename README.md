# Job-Web-Scraper
This project is a python-based web scraper.
# Installation
Download the main file and run as a python script. Our team used the PyCharm IDE to run this code.
# Description
The motivation behind this project is to create a way to reduce the time spent looking for a job by viewing data from multiple websites at once.
This program can scrape job listing information such as job title, location, job description, and a link from all selected websites simultaneously.
It can then return this information to the user through the Graphical User Interface.
This project makes use of four libraries: requests, Beautiful Soup, PySimpleGUI, and Asyncio.
The user can choose which website to gather information through the checkboxes on the GUI and then add parameters such as Job Title with the text boxes.
The other classes were created to test each website individaully before adding them to the main class.
# Usage
Running the python file will open the gui as shown below.
![image](https://user-images.githubusercontent.com/62351065/165407560-d9324168-8aa8-4173-b45d-4aaf37f1bf79.png)
Each checkbox allows the user to choose which scrapers they would like to use.
The input text bars allow the user to fill in any limitations they would want in the results.
The submit button submits runs the selected scrapers and passes any inputs to them.
The cancel button closes the program.
The clear all button clears all output from the output textbox.
After submission the output text box will show any listings that matched the inputs and how many
were returned from each scraped website (see image below).
![image](https://user-images.githubusercontent.com/62351065/165407522-dcc64571-29c0-42bf-865f-b5e8842ce08d.png)
