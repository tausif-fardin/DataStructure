# binary search implementation
# Performed on ordered elements

def binarySearch(item_list, item):
    start = 0
    end = len(item_list)-1
    found = False
    while(start <= end and not found):

        mid = (start+end)//2

        if item_list[mid] == item:
            found = True
        elif item_list[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return found


print(binarySearch([10, 11, 12, 14, 144], 13))
