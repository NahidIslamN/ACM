class Payment:
    def __init__(self,price):
        self.__final_price=price+price*0.5
    def Show_final_price(self):
        print("final price is : ",self.__final_price)

obj=Payment(10)


