class Manager:
    def __enter__(self):
        print("do something before")

    def __exit__(self, *exec):  # it will run even if an exception occurs whilst the main work
        print("do something after")


if __name__ == '__main__':
    with Manager():
        print("do some work")  # this is the main work
