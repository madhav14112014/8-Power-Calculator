string1=input("Please enter your own string: ")
string2=("")
for i in string1:
    string2=i+string2
print("The original string is:",string1)
print("The reversed string is:",string2)