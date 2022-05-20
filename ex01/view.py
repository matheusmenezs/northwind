from datetime import datetime


class View():
    def main(self):
        return self.menu()

    def menu(self):
        print("-----Menu-----")
        print("1.Create Order")
        print("2.Read Order")
        print("3.Update Order")
        print("4.Delete Order")
        print("5.Exit")
        option = int(input("Type an option: "))
        return option

    def getOrderData(self):
        orderid = input("Type the Order id: ")

        # return values

    def printStatus(self, status):
        if status == 'Sucess':
            print("Order registered successfully")
        else:
            print(status)
