import argparse
import getpass
import os
import sys
from pathlib import Path

from bcrypt import gensalt, hashpw

DEFAULT_PW_FILENAME = Path("~").expanduser().absolute() / ".pw-learn"
MAX_RETRIES = 3


def prompt_password(prompt):
    return getpass.getpass(prompt).encode("utf-8")


def test_password(hashed_pw):
    for _retry in range(MAX_RETRIES):
        if hashpw(prompt_password("Verify your password: "), hashed_pw) == hashed_pw:
            return True
        print("Passwords do not match; try again.")
    return False


def generate_password(pw_filename):
    hashed_pw = hashpw(prompt_password("Enter your password: "), gensalt())
    for _retry in range(MAX_RETRIES):
        if hashpw(prompt_password("Repeat your password: "), hashed_pw) == hashed_pw:
            with open(pw_filename, "wb") as fp:
                fp.write(hashed_pw)
            print(f"Written to file {pw_filename}")
            break
        print("Passwords do not match; try again.")
    else:
        print(f"Could not match password after {MAX_RETRIES} tries.")


def main():
    pw_filename = os.environ.get("PASSWORD_LEARN_FILENAME", DEFAULT_PW_FILENAME)
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--repeat", default=1, dest="repeats", help="Repeat the password prompt", type=int
    )
    arg_parser.add_argument(
        "--reset",
        default=False,
        action="store_true",
        help="Reset the password in your password file",
    )
    args = arg_parser.parse_args()

    try:
        with open(pw_filename, "rb") as fp:
            hashed_pw = fp.read()
    except IOError:
        hashed_pw = None

    try:
        if hashed_pw is None or args.reset:
            generate_password(pw_filename)
        else:
            for _repeat in range(args.repeats):
                if args.repeats > 1:
                    print(f"Test {_repeat + 1} of {args.repeats}")
                test_password(hashed_pw)
    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt; aborting.")


if __name__ == "__main__":
    main()
