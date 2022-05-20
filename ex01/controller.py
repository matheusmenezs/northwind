from view import View
from model import OrderM


class Controller:
    def main(self):
        option = self.view.main()

        while option != 8:
            if option == 1:
                l = self.view.getOrderData()
                order = OrderM.createOrder(l)
                status = OrderM.registerOrder(order)
                self.view.printStatus(status)


if __name__ == "__main__":
    main = Controller()
    main.main
