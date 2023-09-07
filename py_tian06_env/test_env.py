
from dotenv import load_dotenv
import os

load_dotenv()

router_url = os.getenv('URL')



print(router_url)