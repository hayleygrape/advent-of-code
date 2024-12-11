import requests
import os
import re
import time
import glob

from bs4 import BeautifulSoup
from dotenv import load_dotenv, set_key

def get_year_and_day(fpath):
    try:
        file_name = fpath.split('/')[-1]
        folder_name = fpath.split('/')[-2]
    except:
        raise Exception("Invalid path given:", fpath)

    year, day = re.search(r'\d+', folder_name).group(0), re.search(r'\d+', file_name).group(0)

    if year is None or day is None:
        raise Exception("Invalid year or day")

    return year, day.lstrip('0')

def get_puzzle_input_raw(year, day):
    URL = f'https://adventofcode.com/{year}/day/{day}/input'
    try:
        token = os.environ['AOC_SESSION']
    except:
        raise Exception("AOC_SESSION token not found in .env")
    
    headers = {'Cookie': 'session='+token}
    r = requests.get(URL, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f"Request failed with status code {r.status_code}")

def get_test_input(year, day):
    try:
        r = requests.get(f'https://adventofcode.com/{year}/day/{day}')
        text = r.text
        soup = BeautifulSoup(text, 'html.parser')
        example_tag = None
        for tag in soup.find_all('p')[::-1]:  # search backwards
            if 'example:' in tag.text:
                example_tag = tag
                try:
                    code_tag = example_tag.find_next_sibling('pre').code
                except:
                    continue
        return code_tag.text
    except Exception as e:
        print("Error finding test case. Saving empty *.txt file instead")
        print("Error msg:\n", e)
        return ""

def save_to_dir(parent_input, day, puzzle_input, is_test=False):
    fname = f'day{int(day):02d}_test.txt' if is_test else f'day{int(day):02d}.txt'
    full_path = os.path.join(parent_input, fname)
    # make sure input is OK
    if puzzle_input is None or puzzle_input.isspace():
        print(f"Error collecting input for {fname.rstrip('.txt')}. Saving blank file.")
        puzzle_input = ''
    else:
        puzzle_input = puzzle_input.rstrip('\n')  # if there are trailing \n's
    
    with open(full_path, 'w') as f:
        f.write(puzzle_input)
    print("Sucessfully wrote to", full_path, "\n\n")

def is_in_timeout():
    if 'LAST_REQ' in os.environ:
        last_req = os.getenv('LAST_REQ')
        elapsed = int(time.time())-int(float(last_req))
        if elapsed < 2*60:
            time_to_wait = 2*60-elapsed
            print(f"Too many requests. Wait {time_to_wait} seconds")
            return True
        else:
            return False
    else:
        raise Exception("LAST_REQ not in environment")

def get_inputs(fpath):
    load_dotenv()
    year, day = get_year_and_day(fpath)

    # ensure there's not already input file in year/day/inputs/${day}.txt
    parent_input = os.path.join(os.path.dirname(fpath), 'inputs')
    files = glob.glob(parent_input + "/*.txt")
    example_input, main_input = False, False
    for file in files:
        name = os.path.basename(file)
        if name == f'day{int(day):02d}_test.txt':
            example_input = True
        if name == f'day{int(day):02d}.txt':
            main_input = True

    if main_input == False or example_input == False:
        timeout = is_in_timeout()

    if main_input == False and timeout == False:
        print("Downloading main input...")
        set_key('.env', 'LAST_REQ', str(int(time.time())))  # update last req time
        puzzle_input = get_puzzle_input_raw(year, day)  # fmt input
        save_to_dir(parent_input, day, puzzle_input)
    elif main_input == False and timeout == True:
        puzzle_input = ''
    else:
        puzzle_input = open(os.path.join(parent_input, f'day{int(day):02d}.txt')).read()

    if example_input == False and timeout == False:
        print("Downloading test input...")
        set_key('.env', 'LAST_REQ', str(int(time.time())))  # update last req time
        test_input = get_test_input(year, day)
        save_to_dir(parent_input, day, test_input, is_test=True)
    elif example_input == False and timeout == True:
        test_input = ''
    else:
        test_input = open(os.path.join(parent_input, f'day{int(day):02d}_test.txt')).read()

    return puzzle_input.split('\n'), test_input.split('\n')

if __name__ == '__main__':
    pass