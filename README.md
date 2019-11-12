
# Project : pythonassignment3
This repository holds a CRUD project in Flask, MongoDB database about Technology articles.

### Start the project3
To run the API locally clone the repo and run 
```
python3 app.py
```

# pythonassignment3
https:// https://pythonassignment3.herokuapp.com/

Pythonassignment3 is a blockchain information Hub to allow our company to learn and 
share the effect mechanism allowing programmable transactions It related or able to integrate to AI & IOT , etc. Ethereum network, for example, part of blockchain language, used to write such scripts is aTuring complete blockchain transaction.  This Blockchain Hub consist news sharing not only on Blockchain and also IOT, AI, and how python in AI, etc. 

# UX Design
### User Experience
Pythonassignment3 is a blockchain information Hub is for the company internally who want to update, create and experience difference types of technology on Blockchain.
User story
•   As a user, I want to learn and know more about Blockchain and related technology 
•   As a user, I able to add new blockchain technology new and all detail to share internally 
•   As an admin, I want it easy to control everything
•   As an admin, I want to have a one hub for company to communicate and a place to learn new skill on related on Blockchain technology. 
•   As admin, a hub to learn blockchain confidently and new languages 

### The best way to learn & achieve the above:
Questions: where do I start, and when will I master it?

3 attainable ways to speed on blockchain and decentralized learning:
1. Keep update the blockchain information hub and share experience. User can update the latest of news and try to keep as 12 news updates 
2. Read, update, engage!
The Blockchain information Hub is an excellent source for company internally for understanding what is happening in the blockchain, and looks across all blockchain related technologies. 
3. Meet up!
Share and test the blockchain experience to contribute back to company.

# Existing Features
•   Feature 1 - allows user to to register, login, by having them fill out login form
•   Feature 2 - allows user to add new blockchain news, edit blockchain news and delete it
•   Feature 3 - allows user to have a hub of enjoying sharing their own interest blockchain news
### Features
Authentication login and out 
Authentication is the process of determining whether someone or something is, in fact, who or what it declares itself to be. Authentication technology provides access control for systems by checking to see if a user's credentials match the credentials in a database of authorized users or in a data 

# Add Blockchain news
A user is able add new blockchain news to the database and therefore the site using Pymongo (API of ymongoBD)s insert-one() function.The upvotes section is not seen on the form, a function is used to produce a number between 0-10000 and applied to the blockchain news. This is to show how the functionality would work with a live website.

# Edit Blockchain news
A user is able to make edits to blockchain news found on the website. Pymongo (API of mongoBD) allocates each entry into a collection with an object ID and this is what is used to locate the individual blockchain news the user wants to edit and pre-fill the form for the user. After the user has made the necessary changes, they submit the form and Pymongo (API of mongoBD)'s update () method to update the blockchain news.

# Find Blockchain news
Once a user selects a blockchain news from the home-page the Pymongo (API of mongoBD) find() method uses the object ID to find the requested blockchain news. The user is then taken through to the blockchain news's page where information from the database is presented in a readable format to the user.

# Delete Blockchain news
Each blockchain news has a 'Delete Blockchain news' button found at the bottom of the page. Once clicked it uses the remove() Pymongo (API of mongoBD) method.

# Logout page
Each blockchain news allow to add, edit or delete blockchain news on the website. This is an entirely blockchain news collection. Upon they complete, they can logout the site.

Technologies Used
Python 3.6
Google Fonts
Flask
CSS
HTML
Pymongo (API of ymongoBD)
 
### Simple Navigation & Ease of Use:
Add blockchain news – Add the best blockchain news, experienced and want to share
Logout – Friendly out upon finished 

### Information Architecture
Simple to make it fast login 

# Responsive Design
This is mobile responsive on PC, android and IOS & any mobile phone

### Image Presentation
Fast and sharp images

### Colour scheme and typography
Black and yellow to make it sleek and attractive 

# Features Left to Implement
•   Implement a machine learning model to recommend new blockchain news for a specific user
•   Implement blockchain news game to entire platform
•   Implement video blockchain news online
•   Implement “Live” cooking show on certain time


# Routes Testing 
This repo contains routes such as:
- Register ==> /register
- Login ==> /login
- Listings ==> /
- Article ==> /article/:id
- Add new ==> /add
- Edit ==> /edit/:id 

## Login page- Passed

https:// https://pythonassignment3.herokuapp.com/ -- Passed

## Mobile Responsive - Passed
Manually Testing on Desktop, Android , iOS  & others mobile devices - Passed

## Add (create) new articles- Passed 
Click add button, add the new title, add image link and content. Save the file & log out

## Delete articles- Passed 
Click the article and click delete button & logout 

## Edit news articles- Passed 
Click the article and edit test, edit new images and edit content. Save it and logout 


# Deployment
## Packages
## About Mongodb 
The package used is Pymongo which is the API of mongodb in python, and the database is hosted in Atlas Cluster for free.

## About Bcrypt & Create ID & password
To hash passwords, Bcrypt is used for this purpose.
The password should contain 6 characters at least, one special character and one number.

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
In particular, all details of the differences between the deployed version and the development version, if any, including:
Different values for environment variables (Heroku Config)
Different configuration files?
Separate git branch?

# Credits
Content search from google 
Media: www.medysif.com, www.whitehatsec.com, www.epfl.ch, www. deusm.com, www.swinburne.edu.au, www.simplilearn.com, https://storage2.ischool.syr.edu & squarespace-cdn.com, etc

# Acknowledgements
I received inspiration for this project from my company blockchain new division














