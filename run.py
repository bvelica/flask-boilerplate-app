
from app import create_app

### Load the configuration from a .env file when it is present
from dotenv import load_dotenv

# Take environment variables from .env.
load_dotenv('.env')


if __name__ == "__main__":
    create_app.run()
