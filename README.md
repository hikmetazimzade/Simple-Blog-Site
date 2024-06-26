# Simple Blog Site

A Django-based blogging platform designed for easy creation and management of personal blogs. It features a clean interface and leverages modern web technologies.

## Features

- **User Authentication**: Enables users to register and log in.
- **CRUD Operations**: Users can create, read, update, and delete blog posts.
- **Responsive Design**: Ensures a great experience on all device sizes.
- **Comment System**: Readers can engage with content through comments.
- **Web Scraping**: Uses Requests and Beautiful Soup for content scraping.

## Technologies Used

- Django
- SQLite3
- JavaScript
- HTML/CSS
- Requests
- Beautiful Soup

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hikmetazimzade/Simple-Blog-Site.git
   cd Simple-Blog-Site

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run Migrations:**
   ```bash
   cd main_project
   python manage.py makemigrations
   python manage.py migrate

4. **Start Server:**
   ```bash
   python manage.py runserver
