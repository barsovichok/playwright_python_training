from dotenv import load_dotenv
import os


env = os.getenv("TEST_ENV", "dev")
env_file = f".env.{env}"

load_dotenv(dotenv_path=env_file)

BASE_URL = os.getenv("BASE_URL")
INVENTORY_URL = os.getenv("INVENTORY_URL")
