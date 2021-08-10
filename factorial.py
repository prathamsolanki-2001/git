num = input()
no = int(num)
def func(no):
    f=1
    m=1
    for i in range(1,no+1):
        f=f*i

        if i%2==0:
            m=m*i

    return f,m

op=func(no)
print(op)
