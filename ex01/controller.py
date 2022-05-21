from view import View
from model import OrderM


class Controller:
    def main(self):
        option = self.view.main()

        while option != 5:
            if option == 1:
                l = self.view.createOrderData()
                order = OrderM.createOrder(l)
                validCustomerid = OrderM.validateCustomer(order.customerid)
                validEmployeeid = OrderM.validateEmployee(order.employeeid)
                self.view.validateCustomer(validCustomerid)
                self.view.validateEmployee(validEmployeeid)
                if (validCustomerid and validEmployeeid == True):
                    status = OrderM.registerOrder(order)
                    self.view.printStatus(status)
            if option == 2:
                id = self.view.getOrderCod()
                order = OrderM.readOrder(id)
                self.view.printOrder(order)
            if option == 3:
                id = self.view.getOrderCod()
                order = OrderM.readOrder(id)
                self.view.printOrder(order)
                if(order is not None):
                    l = self.view.updateOrderData(id)
                    if (l[1] == 'employeeid'):
                        validEmployeeid = OrderM.validateEmployee(l[2])
                        self.view.validateEmployee(validEmployeeid)
                        if (validEmployeeid == True):
                            status = OrderM.updateOrder(l)
                            self.view.printStatus(status)
                    elif(l[1] == 'customerid'):
                        validCustomerid = OrderM.validateCustomer(l[2])
                        self.view.validateCustomer(validCustomerid)
                        if (validCustomerid == True):
                            status = OrderM.updateOrder(l)
                            self.view.printStatus(status)
                    else:
                        status = OrderM.updateOrder(l)
                        self.view.printStatus(status)
            if option == 4:
                id = self.view.getOrderCod()
                status = OrderM.deleteOrder(id)
                self.view.printStatus(status)

            option = self.view.main()

    def __init__(self):
        self.view = View()


if __name__ == "__main__":
    main = Controller()
    main.main()
