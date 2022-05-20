

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
        customerid = input("Type the Custumer Id: ")
        employeeid = input("Type the Employee Id: ")
        orderdate = input("Type the Order Date: ")
        requireddate = input("Type the Required Date: ")
        shippeddate = input("Type the Shipped Date: ")
        freight = input("Type the Freight: ")
        shipname = input("Type the Ship name: ")
        shipaddress = input("Type the Ship Address: ")
        shipcity = input("Type the Ship City: ")
        shipregion = input("Type the Ship Region: ")
        shippostalcode = input("Type the Ship Postal Code: ")
        shipcountry = input("Type the Ship Country: ")
        shipperid = input("Type the Shipper Id: ")
        values = [orderid, customerid, employeeid,
                  orderdate, requireddate, shippeddate,
                  freight, shipname, shipaddress, shipcity,
                  shipregion, shippostalcode, shipcountry, shipperid]
        return values

    def printStatus(status):
        if status:
            print(status)
        else:
            print("Error")
