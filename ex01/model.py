from decimal import *
from unicodedata import decimal
from config import config
from psycopg2.extensions import AsIs
from datetime import datetime


class OrderM():
    def __init__(self, orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid):
        self.orderid = orderid
        self.customerid = customerid
        self.employeeid = employeeid
        self.orderdate = orderdate
        self.requireddate = requireddate
        self.shippeddate = shippeddate
        self.freight = freight
        self.shipname = shipname
        self.shipaddress = shipaddress
        self.shipcity = shipcity
        self.shipregion = shipregion
        self.shippostalcode = shippostalcode
        self.shipcountry = shipcountry
        self.shipperid = shipperid

    def createOrder(valueList):
        order = OrderM(
            int(valueList[0]),
            int(valueList[1]),
            int(valueList[2]),
            datetime.timestamp(valueList[3]),
            datetime.timestamp(valueList[4]),
            datetime.timestamp(valueList[5]),
            decimal(valueList[6]),
            str(valueList[7]),
            str(valueList[8]),
            str(valueList[9]),
            str(valueList[10]),
            str(valueList[11]),
            str(valueList[12]),
            int(valueList[13])
        )
        return order

    def registerOrder(order):
        query = "INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (order.orderid, order.customerid, order.employeeid, order.orderdate, order.requireddate, order.shippeddate, order.freight,
                  order.shipname, order.shipaddress, order.shipcity, order.shipregion, order.shippostalcode, order.shipcountry, order.shipperid)
        status = config.alterDatabase(config, query, values)
        return status

    def readOrder(orderId):
        query = "SELECT * FROM northwind.orders WHERE orderid = %s;"
        values = config.consultDatabase(config, query, [orderId])
        if(len(values[1]) != 0):
            order = OrderM.createOrder(values[1][0])
            return order
        else:
            return None

    def updateOrder(order):
        query = """UPDATE northwind.orders SET %s = %s WHERE orderid = %s"""
        parameters = ((AsIs(order[1])), int(order[2]), int(order[0]))
        status = config.alterDatabase(config, query, parameters)
        return status

    def deleteOrder(orderId):
        query = "DELETE FROM northwind.orders WHERE orderid = %s;"
        status = config.alterDatabase(config, query, orderId, [orderId])
        return status
