
from app import create_app
from dotenv import load_dotenv

# the path to your .env file
load_dotenv('.env')


if __name__ == "__main__":
    create_app.run()
