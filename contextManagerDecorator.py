import contextlib
# this is only for Py3.2+


class manager(contextlib.ContextDecorator):
    def __enter__(self):
        print("do something before")
        return self

    def __exit__(self, *exec):  # it will run even if an exception occurs whilst the main work
        print("do something after")


@manager()
def main_work():
    print("do some work")  # this is the main work


main_work()
