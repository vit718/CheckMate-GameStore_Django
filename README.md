# CheckMate GameStore

Welcome to my fifth milestone project, an e-commerce website that focuses on selling board games. CheckMate is a fictional store that relies on online sales alone to make revenue.
This project uses the Django framework, HTML, Python, CSS and JavaScript.

A live website can be found [here](https://marcellomuy-checkmate.herokuapp.com/).

![website preview](/readme_files/website-preview.png)

## Table of Contents

1. [UX](#ux)
    * [Colour Scheme and Font](#colour-scheme-and-font)
    * [Wireframes](#wireframes)
    * [Project Management](#project-management)
    * [User Stories](#user-stories)
2. [Data Models](#data-models)
3. [Features](#features)
    * [First Phase](#first-phase)
    * [Second Phase](#second-phase)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
    * [Validation](#validation)
        * [HTML](#html)
        * [CSS](#css)
        * [JaveScript](#javascript)
        * [Python](#python)
    * [Manual Testing](#user-story-testing)
        * [Home page](#home-page)
    * [Bugs](#bugs)
6. [Search Engine Optimisation](#search-engine-optimisation)
7. [Marketing](#marketing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## 1. Ux

As a big fan of board games, I have always looked online when wanting to buy a new game board. This website will showcase a selection of games for the user to buy in a simple-to-use UI.

### 1.1 Colour Scheme and Font

Please find colour scheme used for this project [here](https://coolors.co/002f33-5da3a6-e6f4f1).

The [Roboto flex](https://fonts.google.com/specimen/Roboto+Flex?query=roboto+flex) was used as the website font across all pages.

The website logo was created using [Canva](https://www.canva.com/) designing tools.

![Logo](/media/logo.png)

### 1.2 Wireframes

Mobile and Desktop wireframes were created for some pages of the website.

Due to lack of time, some features fell outside the scope of this project, and wireframes and final project might look different.

#### Home Page

![Home](/readme_files/wireframes/wireframe-home.png)

#### Products Page

![Products](/readme_files/wireframes/wireframe-products.png)

#### Product Details

![Detail](/readme_files/wireframes/wireframe-product-details.png)

#### Shopping Cart

![Cart](/readme_files/wireframes/wireframe-cart.png)

#### Checkout Page

![Checkout](/readme_files/wireframes/wireframe-checkout.png)

#### Reviews Page

![Reviews](/readme_files/wireframes/wireframe-reviews.png)

### 1.3 Project Management

A Kanban board was created on GitHub and was used as a project management tool.
User stories are divided into 6 EPIC labels.

### 1.4 User Stories

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

## 2. Data Models

Data models used in this project:

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

## 3. Features

### 3.1 First Phase

* Navbar

![Navbar](/readme_files/features/features-navbar.png)

On the right, The navigation bar contains the site logo and a link to the home page.

A search bar in the center of the navbar for searching products.
On the right, the My Account dropdown with links for product management, sign in, and sign out pages.

Also on the right is a shopping cart icon that works as a link for the shopping cart page and displays the current total amount in the cart.

Under the search bar there are 5 links.

* (Home), a link to the "home" page

* (All products), dropdown with options to search products by price and rating.

* (Board games), dropdown with options for game categories (Family, Strategy,   Party, Classic) and "all board games".

* (Role-Playing), dropdown with options for dungeons & dragons, pathfinder and all role-playing games.

* (On sale), a link to the "on sale" page.

### 3.2 Second Phase

## 5 Testing

### 5.1 Validation

#### 5.1.1 HTML

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

#### 5.1.2 CSS

  CSS code was validated using W3C CSS validator.

 The validator found no errors in all 3 css files:

* base.css
* profile.css
* checkout.css

  ![css-no-errors](/readme_files/validation/css/validation-css-no-errors.png)

#### 5.1.3 JavaScript

  All JavaScript code was validate using jshint. 
  
  All code was copied into the validator and
  three lines of code were added at the top of the page to ignore some warnings.
  
* /*jshint esversion: 6 */
  
* /*globals $:false */
  
* /*globals Stripe:false */

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

#### 5.1.4 Python



