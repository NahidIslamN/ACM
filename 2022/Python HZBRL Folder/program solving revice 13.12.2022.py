#বৃত্তের ক্ষেত্রে ফল নির্ণয়ের প্রোগ্রাম।

#Sart

#Beshardho=int(input("Enter your cercle beshardho : "))
#Pi=3.1416

#Area=Pi*pow(Beshardho,2)

#print(Area)

#ফারেন হাইড তাপমাত্রাকে সেন্টিগ্রেড তাপমাত্রায় রুপান্তর করা।

#F=int(input("Enter Your Farhanhide Temperature : "))
#C = ((F-32)*5)/9
#print("Your Centigrade Temperature is : ",C)

#অসম বাহু ত্রিভূজের ক্ষেত্রফল নির্ণয়ের সুত্র।
#import math
#base1 = int(input("Enter your Traingle Base1 : "))
#base2 = int(input("Enter your Traingle Base2 : "))
#base3 = int(input("Enter your Traingle Base3 : "))
#if (base1+base2)>base3 and  (base3+base2)>base1 and  (base1+base3)>base2:
#    S = (base1+base2+base3)/2
#    Traingle_Area = math.sqrt(S*(S-base1)*(S-base2)*(S-base3))
#    print("Your Traingle Area is : ",Traingle_Area)
#else:
#    print("Traingle is not possible")

#বহু পদির নিশ্চায়ক নির্ণয়ের সুত্র।
#import math
#a=int(input("Enter your value of a : "))
#b=int(input("Enter your value of b : "))
#c=int(input("Enter your value of c : "))
#D = (pow(b,2)-4*a*c)
#if D>0:
#    X1= (-b+(math.sqrt(D)))/(2*a)
#   X2= (-b-(math.sqrt(D)))/(2*a)
#    print("Frist Mul is : ",(X1))
#    print("Frist Mul is : ",(X2))
#elif D==0:
#    X = (-b)/2*a
#    print("Your Mul is : ",(X))
#else:
#    print("Roots is imaginary")

#কোন সংখ্যা নেগেটিভ না প্রজেটিভ তা বের করার প্রোগ্রাম

#A = int(input("Enter your Number : "))
#if A>0:
#    print("The Number Is Possitive")
#elif A<0:
#    print("The Number Is Negative")
#else:
#    print("Zero Is Not Countable")

# কোন সংখ্যা/শব্দ পলিড্রম কি না তা চেক করারি প্রগ্রাম।

#Word = input("Enter Your Word : ")
#RevWord = Word[ ::-1]
#if Word==RevWord:
#    print("The Word is Polydrom")
#else:
#    print("The Word is Not Polydrom")

#কোন সংখ্য জোড় না বিজোর তা বেড় করার প্রগ্রাম।

#Num=int(input("Enter your number : "))
#if Num==0:
#    print("Ziro is not countable")
#elif (Num%2)==0:
#    print("The number is even")
#else:
#    print("The number is odd")

# মার্কস দিয়ে গ্রেড বের করার প্রোগ্রাম:

#M = int(input("Enter the marks of Math : "))
#E = int(input("Enter the marks of English : "))
#B = int(input("Enter the marks of Bangla : "))
#if M>=80 and E>=80 and B>=80:
#    print("You Got A+")
#elif M>=70 and E>=70 and B>=70:
#    print("You Got A")
#elif M>=60 and E>=60 and B>=60:
#    print("You Got A-")
#elif M>=50 and E>=50 and B>=50:
#    print("You Got B")
#elif M>=40 and E>=40 and B>=40:
#    print("You Got C")
#else:
#    print("Sorry You Are fail in the Exam")




    










