from getpass import getpass
import hashlib

username = input("User:")
password = (getpass("Pass:"))
password = hashlib.md5(password.encode())
digest = password.hexdigest()
print(f'User: {username} and Pass: {digest}')
