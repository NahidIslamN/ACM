# Write a python program to greed someone name input
'''
name=input("enter your name : ")
x=f"Wellcome MR. {name} Islam"
print(x)
'''
# Write triple quite stirng and change the place ment of stirng
latter='''
Dear Mahid
Hope your are well. I am well too by the grate almighty of allah.I fall in love with someone and can't tell
your for some reson sorry re dsto....

your friend
Nahid Islam'''

x=input("Enter your friend Name : ")
y=input("Enter your Name : ")
latter.replace("Mahid",x)
latter.replace("Nahid Islam",y)
print(latter)

