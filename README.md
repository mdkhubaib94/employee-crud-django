# Employee CRUD Django API

This is a Django REST API for managing employees, allowing Create, Read, Update and Delete operations on employee data.

## 🚀 Features

- Implemented using Django and Django REST Framework (DRF)
- Supports CRUD operations for an `Employee` model
- Swagger or browsable API for easy testing

## 🧰 Prerequisites

- Python 3.8 or newer
- pip
- (Optional but recommended) virtualenv or venv

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mdkhubaib94/employee-crud-django.git
cd employee-crud-django

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# (Optional) Create admin superuser to manage via Django admin
python manage.py createsuperuser

# Run the development server
python manage.py runserver
