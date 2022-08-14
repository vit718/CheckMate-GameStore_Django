# CheckMate GameStore

Welcome to my fifth milestone project, an e-commerce website that focuses on selling board games. CheckMate is a fictional store that relies on online sales alone to make revenue.
This project uses the Django framework, HTML, Python, CSS and JavaScript.

In this project, I set up an authentication system and provided access to the site's data for users to purchase various products.

CRUD functionality (Create, Read, Update, Delete) is implemented in the Reviews page, Products Management page, Cart page and the Admin section of the project.

A live website can be found [here](https://marcellomuy-checkmate.herokuapp.com/).

![website preview](/readme_files/website-preview.png)

## Table of Contents

* [1 UX](#1-ux)
  * [Colour Scheme and Font](#colour-scheme-and-font)
  * [Wireframes](#wireframes)
  * [Project Management](#project-management)
  * [User Stories](#user-stories)
* [2 Data Models](#2-data-models)
  * [Models ERD](#models-erd)
* [3 Features](#3-features)
  * [All Pages](#all-pages)
  * [Navbar](#Navbar)
  * [Footer](#Footer)
  * [Home Page Features](#home-page-features)
  * [Contact Us Page](#contact-us-page)
  * [All Products Page](#all-product-page)
  * [Product Detail Page](#poduct-details-page)
  * [On Sale Page](#on-sale-page)
  * [Reviews Page Features](#reviews-page-features)
  * [Product Managemnet Page](#product-management-page)
  * [Shopping Cart Page](#shopping-cart-page)
  * [Checkout Page Features](#checkout-page-features)
  * [Sign in/out Page](#sign-in/out-page)
* [4 Technologies Used](#4-technologies-used)
* [5 Testing](#5-testing)
  * [Validation](#validation)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)
* [6 Search Engine Optimisation](#6-search-engine-optimisation)
* [7 Marketing](#7-marketing)
* [8 Deployment](#8-deployment)
* [9 Credits](#9-credits)

## 1 UX

[Go to the top](#table-of-contents)

Having a website where users can visualize products and make purchases is the backbone of any eCommerce application.

As a big fan of board games, I have always looked online when wanting to buy a new board game.

This website will showcase a selection of games for the user to buy with a easy-to-use UI.

### Colour Scheme and Font

[Go to the top](#table-of-contents)

Please find colour scheme used for this project [here](https://coolors.co/002f33-5da3a6-e6f4f1).

The [Roboto flex](https://fonts.google.com/specimen/Roboto+Flex?query=roboto+flex) was used as the website font across all pages.

The website logo was created using [Canva](https://www.canva.com/) designing tools.

![Logo](/media/logo.png)

### Wireframes

[Go to the top](#table-of-contents)

Mobile and Desktop wireframes were created for some pages of the website.

Due to lack of time, some features fell outside the scope of this project, and wireframes and final project might look different.

#### Home Page

[Go to the top](#table-of-contents)

![Home](/readme_files/wireframes/wireframe-home.png)

#### Products Page

[Go to the top](#table-of-contents)

![Products](/readme_files/wireframes/wireframe-products.png)

#### Product Details

[Go to the top](#table-of-contents)

![Detail](/readme_files/wireframes/wireframe-product-details.png)

#### Shopping Cart

[Go to the top](#table-of-contents)

![Cart](/readme_files/wireframes/wireframe-cart.png)

#### Checkout Page

[Go to the top](#table-of-contents)

![Checkout](/readme_files/wireframes/wireframe-checkout.png)

#### Reviews Page

[Go to the top](#table-of-contents)

![Reviews](/readme_files/wireframes/wireframe-reviews.png)

### Project Management

[Go to the top](#table-of-contents)

A Kanban board was created on GitHub and was used as a project management tool.
User stories are divided into 6 EPIC labels.

### User Stories

[Go to the top](#table-of-contents)

All 29 user stories were implemented.

* Viewing the webpage

![Viewing](/readme_files/user-stories/user-story-viewing-the-webpage.png)

* Filtering and searching

![Viewing](/readme_files/user-stories/user-story-filtering-and-searching.png)

* Buying a product

![Viewing](/readme_files/user-stories/user-story-buying-product.png)

* Registration / Accounts

![Viewing](/readme_files/user-stories/user-story-registration-and-account.png)

* Admin and store management

![Viewing](/readme_files/user-stories/user-story-admin.png)

* Interacting and engaging

![Interacting](/readme_files/user-stories/user-story-interacting.png)

## 2 Data Models

[Go to the top](#table-of-contents)

Data models used in this project:

* Contact app

```python
class ContactMessage(models.Model):
    """Class for contact us model"""
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" + self.email
```

* Products app

```python
class Product(models.Model):
    """
    A model for storing Product information
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    min_players = models.PositiveSmallIntegerField(null=True, blank=True)
    max_players = models.PositiveSmallIntegerField(null=True, blank=True)
    min_age = models.PositiveSmallIntegerField(null=True, blank=True)
    avgRating = models.FloatField(default=0,)
    play_time = models.PositiveSmallIntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    onSale = models.BooleanField(default=False)

    def price_onsale(self):
        return self.price - ((self.price * 50) / 100)

    def __str__(self):
        return self.name
```

* Reviews app

```python
class Review(models.Model):
    """A model for user reviews"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
```

* Newsletter app

```python
class Subscriber(models.Model):
    """Model for subscriber email information"""

    email = models.EmailField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
```

The following apps have their data models based on the Boutique Ado project.

* bag app
* checkout app
* profiles app

### Models ERD

This diagram was automatic generated using django_extensions and Graphviz:

[Click here](/readme_files/models-diagram.png) to open the diagram.

## 3 Features

### All pages
  
  [Go to the top](#table-of-contents)

  All links throughout the website pages will be highlighted in a darker tone when hovered.

  Action buttons like "SHOP NOW", "PROCEED TO CHECKOUT" AND "ADD TO CART" have a dark green background colour and display the HTML text in white when hovered.

  Go back buttons like "CANCEL" and "KEEP SHOPPING" have the background colour white with a dark green text and border. Its background colour will change to dark green and text into white when hovered.

  ![Buttons](/readme_files/features/all_pages/features-buttons.png)

  An alert will appear at the top right of the page every time the user interacts with the webpage.

  ![Alert-success](/readme_files/features/all_pages/features-alerts-success.png)
  ![Alert-success2](/readme_files/features/all_pages/features-alerts-success2.png)
  ![Alert-error](/readme_files/features/all_pages/features-alerts-error.png)

### Navbar
  
  [Go to the top](#table-of-contents)

* Desktop

  On the left, The navigation bar contains the site logo and a link to the home page.

  A search bar is located in the center of the navbar.

  On the right, the "My Account" icon displays a dropdown when clicked on with links to product management, sign in, and sign out pages.

  Also on the right is a shopping cart icon that works as a link to the shopping cart page and displays the current total amount in the cart.
  
  * Under the search bar there are 5 links:

    * (Home), a link to the "home" page

    * (All products), a link to the "all products" page.

    * (Board games), dropdown with options for game categories (Family, Strategy, Party, Classic) and "all board games".

    * (Role-Playing), dropdown with options for (dungeons & dragons and pathfinder) and "all role-playing" games.

    * (On sale), a link to the "on sale" page.

    ![Navbar](/readme_files/features/navbar/features-navbar.png)

  * Mobile
  
    The logo is removed on the mobile version, and a hamburger icon is placed at the left of the navbar.

    When the hamburguer icon is clicked on, a dropdown menu shows all the navigation links.

    The search bar is also hidden in the mobile version and is only displayed when the user clicks on the search icon.

    ![Navbar-mobile](/readme_files/features/navbar/features-navbar-mobile.png)
    ![Navbar-mobile](/readme_files/features/navbar/features-navbar-mobile-dropdown.png)
    ![Navbar-mobile](/readme_files/features/navbar/features-navbar-mobile-search.png)

### Footer
  
* Desktop and mobile

    On the left side of the footer, you will find a link to the privacy policy page and just under it, a link to the "contact us" page.

    On the right side of the footer, you will find a social link icon that directs the user to the CheckMate Facebook business account.

    The content of the footer is in a smaller font size in the mobile version.

    ![Footer](/readme_files/features/footer/features-footer.png)
    ![Footer](/readme_files/features/footer/features-footer-mobile.png)

### Home page

  The home page has a background image and a bootstrap carousel with three carousel items.
  
  The carousel will slide indefinitely every 20 seconds but will stop when hovered.

  The user can control the carousel by clicking on the white arrows of the carousel or at the white lines under it.

  Each line represents one of the carousel items and is highlighted when the correspondent carousel is displayed.

* First item:

    In the first carousel item, you will find the main page headings.

    Under the headings, a "SHOP NOW" button, when clicked on, directs the user to the "all products" page.

    A slide effect was added to the headings and the button, making them appear in sequence after each other.

    ![Home-carousel-1](/readme_files/features/home/features-home-carousel-1.png)

  * Second item:

    In the second carousel item, a flash sale image directs the user to the "on sale" page when clicked on.

    ![Home-carousel-2](/readme_files/features/home/features-home-carousel-2.png)

  * Third item:

    In the third carousel item, there is the form for subscribing to the newsletter with a subscribe button below.

    The user has to type an email address and check a confirmation box.

    The form will only be submitted after checking the box.

    Under the form, there is a link highlighted in red. When clicked on, it directs the user to the unsubscribing page.

    ![Home-carousel-3](/readme_files/features/home/features-home-carousel-3.png)

    ![Unsubscribe](/readme_files/features/home/features-unsubscribe.png)

### Contact Us page

  The Contact page has a white background, four input fields and a submit button.
  
  All fields are required fields.

  ![Contact-us](/readme_files/features/contact/features-contact.png)

### All Products Page

  The products page can be filtered by category by clicking on the navigation links in the navbar.

  If a category is selected, a badge with the category name is displayed below the product heading.

![Products-category](/readme_files/features/products/features-all-products-category.png)

  At the top left of the page, you will see the total number of products, and at the top right, you can sort products by price or alphabetically.

  The number of products per row will differ depending on the screen size.

  The Product name and image will redirect the user to the product details page when clicked.

  Beside the image or below it, if displayed on an extra small screen, you will find the product card.
  
  At the top of the card, you will find the product's name.

  Under the name are icons with information regarding the minimum age, min and max number of players, and the average time to play.
  
  If the product is on sale, the price is displayed in red with the old price crossed and faded.
  
  ![Products-price-red](/readme_files/features/products/features-all-products-price-red.png)

  An "ADD TO CART" button is placed at the bottom of the card and, when clicked on, will add one item to the cart.
  
  At the bottom right, there is an arrow-up icon that brings the user back to the top of the page when clicked. The arrow has an absolute position and is always visible.
  
  Large:

  ![Products-large](/readme_files/features/products/features-all-products-l.png)

  Medium:

  ![Products-medium](/readme_files/features/products/features-all-products-m.png)

  Small:

  ![Products-small](/readme_files/features/products/features-all-products-s.png)

  Extra Small:

  ![Products-extra-small](/readme_files/features/products/features-all-products-xs.png)

### Products Details page

[Go to the top](#table-of-contents)

  On the products details page, there is a large product image.
  
  The product card has all the product information shown on the "all products" page plus four more items:

![Product-details](/readme_files/features/product_details/features-product-details.png)

* Reviews:

    A yellow star icon is located beside the average rating for the product.

    If the product has no reviews, a "no reviews" text is displayed instead

    A reviews link can be found beside the average rating and redirects the user to the reviews page when clicked.

![Product-details-reviews](/readme_files/features/product_details/features-product-details-reviews.png)

* Description:
  
    It contains a description of the product.

* Edit and delete:

    If the user is a superuser, an "edit" and "delete" button is displayed under the quantity field.

    The edit button redirects to a pre-populated product management page, and the "delete" button redirects to the "confirm delete" page.

    ![Product-management-populated](/readme_files/features/product_details/features-management-populated.png)

    ![Product-details-delete-page](/readme_files/features/product_details/features-product-details-delete-page.png)

* Quantity:
  
    On this page, the user can select the quantity to be added to the shopping cart.

  ![Product-details-edit-delete](/readme_files/features/product_details/features-product-details-edit-delete.png)

### On Sale page

[Go to the top](#table-of-contents)

  The On sale page will display all the products that are marked as "on sale".
  
  Products can be marked as on sale through the "product management" page or the "admin" page.

  ![Product-on-sale](/readme_files/features/on_sale/features-on-sale-page.png)

### Reviews page

[Go to the top](#table-of-contents)

  A container with the reviews is displayed on the "product reviews" page if the products have any reviews.

  If the user is the author of the review, links for edit and delete are displayed otherwise, these links are hidden.

  ![Product-reviews](/readme_files/features/reviews/features-product-reviews-page.png)

  The "edit" button will load a pre-populated form.

  ![Product-reviews-edit](/readme_files/features/reviews/features-reviews-edit.png)

  The "delete" button will load a delete confirmation page.

  ![Product-reviews-delete](/readme_files/features/reviews/features-reviews-delete.png)

  The "LEAVE A REVIEW" button will redirect the user to the "Add a Review" page, where a form with fields for comment and rating is displayed.

  ![Product-reviews-add](/readme_files/features/reviews/features-reviews-add.png)

  When submitted, the form will redirect the user back to the reviews page.

### Product management page

[Go to the top](#table-of-contents)

  A "super user" can add new products on the product management page.

  ![management-page](/readme_files/features/management/features-management.png)

### Shopping Cart page

[Go to the top](#table-of-contents)

  On the shopping cart page, the user can visualize all products inside the cart, update the quantity and delete the product entirely from it.

  ![Shopping-cart-page](/readme_files/features/shopping_cart/features-cart.png)

  When the cart is empty this page will load.
  
  ![Shopping-cart-empty](/readme_files/features/shopping_cart/features-cart-empty.png)

  At the bottom of the page, you will find the total price and delivery fee to be paid.
  
  The delivery fee is 10% of the subtotal price.

  When spending more than 50 euros, the delivery fee is free.
  
  ![Shopping-cart-price](/readme_files/features/shopping_cart/features-cart-price.png)

### Checkout page

[Go to the top](#table-of-contents)

  On the checkout page, there is a form for the payment information.

  The order summary is shown on the right side of the page.

  ![Checkout-page](/readme_files/features/checkout/features-checkout.png)

  Clicking the complete order button will create the order, complete the payment transaction and load the "checkout_success" page.
  
  An email is sent to the registerer email confirming the purchase.
  
  Clicking the button at the bottom of the page will redirect the user to the "on sale" page.

  ![Checkout-page-success](/readme_files/features/checkout/features-checkout-success.png)

  ![Checkout-page-email](/readme_files/features/checkout/features-checkout-email.png)

### Authentication

[Go to the top](#table-of-contents)

  The user can register for an account.
  
  ![Register](/readme_files/features/authentication/features-register.png)

  Sign in and Sign out.

  ![Sign-in](/readme_files/features/authentication/features-sign-in.png)
  ![Sign-out](/readme_files/features/authentication/features-sign-out.png)

### 404 page

[Go to the top](#table-of-contents)

A 404 page is loaded if the page is not found.

"GO BACK" button redirects the user to the home page.

![404-page](/readme_files/features/features-404.png)

## 4 Technologies Used

[Go to the top](#table-of-contents)

* [HTML5](https://en.wikipedia.org/wiki/HTML)
  The project uses HyperText Markup Language.
* [CSS3](https://en.wikipedia.org/wiki/CSS)
  The project uses Cascading Style Sheets.
* [Django 3.2](https://en.wikipedia.org/wiki/Django_(web_framework))
  Django was used as the web framework to develop this project.
  Below you can find the Django libraries and packages used in this project.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
  Library used for authentication and registration
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  The project uses JavaScript.
* [Python 3](https://en.wikipedia.org/wiki/Python_(programming_language))
  The project uses Python.
* [Boostrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
  The project uses Bootstrap 4.6.
* [PostgreSQL](https://www.postgresql.org/)
  The project uses PostgreSQL as a database.
* [Gitpod](https://www.gitpod.io/)
  The project uses Gitpod.
* [Chrome Developer tools](https://www.google.com/intl/en_uk/chrome/)
  Chrome was used to debug and test the project's source code.
* [Balsamiq](https://balsamiq.com/)
  Balsamiq was used to create the wireframes during the design process.
* [Canva](https://en.wikipedia.org/wiki/Canva)
  Canva was used to create the website logo and the flash sale image.
* [Google Fonts](https://fonts.google.com/)
  Google fonts were used to import the "Roboto flex" font into the style.css file which is used on all pages throughout the project.
* [Heroku](https://en.wikipedia.org/wiki/Heroku)
  Heroku was useed as a cloud platform service for this project.
* [AWS](https://aws.amazon.com/)
  Used to store the stactic and media files of this project.
* [Stripe](https://stripe.com/ie)
  Payments are processed using Stripe.
* [GitHub](https://github.com/)
  GitHub was used to store the project's code after being pushed from Git.

## 5 Testing

### Validation

[Go to the top](#table-of-contents)

#### HTML

[Go to the top](#table-of-contents)

To validate the HTML code, I clicked on "view page source" on the deployed application page that I wanted to inspect and copied the source code into the W3C validator.

* Home page

    The validator found seven errors in the home page HTML code:
  
  * Error:

    ![Home-error-1](/readme_files/validation/home/validation-home-page-error-1.png)
    * Fix - Inserted list items of mobile navbar inside a ul element.
  
  * Error:

    ![Home-error-2](/readme_files/validation/home/validation-index-page-error-2.png)
    * Fix - Gave a unique id for "a" tag in the mobile header.
  
  * Error:

    ![Home-error-3](/readme_files/validation/home/validation-index-page-error-3.png)
    * Fix - Correct "href" path of "my profile" link in the mobile version of the navbar.
    * Fix - Removed Unused id from the carousel div.
    * Fix - Removed duplicated class from newsletter input element.
    * Fix - Removed type attribute from script tags.

  * All validation errors were fixed.

    ![Home-fixed](/readme_files/validation/home/validation-index-page-no-errors.png)

* Products page

    The validator found four errors in the products page HTML code:

  * Error:

    ![Products-error-1](/readme_files/validation/products/validation-products-page-error-1.png)
    ![Products-error-2](/readme_files/validation/products/validation-products-page-error-2.png)
    ![Products-error-3](/readme_files/validation/products/validation-products-page-error-3.png)
    * Fix - Removed "min" and "max" atributes from input element.
    * Fix - Removed type attribute from script tags.

  * All validation errors were fixed.

    ![Products-fixed](/readme_files/validation/products/validation-products-page-no-errors.png)

* On Sale page

  The validator found four errors in the On Sale page HTML code:

  Two errors for the "min" and "max" attribute of the "input" element and two errors for the unnecessary "type" attribute in the script tags.

  All validation errors were fixed.

    ![On-sale-fixed](/readme_files/validation/products/validation-on-sale-page-no-errors.png)

* Product details page

  The validator found one error in the product details page HTML code:
  
  The unnecessary "type" attribute was removed from the script tag.

  All validation errors were fixed.

    ![Product-details-fixed](/readme_files/validation/products/validation-product-details-page-no-errors.png)

* Product reviews page

  The validator found four errors in the product reviews page HTML code.
  When the product had no reviews, the following error was found:

    ![Product-reviews-no-reviews](/readme_files/validation/reviews/validation-reviews-no-reviews-page-error1.png)

  When trying to leave a new review, the following error was found:
  
    ![Product-add-new-review](/readme_files/validation/reviews/validation-reviews-add-new-review-page-error1.png)

  When trying to edit a review, the following error was found:

    ![Product-edit-review-page](/readme_files/validation/reviews/validation-reviews-edit-review-page-error1.png)

  When deleting a review, the folowing error was found:

    ![Product-delete-review](/readme_files/validation/reviews/validation-reviews-page-delete-error.png)

  All validation errors were fixed.

* Contact us page

  The validator found Two errors in the contact us page HTML code.
  
  * Error:

    ![Contact-us-page-error](/readme_files/validation/contact/validation-contact-us-error.png)

    * Fix - Removed duplicated class attribute.
    * Fix - Removed stray "div" tag.

  All validation errors were fixed.

    ![Contact-us-page-no-errors](/readme_files/validation/contact/validation-contact-us-no-errors.png)

* Unsubscribe page

  The validator found Two errors in the contact us page HTML code.

  * Error:

    ![Unsubscribe-page-error](/readme_files/validation/home/validation-unsubscribe-error.png)

    * Fix - Removed unclosed "div".

  All validation errors were fixed.

    ![Unsubscribe-page-no-errors](/readme_files/validation/home/validation-unsubscribe-no-errors.png)

* Product Management page

    The validator found no errors across the product managements templates HTML code.

  * Product management adding a product:

    ![Product-management-add-no-error](/readme_files/validation/product_management/validation-product-management-add-no-errors.png)
  
  * Product management deleting a product:

    ![Product-management-delete-no-error](/readme_files/validation/product_management/validation-product-management-delete-no-errors.png)

  * Product management editing a product:

    ![Product-management-edit-no-error](/readme_files/validation/product_management/validation-product-management-edit-no-errors.png)

* My Profile page

  The validator found Two errors in the My profile page HTML code.  

  * Errors:

    ![My-profile-errors](/readme_files/validation/profile/validation-profile-errors.png)
  
    * Fix - Added closing "div" tag.

  All validation errors were fixed.

    ![My-profile-no-errors](/readme_files/validation/profile/validation-profile-no-errors.png)

* Allauth templates

  The validator found no errors in the "login" and "logout" templates.

* Shopping cart page

  The validator found no errors in the shopping cart  HTML code.

    ![Shoooing-cart-no-errors](/readme_files/validation/shopping_cart/validation-shopping-cart-no-errors.png)

* Checkout page

  The validator found 4 errors in the checkout page HTML code.

  * Error:

    ![checkout-errors](/readme_files/validation/checkout/validation-checkout-errors.png)

    * Fix - Use "div" elements instead "td" elements.
    * Fix - Use "div" element instead "h1" and added "h1" bootstrap class to keep the heading style.
    * Fix - Removed "for" attribute from the label.

  All validation errors were fixed.

    ![checkout-no-errors](/readme_files/validation/checkout/validation-checkout-no-errors.png)

  The validator found no errors in the checkout success page.

    ![checkout-no-errors](/readme_files/validation/checkout/validation-checkout-success-no-errors.png)

#### CSS

[Go to the top](#table-of-contents)

  CSS code was validated using W3C CSS validator.

 The validator found no errors in all 3 css files:

* base.css
* profile.css
* checkout.css

  ![css-no-errors](/readme_files/validation/css/validation-css-no-errors.png)

#### JavaScript

[Go to the top](#table-of-contents)

  All JavaScript code was validate using jshint.
  
  All code was copied into the validator and
  three lines of code were added at the top of the page to ignore some warnings.
  
* /*jshint esversion: 6*/
  
* /*globals $:false*/
  
* /*globals Stripe:false*/

  * Tested pages:

    * bag.html

    * stripe_elements.js

    * carousel_script.html

    * products.html

    * on_sale.html

    * countryfields.js

  The validator found six errors.

    ![js-errors](/readme_files/validation/js/validation-js-all-errors.png)

  All errors were fixed.

    ![js-no-errors](/readme_files/validation/js/validation-js-no-errors.png)

#### Python

[Go to the top](#table-of-contents)

  The Python code was checked using the command "python3 -m flake8" in Gitpod.

  The validator showed multiple errors.

The following errors were fixed in all files:

* W293 blank line contains whitespace
* E302 expected 2 blank lines, found 1
* W291 trailing whitespace

The following error was fixed in all files except "autogenerated files", "settings.py" and "webhook_handler.py" where this error occurred in essential parts of the code and I chose not to change it.

* E501 line too long (more than 79 characters)

The following error was fixed by adding the unused variable to the Try block.

* local variable 'grand_total' is assigned to but never used

Autogenerated files were not validated.

### Manual Testing

[Go to the top](#table-of-contents)

* All pages

    TEST            | OUTCOME                          | PASS / FAIL  
    --------------- | -------------------------------- | ---------------
    Buttons and Links | All buttons and Links are styled consistently throughout the website. | PASS
    Alerts | Alerts are displayed consistently after every user interaction throughout the website. | PASS
    Responsiveness | All pages are responsive to different screen sizes. | PASS

* Navbar

    TEST            | OUTCOME                          | PASS / FAIL  
    --------------- | -------------------------------- | ---------------
    Logo | Redirects the user to the home page when clicked on. | PASS
    Search Bar | Display a list of products containing the searched words either in the product title or the product description. | PASS
    My Account Link | Show a dropdown when clicked on containing a link to the "Register" page and "Sign in" page. When the user is logged on displays a link to the "Product Management" page, "My Profile" page and "Sign out" page. All links redirect the user to the correct page. | PASS
    Shopping Cart | Displays the total value of all items currently in the cart, when clicked on, redirects the user to the "Shopping Cart" page. | PASS
    Navigation Links | When clicked on, it displays the correctly dropdown menu and all links redirect the user to the correct products page. | PASS

* Footer

    TEST            | OUTCOME                          | PASS / FAIL  
    --------------- | -------------------------------- | ---------------
    Social Link | When clicked, it opens a new page with the CheckMate Facebook business account. | PASS
    Privacy Policy | When clicked, it opens a new page with the Privacy Policy for CheckMate Game Store. | PASS
    Contact Us | When clicked, it redirects the user to the "contact us" page. | PASS

* Home page

    TEST            | OUTCOME                          | PASS / FAIL  
    --------------- | -------------------------------- | ---------------
    Carousel | The Carousel controls work as expected. | PASS
    SHOP NOW button | The "SHOP NOW" button redirects the user to the "all products" page. | PASS
    On sale image | When clicked, the "on sale" image redirects the user to the "on sale" page. | PASS
    Newsletter form | Subscribe form only accepts a valid email address. | PASS
    Newsletter check box | The form is submitted only if the check box is checked. | PASS
    SUBSCRIBE button | The "SUBSCRIBE" button submits the form. | PASS
    Newsletter database | The user email is added to the database. | PASS
    Newsletter confirmation email | A confirmation email is sent when a new email is added to the database. | PASS
    Unsubscribe | The link to the unsubscribe page redirects the user to the right page. | PASS

* Unsubscribe page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Cancel button | Redirects the user back to the home page. | PASS
  Unsubscribe button | Submits the form and user back to the home page. | PASS
  Unsubscribe form | Unsubscribe form only accepts a valid email address. | PASS
  Unsubscribe check box | The form is submitted only if the check box is checked. | PASS
  Unsubscribe database | The user email is deleted from the database. | PASS
  Unsubscribe confirmation email | A confirmation email is sent when a email is deleted from the database. | PASS

* Contact Us page

    TEST            | OUTCOME                          | PASS / FAIL  
    --------------- | -------------------------------- | ---------------
    Input Fields | Form will only be submitted when all fields were filed. | PASS
    Email field | Form will only be submitted when a valid email address is used. | PASS

* Products page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Image | Products are displayed in the correct format depending on the screen size. | PASS
  Card information| Information on the card corresponds to the related product image | PASS
  Price | Price information on the products card are displayed correctly if product is on sale. | PASS
  Links | Image and product name redirect the user to the "product details" page when clicked. | PASS
  "ADD TO CART" button | When clicked on, adds one item to the shopping cart. | PASS
  Sorting | Alphabetcaly sorting returns the expected result. | PASS
  Sorting | Sorting by price returns the expected result. | FAIL

    (Sorting by price produces the correct output but doesn't consider if the product has a reduced price on, resulting in the full price being used for sorting.)

* Products Details page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Image | Product image is displayed in a larger size. | PASS
  Product information | Card contains the correct product information. | PASS
  Rating | The average rating is displayed correctly. When the product has no reviews, a "No Reviews" text is displayed instead.| PASS
  Reviews | Reviews link redirects to the product reviews page. | PASS
  Quantity | Allow only values between 1 and 99. | PASS
  Edit and Delete | Links are only visible if the user is "superuser". | PASS
  ADD TO CART button | Adds the correct number of items to the cart. | PASS
  KEEP SHOPPING button |Redirects the user to the products page. | PASS

* On Sale page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Products |Only products on sale are displayed. |  PASS
  Product information | Card contains the correct product information. | PASS
  ADD TO CART button | Adds one item to the cart. | PASS

* Reviews page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Rating | Average rating is displayed correctly. | PASS
  Reviews Card | Author's name, ratings and comments are displayed correctly on the card. | PASS
  Edit and Delete | Links are only visible if the user is the review's author. | PASS
  LEAVE A REVIEW button | Loads the review form when clicked. | PASS
  KEEP SHOPPING button | Redirects the user back to the products page. | PASS

* Leave a review

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  LEAVE A REVIEW button | When clicked, the form is submitted and the new review is added to the reviews page. | PASS
  CANCEL button | Redirects to the reviews page when clicked. | PASS

* Edit a review

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Edit review page | Page is loaded when "Edit" link is clicked. | PASS  
  Review form |The form has the prepopulated product information. | PASS
  Rating input | Only accepts values between 0 and 5. | PASS
  EDIT A REVIEW button | The form is submitted and the review is updated when clicked. | PASS
  CANCEL button | Redirects to the reviews page when clicked. | PASS

* Delete a review
  
  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Delete review page | Page is loaded when the "Delete" link is clicked. | PASS
  Review card | The correct review information is displayed on the card. | PASS
  DELETE REVIEW button | When clicked, deletes the review entirely from the database and redirects the user to the reviews page. | PASS
  CANCEL button | Redirects to the reviews page when clicked. | PASS

* Product management page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Authentication | Page is only loaded if the user is "superuser". | PASS
  Add Product form | All form fields are loaded. | PASS
  ADD PRODUCT button | Product is added when all the required input fields are filled. | PASS
  CANCEL button | Redirects the user back to the home page. | PASS

* Product management edit

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Authentication | Page is only loaded if the user is "superuser". | PASS
  Edit Product form | All form fields are loaded and prepopulated. | PASS
  EDIT PRODUCT button | Product is updated with the new information. | PASS
  CANCEL button | Redirects the user back to the product details page. | PASS

* Product management delete

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Authentication | Page is only loaded if the user is "superuser". | PASS
  DELETE PRODUCT button | Deletes product from the database | PASS
  CANCEL button | Redirects the user back to the product details page. | PASS

* Shopping Cart page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Shopping cart | All the correct product information is displayed. | PASS
  Quantity | Product quantity can be updated from the cart. | PASS
  Product deletion  | Product can be entirely removed from the cart. | PASS
  Delivery fee | Delivery fee price is displayed correctly. | PASS
  Grand Total | Total of the order is displayed correctly. | PASS
  PROCEED TO CHECKOUT button | Redirects to the checkout page. | PASS
  KEEP SHOPPING button | Redirects back to the products page. | PASS

* Checkout page

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Checkout Summary | The order information is displayed correctly. | PASS
  Checkout form | All form fields are loaded correctly and prepopulated if the user is signed in. | PASS
  Save info check box | When checked, the user information is saved to the user's profile. | PASS
  COMPLETE ORDER button | When clicked order is processed, and the checkout success page is loaded. | PASS
  ADJUST CART button | Redirects back to the shopping cart page. | PASS

* Checkout success page

   TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Checkout success page | All order information is displayed correctly. | PASS
  Order | Order is added to the database. | PASS
  Stripe | Stripe shows no errors on the dashboard. | PASS
  Email | A confirmation email is sent to the user. | PASS
  Button | Button at the bottom of the page redirects the user to the "on sale" page. | PASS

* Authentication

  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  Register | User can register a new account. | PASS
  Sign in | User can sign in with an existing account. PASS
  Sign out | User can sign out. | PASS
  Confirmation | A confirmation email is sent when a new account is registered. | PASS

* 404 page
  
  TEST            | OUTCOME                          | PASS / FAIL  
  --------------- | -------------------------------- | ---------------
  404 page | Page is loaded when a page is not found. | PASS
  Image | 404 image is displayed on the page. | PASS
  GO BACK button | Redirects the user to the home page. | PASS

### Bugs

[Go to the top](#table-of-contents)

* Fixed:

  Issue - Total order price showed incorrect value.

  Fix - Added products on sale object to try block in the checkout view.

  ![views-onsale-bug](/readme_files/bugs/views-on-sale-bug-solution.png)

  In the orderLineItem model, check if products are on sale and use the correct price before saving them.

  ![models-onsale-bug](/readme_files/bugs/models-on-sale-bug-solution.png)

  Issue - The edit review button didn't update the review.

  Fix - Added the correct form action path.

* Not Fixed:
  
  Issue - When sorting products by price, products "onSale" are sorted using full price as a reference instead of half price.

  Issue - When there are items in the shopping cart, the success alert messages are shown on top of the cart contents.

  ![alerts-bug](/readme_files/bugs/success-message-with-items-cart.png)

  These two issues were discovered during the project manual testing in the final stages of the development, and with the submission date approaching, I had no time left to address them.

## 6 Search Engine Optimisation

[Go to the top](#table-of-contents)

To improve the website SEO, I created a list with short-tail and long-tail keywords and used [WorldTracker](https://www.wordtracker.com/) to find keywords with high traffic and low competition.These keywords were added to the website meta tags and headings, keeping the headings information meaningful to the user and avoiding keyword stuffing.

* Final list:
  * Board games
  * Board game shop
  * Board game store
  * Fun board games
  * Board game gift
  * Classic board games
  * Best price board games
  * Buy board games online
  * Board games for adults
  * Board game for two players

These keywords will need to be constantly monitored.

If necessary, keywords can be added or removed to keep improving the website's SEO.

## 7 Marketing

[Go to the top](#table-of-contents)

* Social Media:

  * Facebook:
  
    For the marketing strategy, I created a Facebook account where weekly posts to promote discounted products are posted.

    Other examples of posts would be a post when a new game is added to the website or sharing articles related to the board game scene.

    With a small investment, the Facebook page can be promoted on Facebook to increase the page's reach.

    ![facebook-page1](/readme_files/facebook-page1.png)
    ![facebook-page2](/readme_files/facebook-page2.png)

  * Tiktok:
    Another marketing strategy would be making short videos about specific products and promoting them on TikTok.

* Email Marketing:

    Having a newsletter is a free form of marketing and will keep subscribed customers updated about the ongoing sales and new products.

    Sending discounted codes through the newsletter will make subscribed customers more likely to complete a purchase, increasing sales numbers.

## 8 Deployment

[Go to the top](#table-of-contents)

Running the project locally:

1. Create a new Github repository.
2. Open a new Gitpod workspace.
3. Install Django and the supporting libraries.
4. Create the requirements.txt file. Here you include the project's dependencies so Heroku can recognize them.
5. Create a new Django Project.
6. Create all django apps.
7. Add apps to the installed apps in settings.py.
8. Migrate all new changes to the database.
9. Run the server to test "pyhton3 manage.py runserver".

Setting up the project to use PostgreSQL in Heroku:

1. Create Heroku App.
2. Install dj_database_url and psycopg2-binary in my local environment.
3. Freeze requirements.txt file.
4. In settings.py import dj_database_url.
5. Back up the local database using "./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json" in the terminal window.
6. Comment out the local default database.
7. Add the Heroku database url via dj_database_url.parse().
8. Run migrations to the Postgres database.
9. Restore the database using this command "./manage.py loaddata db.json" in the terminal windows.
10. Create a SuperUser for the Postgres database.
11. Configure the database so that when the app is running on Heroku it uses the Postgres database and when it's running locally it uses the SQLite database.
12. Create Procfile so that Heroku creates a web dyno so that it will run gunicorn and serve the Django app.
13. Disable Heroku collect static.
14. Add the Heroku hostname to allowed hosts in settings.py.
15. Generate a new Django secret key and add this to the Heroku config variables.
16. Replace the secret key in settings.py to grab it from the environment.
17. Set debug to True only if the environment is a development environment.
18. Commit changes and deploy to GitHub and Heroku.
19. Create an AWS account.
20. Create an S3 bucket.
21. Configure the S3 bucket settings and policies.
22. Create and configure the IAM service.
23. In the terminal install Boto3 and Django-storages.
24. Freeze requirements.txt file.
25. Add a statement to the AWS bucket if the environment is "USE_AWS".
26. Add AWS keys to the Heroku config variables.
27. Create custom storage classes for media and static files.
28. In settings.py add a statement to use the static and media storage class and locations.
29. Commit and push to GitHub and Heroku.
30. In the S3 bucket create a new folder for media.
31. Upload all used images to the media file in the S3 bucket.
32. Add the Stripe keys to the Heroku config variables.
33. Create a new webhook endpoint from the Stripe dashboard.
34. Add all the Stripe keys to the Heroku config variables.

## 9 Credits

[Go to the top](#table-of-contents)

### Code
  
* [Bootstrap](https://getbootstrap.com/) carousel, grid, buttons, navbar and footer features were used in this project.
* [Font Awesome](https://fontawesome.com/) icons were used in this project.
* The eCommerce part of the website was adapted from Code Institute 'Boutique Ado' walkthrough project.

### Content

* Home page Background image and logo was taken from [Canva](https://www.canva.com/).
* The privacy policy on the site came from [PrivacyPolicyGenerator](https://www.privacypolicygenerator.info/).
* The website site map was generated using [XML Sitemaps](https://www.xml-sitemaps.com/)
* All product images, description and reviews were taken from [Board Game Atlas](https://www.boardgameatlas.com/api/docs)
