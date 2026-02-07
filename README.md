# KarinShop

KarinShop is a full-featured e-commerce web application built with Django. It is designed with a modular architecture, clean code structure, and scalability in mind, making it suitable for learning, prototyping, and extending into a production-ready online store.

---

## Features

- User authentication and account management  
- Product catalog with images and details  
- Shopping cart functionality  
- Article/blog module for content management  
- Media and static file handling  
- Clean and responsive Django templates  
- Modular Django app structure  

---

## Tech Stack

- Backend: Python, Django  
- Frontend: HTML, CSS, JavaScript  
- Database: SQLite (default)  
- Template Engine: Django Templates  

---

## Installation

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

Clone the repository:

```bash
git clone https://github.com/Fatemehjanii/karinshop.git
cd karinshop
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

Install dependencies:

```bash
pip install django
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser (optional):

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
karinshop/
├── accounts/
├── articles/
├── cart/
├── core/
├── products/
├── media/
├── static/
├── templates/
├── db.sqlite3
└── manage.py
```

---

## Purpose

This project is suitable for:

- Learning Django project architecture
- Practicing backend and full-stack development
- Building and extending an e-commerce platform

---

## Future Improvements

- REST API with Django REST Framework
- Payment gateway integration
- Product search and filtering
- Order management system
- Deployment with Docker and CI/CD

---

## License

This project is open-source. You may add a license file (MIT, Apache 2.0, etc.) as needed.
 
