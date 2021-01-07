# Recursion using python.
# Example-1
def openRussianDoll(doll):
    if doll==1:
        print("All dolls are open.")
    else:
        openRussianDoll(doll-1)

openRussianDoll(10)

# Example-2
def recursionMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursionMethod(n-1)
        print(n)


recursionMethod(10)

#Example-3 using Recursive method
def powerOfTwo(n):
    if n==0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power*2

print(powerOfTwo(4))

