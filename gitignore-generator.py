#!/usr/bin/python3

import requests, argparse

def file_write(content):
    try:
        with open('.gitignore', 'w') as file:
            file.write(str(content))
            file.close()

            print('DEBUG: File was writted')
    except: print('ERROR: File writing error!')

def request_gitignoreio(need):
    url = 'https://www.gitignore.io/api/'

    try:
        response = requests.get(url + need)
        response.close()
        
        print('DEBUG: Successful request to gitignore.io')

        return response.text
    except: print('ERROR: Not successful request to gitignore.io!')

def main(need):
    content = request_gitignoreio(need)
    file_write(content)

    print('\nDEBUG: The program ended')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--need')
    args = parser.parse_args()
    
    if args.need: main(need=args.need)
    else: print('\nYou first find out what you need!\n')
