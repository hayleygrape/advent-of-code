import time
import os
from dotenv import load_dotenv, find_dotenv, set_key
from bs4 import BeautifulSoup

def do_something():
    print("did something")
    dotenv.set_key()

def main():
    load_dotenv()
    cur_time = time.time()
    env_time = os.getenv('LAST_REQ')
    print("Current time:", cur_time)
    print("Env time:", env_time)

    # set key
    set_key('.env', 'LAST_REQ', str(cur_time))

    new_env_time = os.getenv('LAST_REQ')
    print("New env time:", new_env_time)

def main2():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    print(f"ORI: {os.getenv('ORI')}")
    set_key('.env', 'ORI', '34')

    load_dotenv(dotenv_path)

    # Verify the change
    print(f"ORI: {os.getenv('ORI')}")


    set_key('.env', 'ORI', '341')

main2()