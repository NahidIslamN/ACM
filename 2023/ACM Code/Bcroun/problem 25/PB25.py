Co=int(input())
QU=int(input())
Product_List=[1,2,5,4,5]
for i in Product_List:
        if i==1:
            Pay=QU*4.00
        elif i==2:
            Pay=QU*4.50
        elif i==3:
            Pay=QU*5.00
        elif i==4:
            Pay=QU*2.00
        elif i==5:
            Pay=QU*1.50
print(Pay)

