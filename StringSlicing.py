str= "Priyansh  is a good boy"
print(str[0:7:2])     #the last value represents the number of chacarter that we want to skip. Default is 1 and 2 means that 1 character will be skipped every time #3 means that 2 elements will be skipped
print(str[::-1])  #using -1 will reverse the string from backwards, -2 will reverse the string and will skip every second element
print(len(str))
print(str.isalnum())  #is alphanumeric i.e.., alpha means spaces and numeric numbers
print(str.isalpha())
print(str.endswith("boy"))
print(str.count("b"))
print(str.capitalize())       #capitalize the first alphabet of string
print(str.find("is"))
print(str.upper())         #will capitalize whole string
print(str.lower())
print(str.replace("b", "c"))