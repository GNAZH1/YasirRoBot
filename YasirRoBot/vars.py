# (c) adarsh-goel
import os
import sys
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    
    # Ensure API_ID and other important variables are provided
    try:
        API_ID = int(getenv("API_ID"))
    except TypeError:
        sys.exit("Error: API_ID is not set in the environment or is invalid.")
    
    API_HASH = str(getenv("API_HASH", ""))
    if not API_HASH:
        sys.exit("Error: API_HASH is not set in the environment.")
    
    BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
    if not BOT_TOKEN:
        sys.exit("Error: BOT_TOKEN is not set in the environment.")
    
    name = str(getenv("name", "filetolinkbot"))
    SLEEP_THRESHOLD = int(getenv("SLEEP_THRESHOLD", "60"))
    WORKERS = int(getenv("WORKERS", "4"))
    
    try:
        BIN_CHANNEL = int(getenv("BIN_CHANNEL"))
    except TypeError:
        BIN_CHANNEL = None
    
    PORT = int(getenv("PORT", 8080))
    BIND_ADDRESS = str(getenv("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    NO_PORT = bool(getenv("NO_PORT", False))
    
    APP_NAME = None
    OWNER_USERNAME = str(getenv("OWNER_USERNAME", ""))
    
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    
    ON_HEROKU = "DYNO" in environ
    if ON_HEROKU:
        APP_NAME = str(getenv("APP_NAME", ""))
    
    FQDN = str(getenv("FQDN", BIND_ADDRESS)) if not ON_HEROKU or getenv("FQDN") else APP_NAME + ".herokuapp.com"
    HAS_SSL = bool(getenv("HAS_SSL", False))
    
    if HAS_SSL:
        URL = f"https://{FQDN}/"
    else:
        URL = f"http://{FQDN}/"
    
    DATABASE_URL = str(getenv("DATABASE_URL", ""))
    UPDATES_CHANNEL = str(getenv("UPDATES_CHANNEL", None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
