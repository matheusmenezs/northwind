from view import View
from model import OrderM


class Controller:
    def main(self):
        option = self.view.main()

        while option != 8:
            if option == 1:
                l = self.view.getOrderData()
                #order = OrderM.createOrder(l)
                status = OrderM.registerOrder('')
                self.view.printStatus(status)
            if option == 2:
                id = self.view.getOrderCod()
                order = OrderM.readOrder(id)
                self.view.printStatus(order)
            if option == 3:
                id = self.view.getOrderCod()
                status = OrderM.deleteOrder(id)
                self.view.printStatus(status)
            if option == 4:
                id = self.view.getOrderCod()
                order = OrderM.readOrder(id)
                self.view.printOrder(order)
                if(order is not None):
                    l = self.view.getOrderDataUpdate(id)
                    status = OrderM.updateOrder(l)
                    self.view.printStatus(status)
            option = self.view.main()

    def __init__(self):
        self.view = View()


if __name__ == "__main__":
    main = Controller()
    main.main()
