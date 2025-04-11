import os
from dotenv import load_dotenv

def main():
    # load_dotenv()
    print(os.getenv("TRADETHING_URL"))

if __name__ == "__main__":
    main()