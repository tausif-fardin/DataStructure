# Recursion using python.
def openRussianDoll(doll):
    if doll==1:
        print("All dolls are open.")
    else:
        openRussianDoll(doll-1)


openRussianDoll(10)