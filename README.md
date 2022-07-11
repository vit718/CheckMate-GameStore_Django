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
    * [Bugs](#bugs)
    * [User Story Testing](#user-story-testing)
        * [EPIC 1 Testing](#epic-1-testing)
        * [EPIC 2 Testing](#epic-2-testing)
        * [EPIC 3 Testing](#epic-3-testing)
        * [EPIC 4 Testing](#epic-4-testing)
        * [EPIC 5 Testing](#epic-5-testing)
        * [EPIC 6 Testing](#epic-6-testing)
6. [Search Engine Optimisation](#search-engine-optimisation)
7. [Marketing](#marketing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## 1. Ux

As a big fan of game boards, I have always looked online when wanting to buy a new game board. This website will showcase a selection of games for the user to buy in a simple-to-use UI.

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

- Viewing the webpage

![Viewing](/readme_files/user-stories/user-story-viewing-the-webpage.png)

- Filtering and searching

![Viewing](/readme_files/user-stories/user-story-filtering-and-searching.png)

- Buying a product

![Viewing](/readme_files/user-stories/user-story-buying-product.png)

- Registration / Accounts

![Viewing](/readme_files/user-stories/user-story-registration-and-account.png)

- Admin and store management

![Viewing](/readme_files/user-stories/user-story-admin.png)

- Interacting and engaging

Not all CRUD functionality was implemented for the "reviews" user story.

The user can leave a review, but editing and deleting were not implemented and will be dealt with in the second phase of this project.

The "contact us" functionality will be implemented in the second phase of this project.

![Interacting](/readme_files/user-stories/user-story-interacting.png)

## 2. Data Models

Data models used in this project:

- Products app

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

- Reviews app

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

- Newsletter app

```python
class Subscriber(models.Model):
    """Model for subscriber email information"""

    email = models.EmailField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
```

The following apps have their data models based on the Boutique Ado project.
- bag app
- checkout app
- profiles app

## 3. Features

### 3.1 First Phase

- Navbar 

![Navbar](/readme_files/features/features-navbar.png)

On the right, The navigation bar contains the site logo and a link to the home page.

A search bar in the center of the navbar for searching products.
On the right, the My Account dropdown with links for product management, sign in, and sign out pages.

Also on the right is a shopping cart icon that works as a link for the shopping cart page and displays the current total amount in the cart.

Under the search bar there are 5 links.

- (Home), a link to the "home" page

- (All products), dropdown with options to search products by price and rating.

- (Board games), dropdown with options for game categories (Family, Strategy,   Party, Classic) and "all board games".
    
- (Role-Playing), dropdown with options for dungeons & dragons, pathfinder and all role-playing games.
    
- (On sale), a link to the "on sale" page.


### 3.2 Second Phase

Unfortunately, several important concepts are missing from this project due to the deadline submission date.

The Readme file is not completed. The following sections are missing.

3. Features 
4. Technologies Used
5. Testing
6. Search Engine Optimisation
7. Marketing
8. Deployment
9. Credits

Also, features like robox.txt, sitemap and Facebook page still need to be done.

To be continued...