# from os import environ
# from dotenv import load_dotenv
# from os.path import join, dirname
from App import App

if __name__ == '__main__':
    app = App()

    # dotenv_path = join(dirname(__file__), '.env')
    # load_dotenv(dotenv_path)
    # print(environ.get('PASSWORD', None))

    while True:
        if not app.getValid():
            break
        else:
            app.lobby()