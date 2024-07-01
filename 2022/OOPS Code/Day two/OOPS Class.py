# add an new perameter with self and set color and cost with function defination


# Creating a class to set color and set cost and show color and show cost
class Phone:

    # defining the methods how to work to solve the problem
    def set_color(self,color):
        self.color=color

    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        print("Color : ",self.color)
    def show_cost(self):
        print("Cost : ",self.cost)

#Creating an object to acceess the methoods

obj=Phone()
obj.set_color("Blue")
obj.set_cost("25000 tk")











