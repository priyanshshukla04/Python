# import random
# rand1 = random.random()   #number between 0 to 1 but not 1
# print(rand1)
# rand2 = random.randint(0,100)
# print(rand2)
# lst = ["Priyansh","Saumya","Aashi","Vansh","Shubhansh","Manya"]
# rand3 = random.choice(lst)
# print(rand3)
#
# #automate whatsapp message
# #install pywhatkit package and import it
# import pywhatkit
# pywhatkit.sendwhatmsg("+917900331733","moti pagal",19,14)
# #pywhatkit.text_to_handwriting("There is no su password to authenticate to root by default; anything ... Terminal you want the privileges of the non-existent user",rgb=[0,0,0])

import time
a = time.gmtime(0)
print(a)
b = time.asctime(a)
print(b)
c = time.localtime()
print(c)
d = time.asctime(time.localtime())
print(d)