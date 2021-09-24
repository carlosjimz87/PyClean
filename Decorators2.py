def decorator_function(original_function):
    def inner():
        commands = original_function()
        function_name = original_function.__qualname__

        try:
            for command in commands.split(" "):
                print(command)
        except Exception as e:
            print(f'ERROR: {e} in [{function_name}]')
        else:
            print("DONE\n")
    return inner


@decorator_function
def my_function_with_decorator():
    """ ORIGINAL FUNCTION WITH DECORATORS """
    commands = "add stash commit push pull checkout"

    return commands


def my_function():
    """ ORIGINAL FUNCTION """
    commands = "add stash commit push pull checkout"

    try:
        for command in commands.split(" "):
            print(command)
        raise Exception("My Exception")
    except Exception as e:
        print(f'ERROR: {e} in [function_name]')

    print("DONE\n")

    return commands


if __name__ == '__main__':
    # my_function()
    my_function_with_decorator()
