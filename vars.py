#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "6024888"))
API_HASH = environ.get("API_HASH", "c78489a1b52a6dac192f2c1b6eb30435")
BOT_TOKEN = environ.get("BOT_TOKEN", "7855245857:AAEhp3xYfBBxwg4EhsiUNVj4fWYdPDqf-Cc")

OWNER = int(environ.get("OWNER", "1786342431"))
CREDIT = environ.get("CREDIT", "SS 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1786342431').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1786342431').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

