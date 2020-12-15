An example of Django project with basic user functionality.

## Live
[MyCart](https://mycart-web.herokuapp.com/shop/)

## Screenshots

| Landing Page | Tracker | About |
| -------|--------------|-----------------|
| <img src="./screenshots/page1.PNG" width="400"> | <img src="./screenshots/tracker1.PNG" width="400"> | <img src="./screenshots/about.PNG" width="400"> |
| Checkout | Contact | Search |
| <img src="./screenshots/checkout.PNG" width="400"> | <img src="./screenshots/contact.PNG" width="400"> | <img src="./screenshots/watch_search.PNG" width="400"> |

## Functionality

- Pages
    - Home
    - About Us
    - Tracker
    - Contact Us
 - Product Cart System
    - Auto Calculate Price and Increase/Decrease products
 - Smart Search Bar
 - Tracker
    - to Track Orders using Order Id and Email


## Installing

### Clone the project

```
git clone https://github.com/raja53a/MyCart.git
cd MyCart
```

### Install dependencies & activate virtualenv

```
pip install pipenv

pip install -r requirements.txt

```
### Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```
### Running

#### A development server

Just run this command:

```
python manage.py runserver
```
