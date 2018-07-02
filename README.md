This is a simple script to help you practice learning a new password!

To setup:

    virtualenv -p `which python3` vendor
    vendor/bin/pip install -r requirements.txt

To set a password (or practice a password you’ve set) in `~/.pw-learn`:

    ./password_learn.py

To set a password (or practice a password you’ve set) in `/foo/bar/example.txt`:

    PASSWORD_LEARN_FILENAME=/foo/bar/example.txt ./password_learn.py

To reset a password:

    ./password_learn.py reset
    # or
    PASSWORD_LEARN_FILENAME=/foo/bar/example.txt ./password_learn.py reset

