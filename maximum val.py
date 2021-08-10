#wap function that returns a maximum value from the list
def maximum_value(b):
    max = b[0]
    for i in b:
        if i > max:
            max = i
    return max

x = [1,2,3,4,5,6,7,8,9,10]
print(maximum_value(x))