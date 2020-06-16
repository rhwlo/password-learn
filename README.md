This is a simple script to help you practice learning a new password! By
default, the password hash will be written to `.pw-learn` in your home
directory, but you can change the destination by setting the environment
variable `PASSWORD_LEARN_FILENAME`.

To install:

```bash
poetry install
```

To store a `bcrypt`ed password to practice:

```bash
password_learn --reset
```

To practice your password once:

```bash
password_learn
```

To practice it 3 times:

```bash
password_learn --repeat 3
```
