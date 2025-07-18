# 🃏 Villain Trading Cards Project

This repository contains a progressive Flask project that builds a villain trading card web application across three branches. Each branch represents a new step in functionality and learning — from static templates to a full database-driven site.

---

## 📚 Table of Contents

- [📂 Branches Overview](#-branches-overview)
- [🔎 Branch-Specifics](#-branch-specifics)
- [🦹‍♂️ Project Background](#-project-background)
- [📦 Requirements](#-requirements)
- [🚀 Getting Started](#-getting-started)

---

## 📂 Branches Overview

| Branch            | Description                                                |
|------------------|------------------------------------------------------------|
| `template-layout`| Base layout with Flask routing and HTML template rendering |
| `static-site`    | Adds CSS, images, and static file handling                 |
| `with-database`  | Connects to a SQLite database using Flask-SQLAlchemy       |

---

## 🔎 Branch-Specifics

### 🔹 `template-layout`
- The simplest starting point  
- Renders a single villain card from a Python dictionary  
- No styling or database involved  

### 🔹 `static-site`
- Adds static assets like CSS and images  
- Improves visual layout and card design  

### 🔹 `with-database`
- Uses Flask-SQLAlchemy to store and retrieve villain data  
- Villains are no longer hardcoded — pulled from a SQLite database  

---

## 🦹‍♂️ Project Background

This project was part of Skillcrush's "Using Python to Build Web Apps" lesson. Through the materials and assistance Skillcrush provided, I practiced coding a web app that allows the user to fill out a form and add a new supervillain card. That information is saved in a SQL database. The app is built with Flask and uses Flask-SQLAlchemy to work with the database. It uses routes and HTTP methods to send and receive data between the front end and back end, as well as Jinja templates to display the data on web pages.

---

## 📦 Requirements

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy

Install requirements with:

```bash
pip install -r requirements.txt
```

## 🚀 Getting Started

These instructions will help you run the app in **any of the three branches**. Open your command line and follow these steps:

### 1. Clone the repository and navigate to it

```bash
git clone https://github.com/jesteffes/villain-trading-cards-template.git
cd villain-trading-cards-template
```
### 2. Check out the branch you want to interact with:

```bash
git checkout with-database  # or static-site, or template-layout
```
### 3. Create and activate a virtual environment:
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
 ```
 **Mac/Linux:**
 ```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Install dependencies:
```bash
pip install -r requirements.txt
```
### 5. Run the app:
```bash
flask run
```


---
Then open your browser at: http://127.0.0.1:5000

To stop the server, press Ctrl + C.

To exit the virtual environment, run:
```
deactivate
```

