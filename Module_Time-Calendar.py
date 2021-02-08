import time
k = 0
initial_time1 = time.time()
while(k<=20):
    print("Hello")
    time.sleep(1)   #makes it sleep for 1 second
    k += 1
print("While loop execution time is: ",time.time()-initial_time1)
initial_time2 = time.time()
for i in range(20):
    print("Hello")
print("For loop execution time is: ",time.time()-initial_time2)

#to print time is readable format
readable_time = time.asctime(time.localtime(time.time()))
print(readable_time)

import calendar
year_leap = calendar.isleap(2021)
print(year_leap)
month =  calendar.monthcalendar(2021,1)
print(month)
calendar = calendar.calendar(2021,2,1,6)
print(calendar)

