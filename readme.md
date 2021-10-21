## Gallery App 


## Author
### Langat Tito Kipkirui

## Description
This is a system that display pitcture of event , one can be able to search for a category of images and also it display images according to the location.

## User stories
As a user of the application I should be able to:

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## System Features
### Feature A: Image Model
Project contains an Image model with the following properties:

* Image
* Image Name.
* Image Description.
* Image Location Foreign Key.
* Image category Foreign Key.
* Remember to make migrations to your database when you change the properties of the model.

### Feature B: Location and Category models
Project contains location and category that link to the Image model.

### Feature C: Image Model methods
Image model contains the following methods:

* save_image() - Save an image to the database.
* delete_image() - Delete image from the database.
* update_image() - Update image in the database.
* get_image_by_id(id) - Allows us to get an image using its ID.
* search_image(category) - Allows us to search for an image using its category.
* filter_by_location(location) - Allows us to filter images by the location.

### Feature D: Location and Category models methods
implemention of the save, update and delete methods in both models and making sure you write tests for each method

### Feature E: Search Functionality
Project have a search form that when submitted calls a search function in the view function and redirects to a search results page.

### Feature F: Image Details
When a user clicks on an Image he/she should be redirected where a larger version of the image is displayed and should also see the details of the Image.

### Feature G: Copy Link
A user should be able to click a button and have the link to the image copied to the machine’s clipboard. Make sure you write a test for this functionality.

### Feature H: Admin Dashboard
Your project should have a dashboard that you will use to post photos to the database and manage the photos.

### Feature I: Deployment
project is deployed to Heroku 

## Setup and Installation instructions
To have a copy of this project, you can clone it from my github account using these steps;

Open your terminal (Ctrl+Alt+T)
git clone $ git clone https://github.com/Tito-74/Gallery-App.git
cd Gallery App 
code . or atom . based on your favorite text editor you have.

## Technologies Used
 * Python 
 * Django
 * CSS
 * javacript
 * HTML

## Further help
For any challenge using the App please don't hesitate to contact me through Email: kipkirui133@gmail.com or call me through 0714969204

<a href='https://github.com/Tito-74/Gallery-App/blob/master/license'>MIT license</a>