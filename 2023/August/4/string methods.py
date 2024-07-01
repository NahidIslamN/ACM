#Captilalize String
a="the quick brown fox jump over THE  lazy dog. the quick brown fox jump over the lazy dog."
b=a.capitalize()
print(b)

# upper case
c=a.upper()
print(c)

# lower case
d=a.lower()
print(d)

# get the length of a stirng
e=len(a)
print(e)

# replceing part of a string
x=a.replace("brown","Nahid")
print(x)

# find a text from a string
y=x.find(input("Enter the txt : "))
print(y)
print(x[y:y+5])
