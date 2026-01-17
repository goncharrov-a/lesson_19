import os
from dotenv import load_dotenv

load_dotenv()

bstack_userName = os.getenv("BSTACK_USERNAME")
bstack_accessKey = os.getenv("BSTACK_ACCESS_KEY")
timeout = float(os.getenv("TIMEOUT", 10))