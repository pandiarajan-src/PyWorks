'''Learn environment'''
import os
from dotenv import load_dotenv

load_dotenv()

PWD_VALUE_FROM_DOT_ENV = os.getenv("PASSWORD")
WHAT_TO_USE_FROM_DOT_ENV = os.getenv("WHATTOUSE")
print(PWD_VALUE_FROM_DOT_ENV)
print(WHAT_TO_USE_FROM_DOT_ENV)
