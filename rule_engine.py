"""
Write a simple rules engine in Python.

It consists of a daemon script that accepts a keyword and a record
associated with the keyword as input in a loop, on receiving an input it calls
a list of functions that are mapped to the keyword and prints the result.

The mapping of keyword with target functions can be fed at the startup of
the script.

Test mapping (keyword -> list of functions):
{
    'sum': ['log', 'sum'],
    'sqrt': ['log', 'square_root'],
    'division': ['log', 'square_root'],
    'greet': ['greet_good_x']
}

Sample input:
    division 128 16
    division 67 0
    greet John Doe

Expected output:
    8
    integer division or modulo by zero
    Good afternoon John Doe!

Use exception handling. Create a custom exception called ActionException which
 will be raised by actions (functions).

ActionException will have the reference of the function that raised an error
and the error message.

The main script will catch these exception and print it on stdout.


"""


set_of_rule = {
    'sum': ['log', 'sum'],
    'sqrt': ['log', 'square_root'],
    'division': ['log', 'division'],
    'greet': ['greet_good_x']
}


class ActionException(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


def sum(a, b):
    return "Sum {} + {} = {}".format(a, b, int(a) + int(b))


def greet_good_x(a, b):
    return "Good afternoon {} {}!".format(a, b)


def division(a, b):
    return "Divison {} / {} = {}".format(a, b, int(a) / int(b))


def square_root(a, b):
    return "Sqrt {} ** {} = {}".format(
        a, 1 / float(b), float(a) ** (1 / float(b))
    )


def main():
    while True:
        input_value = raw_input(
            "Enter input in following format:\nkeyword input1 input2 (space seperated):\n"
        ).split(' ')
        if len(input_value) != 3:
            raise ActionException("keyword input1 input2 (space seperated)")
        keyword, a, b = input_value
        if not set_of_rule.get(keyword):
            raise ActionException("Enter wrong keyword")
        print eval(set_of_rule[keyword][-1] + "(a,b)")
        print "----------------------------------"


if __name__ == "__main__":
    main()
