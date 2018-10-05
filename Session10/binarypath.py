#def binary_search(my_list, x):
    # '''
    # this function adopts bisection/binary search to find the index of a given
    # number in an ordered list
    # my_list: an ordered list of numbers from smallest to largest
    # x: a number
    # returns the index of x if x is in my_list, None if not.
    # '''
    # mid = (len(my_list)/2)
    # for x in my_list:
    #     if my_list[mid] == x:
    #         return [mid]
    #     else:
    #         if x < my_list[mid]:
    #             return binary_search(my_list[:mid],x)
    #         else:
    #             return binary_search(my_list[mid+1:],x)

def binary_search(my_list, x):
    c = len(my_list)//2
    if x > my_list[c]:
       ans = binary_search(my_list[c+1:],x)
       if ans:
          return binary_search(my_list[c+1],x)+c+1
    elif x < my_list[c]:
       return binary_search(my_list[:c],x)
    else:
       return c


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None


#https://stackoverflow.com/questions/9501337/binary-search-algorithm-in-python