

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


main()
