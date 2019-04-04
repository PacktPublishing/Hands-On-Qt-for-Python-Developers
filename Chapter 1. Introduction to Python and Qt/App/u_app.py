# -*- coding: utf-8 -*-
from u_tools import UTools                   # Importing of the UTools class.

class UApp(UTools):                          # Inheritance of the UTools.

    def __init__(self):                      # Constructor of the class.
        UTools.__init__(self)                # Call the UTools constructor.
        self.uaps1 = "I am a coder, and I do" 

    def u_app1(self):                        # Concatenation of the strings
        print(self.uaps1 + " " + self.us1)   # from UApp an UTools classes.
        # print self.uaps1 + " " + self.us1  # For python 2.x version.

    def u_app2(self):                        # Function operates strings. 
        uap_list1 = []                       # Creation of the new list.
        i = 0                                # Variable will be used in loop.
        for ul in self.u_list():             # "for" statement, loop for list
            if ul.isalnum():                 # from UTools, checks if digit
                if ul != ".":                # or letter, if not equal to '.'
                    uap_list1.insert(i, ul.lower())
            elif ul == " ":                  # all letters to the lowercase,
                uap_list1.insert(i-i, ul)    # elif statement could be not
                i = 0                        # once, continue the if
                continue                     # statement if the space with
            else:                            # i variable set equal to zero.
                break                        # Breaks the loop if conditions
            i += 1                           # are not acheived, increment.
        print(' '.join(uap_list1))           # Join the list to string.
        # print ' '.join(uap_list1)          # For python 2.x version.


if __name__ == "__main__":                   # If name will not be main. 
    uap = UApp()                             # Class instance.
    uap.u_app1()                             # First function of the class.
    uap.u_app2()                             # Second function of the class.
