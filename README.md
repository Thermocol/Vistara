# Vistara Project
## Overview
Vistara is a web application built using Django that allows users to upload, share, and view videos. The platform provides a user-friendly interface for content creators to showcase their work and engage with their audience through comments and profiles.
## Features
- User authentication and account management using Django Allauth.
- Video upload functionality with support for various video formats.
- Profile management for users to display their uploaded content.
- Commenting system for user interaction on videos.
- Admin panel for managing users and content.
## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django Allauth**: A Django application that provides a comprehensive authentication system.
- **SQLite**: A lightweight database for development and testing.
- **HTML/CSS/JavaScript**: For front-end development and user interface design.
- **Bootstrap**: For responsive design and styling.
- **Font Awesome**: For icons and visual elements.
## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sairashwant/Vistara
   cd Vistara
2. **Create Virtual Env if needed**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
4. **Create a superuser (for accessing the admin panel)**:
   ```bash
    python manage.py createsuperuser
5. **Run the development server**:
   ```bash
    python manage.py runserver
6. **Access the application: Open your web browser and go to http://127.0.0.1:8000/**

