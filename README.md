# Love Lanarkshire

Welcome to Love Lanarkshire. 

<img src="development/ResponsiveMockup.png" height="520px" width="100%">

This is a web application that brings local communities together, allowing users to share their interests, hobbies and expertise with others in their local area. There is a robust relational database hosted with PostgresSQL. The site features a backend code devleoped with Python and the Django framework, that allows users to upload their events to the database and view a variety of event details, interact with specific events and filter and search through the database. The frontend was developed with HTML, CSS and JS and displays all events in a responsive, intuitive and coherent design. Registered users can perform CRUD operations on their own details or the events they have listed. Registered users have the ability to upgrade their membership of the site and this is facilitated by Stripe payments.
There is a secure user registration and authentication to the site. This allows for a more personalised experience.

View the deployed site [here](https://love-lanarkshire-ms4.herokuapp.com).

<img src="https://travis-ci.org/paperclippete/FinalMilestone.svg?branch=master">

| Contents  |
|-----------|
|[UX](#UX) |
|[Features](#Features)|
|[Testing](#Testing)|
|[Deployment](#Deployment)|
|[Credits](#Credits)|

### UX
___

#### Strategy

The site should...

* be visually appealing - using colours, styles and fonts which reflect the style and ethos of the brand
* provide quick access to the database of events
* enable the user to search for events by keywords
* enable the user to filter their search results
* enable users to change their details in the database
* enable users to change their membership status (posting privileges) by completing a one-time payment
* enable users to post/delete and edit events in the database
* enable users to like and join events

For the user the site should...

* be intuitive and easy to use
* be personalised and welcoming
* be responsive and accessible on a range of screens and devices
* provide quick access to events with a very simple search and filter function
* look appealing and in keeping with the brand
* ensure their data is secure
* allow them to manage their own events and user data
* allow them to keep their favourite(liked) events


##### User Stories

* As a bronze (free tier) user... 
    1. As a user, I want quick access to a variety of events based on my location
    2. As a user, I want quick access to a variety of events based on my interests
    3. As a user, I want quick access to a variety of events based on my age range
    4. As a user, I want to be able to book a place on an event
    5. As a user, I want to be able to save the events that I think I will like
    6. As a user, I want to see an overview of my upcoming booked classes
    7. As a user, I want to see the exact location of my event
    8. As a user, I want to be able to easily make changes to the data stored in my profile
* As silver/ gold (paid tier) user...
    1. As a user, I want to manage my membership, upgrading or changing it with ease and instant clarification of any changes
    2. As a user, I want to be able to post events providing event specific information that will appeal to the users who will enjoy my event most
    3. As a user, I want to be able to edit and delete events that I've posted
    4. As a user, I want to be able to upload specific event-related photographs that will help users find my event
    5. As a user, I do not want my event to be over-subscribed
    6. As a user, I want to know how many people to expect at my event

#### Scope

In order to create a good UX Love Lanarkshire should...

* be developed with a mobile-first approach in order to suit the widest possible audience
* be responsive in order to display correctly across a range of devices. A quick overview of [current browser stats](https://www.w3counter.com/globalstats.php) reveals that whilst Chrome is by far the most popular browser by far, the top 3 screen resolutions were 640x360, 1920x1080 and 1366x768 therefore it is essential to support a range of screens.
* be intuitive and provide feedback to the user on their actions
* feature a cohesive and distinctive design which promotes the Love Lanarkshire brand
* have a simple and easy to use search interface with filters
* enable users to instantly increase the functionality they receive with a one-time payment
* be functional to any user, whether logged in or not, but provide extra functionality and personalisation to registered users and differing membership levels

Please find my initial wireframe and database schema, created using Balsamiq, [here](development/LL-wireframes.pdf)


### Features
___

#### Existing Features

> Navigation Bar/ Dropdown Menu

Bootstrap 4 creates a minimalist navigation bar that toggles a dropdown menu on mobile/tablet devices. A user should not have to use the browser's back-button as the navigation bar is fixed, it will also fade to opaque when in use to increase the contrast of the text 

> Personalisation of Theme - FAB Button

A FAB button allows users to personalise their Love Lanarkshire experience. They can choose the colour theme of the site, setting their preference to local storage which will be remembered on their next visit.

> Main Search Box

For ease of use and in line with good UX design, there is a minimal search interface on the index page.

> Filter Accordion on Search Results

As some users may not be sure what they are looking for immediately and may like to initially browse the database, having extra filters on the search results page would prevent users from having to navigate back to the search box. 

> Bootstrap 4 grid layout and cards

Bootstrap styling ensures that the search results page would remain as responsive as possible. Using the card format ensures that key information is displayed in a way that is quick to see for the user. Each event can then be viewed for more information.

> Django Easy Maps and Google Maps API

Using a plugin called Django Easy Maps Love Lanarkshire will populate and display the correct location for each event in a Google Map. 

> User Register and Login with Password Reset Function using Django Authentication

Users can register and login to Love Lanarkshire with their password being encrypted when it is entered into the database. If a user forgets their password they can reset it through a personalised email link.

> User Profile Page

This is essentially a user dashboard that houses all of the most crucial user functionality for the Love Lanarkshire website. It is personalised to the user and allows them to update their details, upgrade their membership to the site, view their upcoming events, view their event history, view events they have liked and, dependant on their membership, allow them to post new events.

> Stripe Payments for Membership Upgrade

Using the Stripe API and plugin means that users can have confidence in submitting their payment details to Love Lanarkshire. It also means that Stripe will handle all verification and encryption of user payment details ensuring that Love Lanarkshire can keep their user details safe.


#### Features for the Future

> Pagination

Pagination on the search results will be essential as the database grows.

> Automation

Automation of some services would improve functionality as the user base increases - emails could alert event hosts when users book their event, emails could be sent to remind users of an upcoming event for which they are booked.

> Terms and Conditions

There would need to be a robust terms agreement for using the website - this would protect users against fraud and ensure the site is safe and secure for everyone.

> Post Event Form Location

Using current location or allowing hosts to choose their event location on a map may increase ease of use.

> Ratings

Creating a ratings system would improve accountability for hosts and users ensuring that Love Lanarkshire retains its community ethos.


### Technologies Used

##### Languages

* **HTML** - used for creating content and basic layout and validated with W3C
* **CSS** - used for customised styling and layout and validated with W3C
* **JavaScript** - used to provide interactivity and logic to the site
* [Python](https://www.python.org/) - used to programme the site and interact between the database and the frontend


##### Frameworks

* [Django](https://www.djangoproject.com/) - A Python framework
* [Bootstrap](https://getbootstrap.com/) - used for responsive layout, basic styling, dropdown Navbar (JavaScript for these features was used - linked to Bootstrap and, through BS, popper.js in <script> tags)

##### Tools

* [PyMongo](https://api.mongodb.com/python/current/) - An API which provides tools for working with MongoDB in Python
* [MongoDB](https://www.mongodb.com/) - non-relational document style database used to store the recipes and users for Dessert Search
* [WTForms](https://wtforms.readthedocs.io/en/stable/) - An API which provides form classes for ease of managing form data in Python
* [CSS Minifier](https://cssminifier.com/) - used to minify my CSS data for deployment
* [Favicon Generator](https://www.favicon.cc/?) - I used this to generate a Favicon
* [W3C Validator](https://validator.w3.org/) - HTML Validator 
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validator
* [PyCodeStyle](https://pypi.org/project/pycodestyle/) - Python Validator
* [JSLint](https://www.jslint.com/) - JS Validator
* [Cloud9 IDE](https://ide.c9.io/) - this was the IDE where I developed and tested my application
* **Git** - I pushed my files using **Git**, storing them in a repository on **GitHub**
* [Heroku](https://heroku.com/) - I deployed my finished site through Heroku
* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/) - used to test and check my work throughout the development process

##### Libraries

* [jQuery](https://jquery.com/) - JavaScript library used to connect with APIs and custom-code for the site which allows for DOM manipulation
* [Google Fonts](https://fonts.google.com/) - used for customised fonts
* [Font Awesome](https://fontawesome.com/) - used for links and icons to make the site more appealing


### Testing
___

#### Manual and Automated Testing

Manual testing was done for all CRUD operations from the database as well as for all links, buttons and forms in the site. I used Werkzeug Debugger throughout the development process to immediately flag errors when running my app.py file.

I created a [test.py](development/testing/testdb.py) file that tested the connection to my database, ensuring data was inserted in a suitable manner and was returned to the console when requested.

Throughout the process I continually manually tested the frontend, by saving my work in the IDE and running it in Google Chrome. I used Chrome Developer Tools to ensure that my site was responsive and functioned in all screen sizes and that my styling was applied appropriately throughout. 

I set ```console.logs``` and ```debugger``` statements throughout my js files in order to debug through the console.

I used jQuery to manipulate the DOM in Chrome Developer Tools in order to test my code visually before writing it within the script.

I had several users log in and out of the website searching, adding, editing and deleting (CRUD) the recipes. This was to ensure that only registered users were able to delete/edit their own recipes. It also verified that the correct author showed up for each recipe. 

#### Responsiveness

I tested my project throughout development using Chrome Developer Tools to check the site was responsive. I continually made adjustments to my media-queries in CSS to ensure it looked good at all screen-widths, however I realised my laptop had a different screen size to the standard. I began to investigate a range of screen sizes and realised the best option was just to make it as responsive as I possibly could!

#### Bugs

There were several issues with my Python code, however, using the Werkzeug Debugger allowed for an immediate fix. I used the documentation for Flask, PyMongo and MongoDB to help solve any problems. I found it very difficult to get a search function that would search text and use checkboxes. I eventually had code that would work in every instance although I am aware that it could be neater.

There was a 500 error displaying in the console when Fetch was trying to retrieve login details from an anonymous user. I've run out of time on my project to fix this issue but I'd look into an if statement in the fetch function or in python to catch this.

There was a 400 error in the console for the favicon. I created a favicon.

There is a known issue with the 'back' button on the view recipe pages, as they return to the main search page in this instance they require form resubmission. I have looked into this in various developer support resources but have yet to find a fix. Essentially I want to go back and refresh the page automatically for the user, just like using the browser back button. When a user liked a recipe and then clicked the back button it took them back to view recipe with an active like recipe button again. I fixed this by searching the current url for 'like_recipe', if it was located the back button would go back by 2 pages.
*I have decided to send the user back to Search Results temporarily, as I feel the user's experience would be blighted by an ERR_CACHE_MISS page and the alternative of having to reset the filters or pressing the browser's back button would provide a less negative experience for the user. I then had to create a back to user home button*

There is an issue with the recipe description and method not rendering correctly, they render as input in the terminal when printed but do not when rendered in the HTML template, I have attempted to fix this but there are sometimes two full stops at the end of the text. I am continuing to look for a fix.

There is also an issue with duplicate ingredients not showing up, this is because I currently have each ingredient set as a key in the database and therefore can't have duplicates. I will continue to look into this.

There have been several issues throughout development with my JS code breaking, I worked hard using console.logs and debuggers to pinpoint errors and fix them. There shouldn't be any errors displaying in the console except for the above 500 error, intermittently.

There was a security issue related to the app.py view where the database string was returned in the URL. This could enable people to find and access the dtabase. I quickly fixed the URL parameter to be the user._id rather than users._id.

### Deployment
___

#### How to Install Dessert Finder

1. From your terminal enter `git clone https://github.com/paperclippete/Milestone3.git` to clone the project and download to your IDE

2. Set up your Virtual Environment Variables 
    * this can be done by creating folder named .venv to hold your variables and importing them into your app.py
    * this can be done in your IDE bash terminal - e.g. cd .. to your root directory and type `nano.bashrc` and type in your important environment variables
    
    * Your environment variables should not be committed to git*


3. You should now install the requirements by typing `$ sudo pip3 -r install requirements.txt`

4. You will also have to create your own database to get full functionality from the project. [MongoDB](https://www.mongodb.com/) is free and easy to use. 

> Within my Database I had two collections, recipes and users

``` 
    recipes
    {
    _id: ObjectId("5cfd48d8b93f0ccb1dcbe754")
    ingredients: Object
        key: "value"
    dairy_free: bool
    gluten_free: bool
    main_ingredient: "string"
    recipe_description: "string"
    title: "string"
    image: "string"
    method: "string"
    author: "string"
    vegan: bool
    prep_time: "string"
    serves: "string"
    like_count: Int
    likes: Array
        0: ObjectId("5cfd48d8b93f0ccb1dcbe754")
    }
    
    users
    { 
    id: ObjectId("5cfd4210b93f0ccb1dcbe74f")
    last_name: "string"
    first_name: "string"
    password: "string" (hashed)
    username: "string"
    }
```    

#### How to Deploy your Site

I committed my code to GitHub at regular intervals. I am now using git more often, making sure to give detailed commit messages as I know it provides version control.

1. In order to deploy the site to Heroku, you must create a Procfile and requirements.txt. *These will tell Heroku how to run your app.*
    * To create a Procfile - `echo web: python (your filename).py > Procfile ` 
    * To create a requirements.txt - `sudo pip3 freeze --local > requirements.txt ` 

2. Next, log into Heroku and set up the remote.
    ``` 
    
 
    heroku login  
    
    git remote add heroku(url) 


    ``` 

3. You then need to setup your Heroku Enivronment Variables and you can do this in two ways, either through the terminal or by navigating to [Heroku](http://heroku.com).

4. On navigating to the Heroku website, log in and select your app from the dashoboard.

5. Choose settings and click on 'Reveal Config Vars' and insert the environment variables that are essential for your project to run. For example, 

    > IP - 0.0.0.0 
    PORT - 8080 
    MONGO_URI - mongodb+srv://root*your password*@myfirstcluster-ug8tc.mongodb.net/*your database*?retryWrites=true 
    DB_NAME - *your database name*
    SECRET KEY - *create a secret key*
    
    * You should never reveal any of these environment variables to ensure you maintain the security of your database *

6. You should then send your committed code to Heroku using `git push heroku master` and view your deployed site on the URL provided within your Heroku dashboard.

#### Differences between Development and Deployed version

The difference between the deployed version and the development version is that I'm using a minified CSS file whereas I used SASS to compile my styling during development. I also set the debug to false for deployment.

### Credits
___

#### Content
The recipes and recipe images were inserted for testing purposes were taken from the [BBC website](https://www.bbc.co.uk/food).

The background image was from [Pexels](https://www.pexels.com/search/website%20background%20food/), the video was from [Videvo](https://www.videvo.net/). The cake images and icons were from [FlatIcon](https://www.flaticon.com/).

**This site has been created for educational purposes only**

#### Media
The images and text were sourced from the sites listed above. All images have been used for educational purposes only.

#### Acknowledgements

I used Ian Lunn's [Hover](https://ianlunn.github.io/Hover/) for my navbar link hover effects. I have clearly marked the borrowed code in my CSS.

I used [W3Schools](https://www.w3schools.com/) code as a basis for my custom checkboxes.

Throughout this project I have sought support and guidance from [Stack-Overflow](https://stackoverflow.com/), Code-Institue [Slack](https://slack.com/intl/en-gb/) Community, [W3Schools](https://www.w3schools.com/), [CSS Tricks](https://css-tricks.com/), [Pretty Printed](https://prettyprinted.com/) YouTube videos.