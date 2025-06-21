#  Django Internship Assignment 

This project was developed as part of an internship assignment. It is a complete Django-based backend system that includes REST API authentication, background tasks, and Telegram bot integration.

---

##  Features

- Django REST Framework (DRF) for building APIs  
- JWT Authentication using `SimpleJWT`  
- Celery + Redis for background task processing  
- Sends a welcome email when a user registers  
- Telegram bot that stores user info when they send `/start`  
- Secure production-style setup using `.env`

---


##  Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/django-fan-project.git
cd django-fan-project
```

### 2. Create virtual environment & activate
```
python -m venv env
env\Scripts\activate   # For Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Configure environment variables
cp .env.example .env
# Then open .env and fill in your credentials

### 5. Run database migrations
```
python manage.py migrate
python manage.py createsuperuser
```

### 6. Start development server
```
python manage.py runserver
```

### Celery + Redis Setup
## Start Redis server (on WSL or installed natively), then run:
```celery -A myproject worker --loglevel=info --pool=solo
```

### Telegram Bot Setup
  Create a bot with @BotFather
  Add the bot token to your .env
  Run the bot:

  ``` python -m telegrambot.bot
  ```
Now send /start to the bot in Telegram — your username will be saved.
