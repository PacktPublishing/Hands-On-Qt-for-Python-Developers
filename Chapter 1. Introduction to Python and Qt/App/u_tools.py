# -*- coding: utf-8 -*-


class UTools():                               # Creation of the Python class.

    def __init__(self):                       # Constructor of the class.
        self.us1 = "Application with Python."

    def u_list(self):                         # Function - converts string
        self.ul1 = []                         # to list, new list, "for"
        for s in self.us1:                    # statement - creates the loop,
            self.ul1.append(s)                # append to the new list
        return self.ul1                       # characters of the string.


if __name__ == "__main__":                    # If file will start from
    ut = UTools()                             # terminal/cmd, etc., create
    print(ut.us1)                             # instance of the class, print
    # print ut.us1  # for  python 2.x         # string, and call function
    ut.u_list()                               # of the UTools class.
