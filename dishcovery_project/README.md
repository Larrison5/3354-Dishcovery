<div align="center">

# 🍽️ Dishcovery

### Personalized Restaurant Discovery Platform

Find restaurants based on your dining preferences using an intelligent matching system built with the **Model-View-Controller (MVC)** architecture.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![MVC](https://img.shields.io/badge/Architecture-MVC-green)
![Status](https://img.shields.io/badge/Status-In_Development-orange)

</div>

---

# 📖 About the Project

Dishcovery is a web application that helps users discover restaurants based on their personal dining preferences instead of browsing through hundreds of search results.

Users can create an account, save their dining preferences, receive personalized restaurant recommendations, and keep track of favorite restaurants. Administrators are able to manage restaurant information through a separate administration interface.

This project was developed as part of **CS 3354 – Software Engineering** and follows the **Model-View-Controller (MVC)** software architecture.

---

# ✨ Features

## Customer Features

- Create a new account
- Secure login and logout
- Save dining preferences
- Receive personalized restaurant recommendations
- Search restaurants
- View restaurant profiles
- Save favorite restaurants
- Remove restaurants from favorites

---

## Administrator Features

- Add restaurants
- Edit restaurant information
- Delete restaurants
- Manage restaurant database

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Web Framework |
| SQLite | Database |
| SQLAlchemy | ORM |
| Flask-Login | User Authentication |
| HTML5 | Frontend |
| CSS3 | Styling |
| Git | Version Control |
| GitHub | Team Collaboration |

---

# 🏛 Architecture

The project follows the **Model-View-Controller (MVC)** design pattern.

```
                User
                  │
                  ▼
          Controllers (Routes)
                  │
                  ▼
          Business Services
                  │
                  ▼
        Repository / Database
                  ▲
                  │
              SQLAlchemy
```

### Models

Store application data.

Examples:

- User
- Restaurant
- Preference
- Favorite

### Views

Responsible for displaying pages to the user.

Examples:

- Login
- Register
- Restaurant Search
- Restaurant Profile
- Favorites
- Administrator Dashboard

### Controllers

Handle incoming requests and coordinate communication between the views and services.

---

# 📂 Project Structure

```text
Dishcovery
│
├── app
│   ├── controllers
│   ├── models
│   ├── repositories
│   ├── services
│   ├── static
│   └── templates
│
├── tests
│
├── requirements.txt
├── seed.py
├── run.py
└── README.md
```

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone (https://github.com/Larrison5/3354-Dishcovery)
```

---

## 2. Navigate into the project

```bash
cd Dishcovery
```

---

## 3. Create a virtual environment

Windows

```powershell
py -m venv .venv
```

Activate

```powershell
.venv\Scripts\activate
```

---

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 5. Create the database

```powershell
py seed.py
```

---

## 6. Start the application

```powershell
py run.py
```

---

## 7. Open your browser

```
http://127.0.0.1:5000
```

---

# 👤 Demo Accounts

## Administrator

```
Email:
admin@dishcovery.com

Password:
admin123
```

---

## Customer

```
Email:
customer@dishcovery.com

Password:
customer123
```

---

# 🧪 Running Tests

```powershell
pytest
```

---

# 👨‍💻 Development Workflow

Our team follows a GitHub feature-branch workflow.

```
main
│
├── feature-authentication
├── feature-restaurant-search
├── feature-matching
├── feature-favorites
└── feature-admin
```

Each feature is developed in its own branch before being merged into the main branch through a Pull Request.

---

# 🎯 Future Improvements

Possible future enhancements include:

- Google Maps integration
- Restaurant photos
- AI-powered restaurant recommendations
- User reviews and ratings
- Distance-based recommendations
- Mobile responsive design
- Dark mode
- Restaurant recommendation history

---

# 📚 Course Information

**Course**

CS 3354 – Software Engineering

**Project**

Dishcovery – Personalized Restaurant Recommendation System

---

<div align="center">

### Built using Python, Flask, SQLite, and the MVC Design Pattern

</div>