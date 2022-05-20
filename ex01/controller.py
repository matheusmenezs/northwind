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
            option = self.view.main()

    def __init__(self):
        self.view = View()


if __name__ == "__main__":
    main = Controller()
    main.main()
