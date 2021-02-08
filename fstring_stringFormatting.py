#1 String Formatting (% Operator)
name = "Priyansh"
s = "My name is %s"%name
print(s)

#2 Using Tuple ()
name1 = "Priyansh"
age = 21
s1 = "%s is %d years old"%(name1,age)
print(s1)

#3 String Formatting (str.format)
random = "This is me Priyansh {} and i live in {} house number {}"
print(random.format("Shukla","Auraiya","93"))

#4 Using f-Strings ( f )
import math
str1 = "Hey!"
str2 = "How are you?"
print(f"Wow, {str1} {str2} {math.cos(90)}")