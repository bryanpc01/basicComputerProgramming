'''
Max Absolute In List Function Lab

Description

Implement function max_abs_val(lst), which returns the maximum absolute value of the elements in list. For example, given a list lst: [-19, -3, 20, -1, 0, -25], the function should return 25. The name of the method should be max_abs_val and the method should take one parameter which is the list of values to test.

Here is an example call to the function:

print(max_abs_val([-19, -3, 20, -1, 0, -25]))
'''


def max_abs_val(lst):
    max_abs_value = calc_abs_value(lst[0])
    for elem in lst:
        abs_value = calc_abs_value(elem)
        if  abs_value > max_abs_value:
            max_abs_value = abs_value
    return max_abs_value


def calc_abs_value(num):
    return num * (-1) if num < 0 else num


print(max_abs_val([-19, -3, 20, -1, 0, -25]))
