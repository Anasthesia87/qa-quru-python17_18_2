import os

from dotenv import load_dotenv

load_dotenv()

login = os.getenv('LOGIN')
access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
project = os.getenv('BROWSERSTACK_PROJECT')
timeout = os.getenv('BROWSERSTACK_TIMEOUT')
app = os.getenv('BROWSERSTACK_APP')