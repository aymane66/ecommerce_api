# E-commerce Product API

## Project Overview

This project is a **Django + Django REST Framework (DRF) backend API** for managing products in an e-commerce platform. It provides full **CRUD functionality for products and categories**, **user authentication**, **search & filtering**, and **pagination**, simulating a real-world backend system for e-commerce.  

The API is designed to be **secure, modular, and deployable** on production platforms like Render.  

---

## Features Implemented

### 1. Product Management (CRUD)
- Create, Read, Update, Delete products.
- Product fields: `name`, `description`, `price`, `category`, `stock_quantity`, `image_url`, `created_date`, `added_by`.
- `added_by` tracks which authenticated user created the product.
- Only authenticated users can create, update, or delete products.

### 2. Category Management
- Separate `Category` model for organizing products.
- CRUD operations on categories.
- Each product is linked to a category via ForeignKey.
- Categories include `name` and `slug` fields for easy URL handling.

### 3. User Authentication
- JWT-based authentication using `djangorestframework-simplejwt`.
- Endpoints to obtain and refresh tokens:
  - `POST /api/token/` → get access & refresh token
  - `POST /api/token/refresh/` → refresh access token
- Authenticated users can perform write actions on products.

### 4. Search, Filtering, and Pagination
- Search products by `name` or `category`.
- Filter products by `category`, `price range`, and `stock quantity`.
- Ordering by `price`, `created_date`, or `stock_quantity`.
- Paginated API responses (default 10 items per page).

### 5. Security & Permissions
- Only authenticated users can create, update, delete products.
- Optional owner-only permission implemented to allow users to edit only their own products.
- Safe read-only access for unauthenticated users.

---

## Technical Details

- **Framework:** Django 4.x, Django REST Framework
- **Database:** PostgreSQL (deployed on Render)
- **Authentication:** JWT
- **Deployment:** Render.com
- **Python Version:** 3.x
- **Dependencies:** See `requirements.txt`

---

## Project Structure

ecommerce_api/
│
├── ecommerce_api/ # Project settings
│ ├── settings.py # Production-ready settings
│ └── urls.py
│
├── products/ # Products and Categories app
│ ├── models.py # Product and Category models
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── users/ # User management app
│ └── urls.py
│
├── manage.py
└── requirements.txt



---

## Setup Instructions (Local)

1. Clone the repository:

git clone 
cd ecommerce_api


2. Install dependencies:

pip install -r requirements.txt


3. Set environment variables (example .env):

export DJANGO_SECRET_KEY='your-secret-key'
export DEBUG=True
export DB_NAME='your-db-name'
export DB_USER='your-db-user'
export DB_PASSWORD='your-db-password'
export DB_HOST='localhost'
export DB_PORT='5432'


4. Run migrations:

python3 manage.py migrate


5. Create superuser (optional for admin access):

python manage.py createsuperuser


6. Start the server:

python manage.py runserver



## API Endpoints (Implemented So Far)

### Products
| Method |        Endpoint       |                     Description                         |
|--------|-----------------------|---------------------------------------------------------|
| GET    | `/api/products/`      | List all products (supports search, filter, pagination) |
| POST   | `/api/products/`      | Create a product (authenticated users only)             |
| GET    | `/api/products/<id>/` | Retrieve product details                                |
| PUT    | `/api/products/<id>/` | Update a product (owner only)                           |
| DELETE | `/api/products/<id>/` | Delete a product (owner only)                           |

### Categories
| Method |        Endpoint         |                   Description                | 
|--------|-------------------------|----------------------------------------------|
| GET    | `/api/categories/`      | List all categories                          |
| POST   | `/api/categories/`      | Create a category (authenticated users only) |
| GET    | `/api/categories/<id>/` | Retrieve category details                    |
| PUT    | `/api/categories/<id>/` | Update a category (authenticated users only) |
| DELETE | `/api/categories/<id>/` | Delete a category (authenticated users only) |

### Authentication
| Method |         Endpoint      |      Description     |
|--------|-----------------------|----------------------|
| POST   | `/api/token/`         | Obtain JWT tokens    |
| POST   | `/api/token/refresh/` | Refresh access token |
