import re


def num_there(s):
    return any(i.isdigit() for i in s)


def special_there(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(string) is None:
        return False
    else:
        return True
