import os


def main():
    print("Starting the development server...")
    os.system("FLASK_APP=app.app:server flask run --reload")


if __name__ == "__main__":
    main()
