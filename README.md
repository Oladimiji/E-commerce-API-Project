# Django E-commerce API

This project is a RESTful API for a full-featured e-commerce platform, built with Django and Django REST Framework. It provides all the backend functionality required for an online store, including user authentication, product management, a shopping cart, and a complete order/checkout system.

## Features

- *User Authentication:* Secure user registration and login using JSON Web Tokens (JWT).
- *Product Management:* Full CRUD (Create, Read, Update, Delete) functionality for products, restricted to admin users.
- *Shopping Cart:* A dedicated shopping cart system that allows authenticated users to add, view, update, and delete products from their cart.
- *Order Processing:* A comprehensive checkout process that converts a user's cart into a permanent order and empties the cart.
- *Permissions:* Utilizes Django REST Framework's permission system to restrict access to certain endpoints (e.g., only admins can manage products).

## Technology Stack

- *Backend:* Django, Django REST Framework
- *Authentication:* djangorestframework-simplejwt for JWT-based authentication
- *Database:* SQLite3 (default)
- *API Testing:* .http file for easy request testing

## Setup and Installation

### 1. Clone the repository

```bash
git clone [https://github.com/YourUsername/your-repo-name.git](https://github.com/YourUsername/your-repo-name.git)
cd your-repo-name