# Recursion using python.
def openRussianDoll(doll):
    if doll==1:
        print("All dolls are open.")
    else:
        openRussianDoll(doll-1)

openRussianDoll(10)

def recursionMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursionMethod(n-1)
        print(n)


recursionMethod(10)