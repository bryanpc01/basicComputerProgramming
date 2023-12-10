'''
Call Cost Calculator Lab:

Description

Write a program that computes the cost of a long-distance call. The cost of the call is determined according to the following rate schedule:

Any call started between 8:00 A.M. and 6:00 P.M., Monday through Friday, is billed at a rate of $0.40 per minute.
Any call starting before 8:00 A.M. or after 6:00 P.M., Monday through Friday, is charged at a rate of $0.25 per minute.
Any call started on a Saturday or Sunday is charged at a rate of $0.15 per minute.
The input will consist of the day of the week, the time the call started, and the length
of the call in minutes. The output will be the cost of the call.


Notes:

The time is to be input as 4 digit number, representing the time in 24-hour notation, so the time 1:30 P.M. is input as 1330
The day of the week will be read as one of the following three character string: ‘Mon’, ‘Tue’, ‘Wed’, ‘Thr’, ‘Fri’, ‘Sat’ or ‘Sun’
The number of minutes will be input as a positive integer.
For example, an execution could look like this:

Enter the day the call started at: Fri
Enter the time the call started at (hhmm): 2350
Enter the duration of the call (in minutes): 22
This call will cost $5.50
'''

day_call_started = input("Enter the day the call started at (‘Mon’, ‘Tue’, ‘Wed’, ‘Thr’, ‘Fri’, ‘Sat’ or ‘Sun’): ")
time_call_started = int(input("Enter the time the call started at (hhmm): "))
num_of_minutes = int(input("Enter the duration of the call (in minutes): "))

if (day_call_started in ['Sat','Sun']):
    rate = .15
    print(f"The call will cost ${num_of_minutes * rate:.2f} with a rate of ${rate:.2f}")
elif (day_call_started in ['Mon', 'Tue', 'Wed', 'Thr', 'Fri'] and (time_call_started // 100 < 8 or
                                                                   time_call_started // 100 >= 18)):
    rate = .25
    print(f"The call will cost ${num_of_minutes * rate:.2f} with a rate of ${rate:.2f}")
elif (day_call_started in ['Mon', 'Tue', 'Wed', 'Thr', 'Fri'] and (8 <= time_call_started // 100 < 18)):
    rate = .40
    print(f"The call will cost ${num_of_minutes * rate:.2f} with a rate of ${rate:.2f}")
else:
    print("Invalid input")
