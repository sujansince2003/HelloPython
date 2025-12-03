import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get("API_KEY","defaultvalue if env value doesnot exist"))