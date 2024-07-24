
# Bluestock IPO REST API

**Developer:** Apurv Nandgaonkar
**Email:** apurv.mod007@gmail.com 

This project is a REST API developed for Bluestock Fintech to manage and showcase IPOs (Initial Public Offerings) to users. The application is built using Django and Django Rest Framework, with PostgreSQL (NeonDB) as the database. The admin can perform CRUD operations, while users can access protected endpoints through JWT authentication.

## Objectives

- Provide a REST API to showcase IPOs to users.
- Enable CRUD operations for IPOs through the admin interface.
- Secure user endpoints with JWT tokens and authentication routes.

## Features

### Admin CRUD Operations
- **POST /administrator/api/v1/ipo-list/**: Create a new IPO.
- **GET /administrator/api/v1/ipo-list/**: Retrieve details of existing IPOs.
- **PUT /administrator/api/v1/ipo-list/1/**: Update the details of an existing IPO.
- **DELETE /administrator/api/v1/ipo-list/3/**: Delete an existing IPO.

### User Operations
- **POST /api/user/register/**: Register a new user.
- **POST /api/user/login/**: Authenticate and login a user.
- **POST /api/user/changepassword/**: Change the password of a logged-in user.
- **GET /api/user/ipo/**: Retrieve a list of IPOs available to the user.
- **GET /api/user/profile/**: Retrieve the profile details of the logged-in user.
- **POST /api/user/send-reset-password-email/**: Send an email to reset the user's password.
- **POST /api/user/reset-password/Mg/cap9d3-cdeca75119a04233b2bbc5a5c166ac4f/**: Reset the user's password using a token sent via email.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL (NeonDB)
- Django 5.0.7
- Django Rest Framework
- Postman or any API testing tool

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/bluestock-ipo-rest-api.git
   cd bluestock-ipo-rest-api
   ```
git commit -m "first commit"
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file:**

   Create a `.env` file in the project root directory and add the following environment variables:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1, .localhost
   DATABASE_URL=postgres://yourusername:yourpassword@yourhost:yourport/yourdbname
   EMAIL_USER=your_email_user
   EMAIL_PASS=your_email_password
   EMAIL_FROM=your_email_from
   ```

5. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

### Access the Admin Interface

Open your web browser and go to `http://127.0.0.1:8000/admin`. Log in using the superuser credentials to manage IPOs.

### API Documentation

You can use tools like Postman to test the endpoints listed in the features section. Make sure to include the JWT token in the Authorization header for protected endpoints.

## License

This project is licensed under the Bluestock Fintech License.
https://bluestock.in/
---
