# self built max
def max_me(s):
    maximum = s[0]
    for i in s:
        if i > maximum:
            maximum = i
    return maximum
# a short way
    #s.sort()
    #return s[-1]
s = [1, 3, 2, 4, 5]    
print(max_me(s))
