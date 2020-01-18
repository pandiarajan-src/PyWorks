from dotenv import load_dotenv

load_dotenv()
import os

pwd_value_from_dot_env = os.getenv("PASSWORD")
what_to_use_from_dot_env = os.getenv("WHATTOUSE")
print(pwd_value_from_dot_env)
print(what_to_use_from_dot_env)


