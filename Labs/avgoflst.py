'''
Average of List Function Lab：

Description

Implement function avg_val(lst), which returns the average value of the elements in list. For example, given a list lst: [19, 2, 20, 1, 0, 18], the function should return 10. The name of the method should be avg_val and the method should take one parameter which is the list of values to test.

Here is an example call to the function:

print(avg_val([19, 2, 20, 1, 0, 18]))
'''


def avg_val(lst):
    return sum(lst) / len(lst)


print(avg_val([19, 2, 20, 1, 0, 18]))
