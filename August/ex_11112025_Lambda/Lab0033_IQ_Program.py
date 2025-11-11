# Find the first non repeating character in the string using set


# This is program is written not using set
#Swiss

def non_repeating_char(string):
    for char in string:
        if string.count(char)==1:
            return(char)
    return none

print(non_repeating_char("SWISS"))