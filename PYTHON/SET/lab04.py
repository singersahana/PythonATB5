# find the first non-repeating character in a string using sets
# swiss --> s -- repeating one
# w --> answer

def checking_first_non_repeating_char(string):
    for char in string:
        if string.count(char)==1:
            return char
    return None
print(checking_first_non_repeating_char("swiss"))
print(checking_first_non_repeating_char("apple"))
print(checking_first_non_repeating_char("sahana"))