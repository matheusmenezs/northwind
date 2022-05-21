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

    def createOrderData(self):
        orderid = input("Type the Order id: ")
        customerid = input("Type the Custumer Id: ")
        employeeid = input("Type the Employee Id: ")
        orderdate = input("Type the Order Date (YYYY-MM-DD): ")
        requireddate = input("Type the Required Date (YYYY-MM-DD): ")
        shippeddate = input("Type the Shipped Date (YYYY-MM-DD): ")
        freight = input("Type the Freight: ")
        shipname = input("Type the Ship name: ")
        shipaddress = input("Type the Ship Address: ")
        shipcity = input("Type the Ship City: ")
        shipregion = input("Type the Ship Region: ")
        shippostalcode = input("Type the Ship Postal Code: ")
        shipcountry = input("Type the Ship Country: ")
        shipperid = input("Type the Shipper Id: ")
        year, month, day = map(int, orderdate.split('-'))
        orderdate = datetime(year, month, day)
        year, month, day = map(int, requireddate.split('-'))
        requireddate = datetime(year, month, day)
        year, month, day = map(int, shippeddate.split('-'))
        shippeddate = datetime(year, month, day)
        values = [orderid, customerid, employeeid,
                  orderdate, requireddate, shippeddate,
                  freight, shipname, shipaddress, shipcity,
                  shipregion, shippostalcode, shipcountry, shipperid]
        return values

    def getOrderCod(self):
        orderid = int(input("Type the Order id: "))
        return orderid

    def updateOrderData(self, orderid):
        attributes = {1: 'customerid', 2: 'employeeid', 3: 'orderdate', 4: 'requireddate', 5: 'shippeddate', 6: 'freight',
                      7: 'shipname', 8: 'shipaddress', 9: 'shipcity', 10: 'shipregion', 11: 'shippostalcode', 12: 'shipcountry', 13: 'shipperid'}
        print("Type the atribute to update: ")
        print("1: Customer identifier")
        print("2: Employee identifier")
        print("3: Order date")
        print("4: Required date")
        print("5: Shipped date")
        print("6: Freight")
        print("7: Ship name")
        print("8: Ship address")
        print("9: Ship city")
        print("10: Ship region")
        print("11: Ship postal code")
        print("12: Ship country")
        print("13: Shipper id")
        option = int(input("Type an option: "))
        value = input("Type the new value: ")
        if (option == 2 or option == 13):
            value = int(value)
        elif (option == 3 or option == 4 or option == 5):
            year, month, day = map(int, value.split('-'))
            value = datetime(year, month, day)
        elif (option == 6):
            value = float(value)
        else:
            value = str(value)
        return (orderid, attributes[option], value)

    def printOrder(self, order):
        if (order is not None):
            print("Order id: ", order.orderid)
            print("Customer id: ", order.customerid)
            print("Employee id: ", order.employeeid)
            print("Order date: ", order.orderdate)
            print("Required date: ", order.requireddate)
            print("Shipped date: ", order.shippeddate)
            print("Freight: ", order.freight)
            print("Ship name: ", order.shipname)
            print("Ship address: ", order.shipaddress)
            print("Ship city: ", order.shipcity)
            print("Ship region: ", order.shipregion)
            print("Ship postal code: ", order.shippostalcode)
            print("Ship country: ", order.shipcountry)
            print("Shipper id: ", order.shipperid)
        else:
            print("Order not found")

    def printStatus(self, status):
        if status == 'Sucess':
            print("Order registered successfully")
        else:
            print(status)

    def validateCustomer(self, customerid):
        if(customerid == True):
            return True
        else:
            return print("Error: Customer not found")

    def validateEmployee(self, employeeid):
        if(employeeid == True):
            return True
        else:
            return print("Error: Employee not found")
