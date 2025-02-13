# Example file for Programming Foundations: Algorithms by Joe Marini
# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    for i in range(len(itemlist)):
        if item == itemlist[i]:
            return i
    return None

print(find_item(87, items))
print(find_item(250, items))

#linear time complexity: worst case if the list has million elements and the item is at the end of the list, it may take million iteration to find it.