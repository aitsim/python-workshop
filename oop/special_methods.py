# Special (Magic/Dunder) Methods like  __init__, __add__, __len__, __repr__ etc.
# double (__) called Dunder “Double Under (Underscores)
# ability to change behaviors\
# The __init__ method for initialization is invoked without any call,
# Commonly used for operator overloading
# These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.

# declare our own string class


class String:
    # magic method to initiate object
    def __init__(self, string):
        self.string = string
    # replace object behavior from <__main__.String object at 0x106359400>  to hello string
    # print our string object

    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # print object location
    print(string1)
    print(string1+" Med")
