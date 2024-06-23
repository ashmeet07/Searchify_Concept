# 🏫🏠 Searchify_Concept

Welcome to **Searchify_Concept**, your ultimate solution for finding the perfect hostel accommodation for college and university students. This Django-powered application provides a seamless and efficient way for students to search for hostels, view details, and make informed decisions.

## 🌟 Features

- **Easy Search:** Students can search for hostels based on location, price range, amenities, and more.
- **Detailed Listings:** Each hostel listing includes photos, descriptions, amenities, and reviews.
- **User Authentication:** Secure login and registration system for students and hostel owners.
- **Reviews and Ratings:** Students can leave reviews and ratings to help others make informed choices.
- **Responsive Design:** Accessible on all devices, from desktops to smartphones.

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Django 3.x
- PostgreSQL (or any preferred database)
- Virtualenv

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Searchify_Concept.git
   cd Searchify_Concept
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Update `DATABASES` settings in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

   - Run migrations:
     ```sh
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

6. **Collect static files:**
   ```sh
   python manage.py collectstatic
   ```

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

8. **Open your browser and navigate to:**
   ```sh
   http://127.0.0.1:8000/
   ```

## 📚 Documentation

For detailed documentation, including API endpoints and usage, please refer to the [Wiki](https://github.com/yourusername/Searchify_Concept/wiki).

## 📸 Searchify Glimpse

![Searchify Screenshot](https://github.com/ashmeet07/Searchify_Concept/assets/91828139/e2805683-8bbf-4cee-ac73-555bfa2a57fc)

## **Our Group Members**

### Ashmeet Singh, Abhijeet Shushir, Garima Chauhan, Amit Sahu, Amit Prajapati

![Group Photo](https://github.com/ashmeet07/Searchify_Concept/assets/91828139/49cff9a3-907e-4631-bce5-20b7c2846ab2)

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](https://github.com/yourusername/Searchify_Concept/blob/main/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/yourusername/Searchify_Concept/blob/main/LICENSE) file for details.

## 📧 Contact

If you want to use the code, please take permission first or mail us at gaminggods0123@gmail.com.

## 🙌 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwesome](https://fontawesome.com/)

## 🌐 Connect with Us

- **Email:** gaminggods0123@gmail.com

---

*Helping students find their home away from home.* 🌍🏠📚
