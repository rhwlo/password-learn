#!vendor/bin/python

import getpass
import os
import os.path
import sys

from bcrypt import gensalt, hashpw

DEFAULT_PW_FILENAME = os.path.join(os.environ['HOME'], '.pw-learn')
MAX_RETRIES = 3

def prompt_password(prompt):
    return getpass.getpass(prompt).encode('utf-8')

def test_password(hashed_pw):
    for _retry in range(MAX_RETRIES):
        if hashpw(prompt_password('Verify your password: '), hashed_pw) == hashed_pw:
            return True
        print('Passwords do not match; try again.')
    return False

def generate_password(pw_filename):
    hashed_pw = hashpw(prompt_password('Enter your password: '), gensalt())
    for _retry in range(MAX_RETRIES):
        if hashpw(prompt_password('Repeat your password: '), hashed_pw) == hashed_pw:
            with open(pw_filename, 'wb') as fp:
                fp.write(hashed_pw)
            print('Written to file {}'.format(pw_filename))
            return True
        print('Passwords do not match; try again.')
    print('Could not match password after {} tries.'.format(MAX_RETRIES))

if __name__ == '__main__':
    pw_filename = os.environ.get('PASSWORD_LEARN_FILENAME', DEFAULT_PW_FILENAME)
    try:
        with open(pw_filename, 'rb') as fp:
            hashed_pw = fp.read()
    except IOError:
        hashed_pw = None

    try:
        argument = sys.argv[1]
    except IndexError:
        argument = None

    try:
        if hashed_pw is None or argument == 'reset':
            generate_password(pw_filename)
        else:
            test_password(hashed_pw)
    except KeyboardInterrupt:
        print('Caught keyboard interrupt; aborting.')

