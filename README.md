# E-commerce Product API

## Project Overview

This project is a **Django + Django REST Framework (DRF) backend API** for managing products, users, and purchases in an e-commerce platform. It provides full **CRUD functionality for products and categories**, **user authentication**, **purchase tracking**, **search & filtering**, and **pagination**, simulating a real-world backend system for e-commerce.  

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

### 4. Purchases
- Users can purchase products.
- Each purchase is linked to a `user` and `product`.
- Purchase fields: `user`, `product`, `quantity`, `total_price`, `purchase_date`.
- Authenticated users can view their purchase history.

### 5. Search, Filtering, and Pagination
- Search products by `name` or `category`.
- Filter products by `category`, `price range`, and `stock quantity`.
- Ordering by `price`, `created_date`, or `stock_quantity`.
- Paginated API responses (default 10 items per page).

### 6. Security & Permissions
- Only authenticated users can create, update, delete products.
- Owner-only permission implemented for product editing.
- Purchases restricted to authenticated users.
- Safe read-only access for unauthenticated users.

---

## Technical Details

- **Framework:** Django 4.x, Django REST Framework
- **Database:** PostgreSQL (deployed on Render) /SQLite (locally)
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
├── purchases/ # Purchases app
│ ├── models.py # Purchase model
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

```bash
git clone https://github.com/aymane66/ecommerce_api
cd ecommerce_api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set environment variables (example .env):

```bash
export DJANGO_SECRET_KEY='your-secret-key'
export DEBUG=True
export DB_NAME='your-db-name'
export DB_USER='your-db-user'
export DB_PASSWORD='your-db-password'
export DB_HOST='localhost'
export DB_PORT='5432'
```

4. Run migrations:

```bash
python3 manage.py migrate
```

5. Create superuser (optional for admin access):

```bash
python3 manage.py createsuperuser
```

6. Start the server:

```bash
python3 manage.py runserver
```


## API Endpoints

### Products

| Method | Endpoint              | Description                                             |
| ------ | --------------------- | ------------------------------------------------------- |
| GET    | `/api/products/`      | List all products (supports search, filter, pagination) |
| POST   | `/api/products/`      | Create a product (authenticated users only)             |
| GET    | `/api/products/<id>/` | Retrieve product details                                |
| PUT    | `/api/products/<id>/` | Update a product (owner only)                           |
| DELETE | `/api/products/<id>/` | Delete a product (owner only)                           |


### Categories

| Method | Endpoint                | Description                                  |
| ------ | ----------------------- | -------------------------------------------- |
| GET    | `/api/categories/`      | List all categories                          |
| POST   | `/api/categories/`      | Create a category (authenticated users only) |
| GET    | `/api/categories/<id>/` | Retrieve category details                    |
| PUT    | `/api/categories/<id>/` | Update a category (authenticated users only) |
| DELETE | `/api/categories/<id>/` | Delete a category (authenticated users only) |


### Purchases

| Method | Endpoint               | Description                                  |
| ------ | ---------------------- | -------------------------------------------- |
| GET    | `/api/purchases/`      | List all purchases (user-specific)           |
| POST   | `/api/purchases/`      | Create a purchase (authenticated users only) |
| GET    | `/api/purchases/<id>/` | Retrieve purchase details                    |


### Authentication

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/token/`         | Obtain JWT tokens    |
| POST   | `/api/token/refresh/` | Refresh access token |
