def decorator_function(original_function):
    def inner():
        commands = original_function()
        function_name = original_function.__qualname__

        try:
            for command in commands.split(" "):
                print(command)
        except Exception as e:
            print('ERROR: {} in [{}]'.format(e, function_name))
        else:
            print("DONE")
    return inner


@decorator_function
def myfunctionwDecorator():
    """ ORIGINAL FUNCTION WITH DECORATORS """
    commands = "add stash commit push pull checkout"

    return commands


def myfunction():
    """ ORIGINAL FUNCTION """
    commands = "add stash commit push pull checkout"

    try:
        raise Exception("My Exception")
        for command in commands.split(" "):
            print(command)
    except Exception as e:
        print('ERROR: {} in [myfunction]'.format(e))
    else:
        print("DONE")

    return commands


# myfunction()
myfunctionwDecorator()
