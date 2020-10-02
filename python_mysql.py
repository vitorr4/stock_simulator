import mysql.connector

mydb = mysql.connector.connect(host="hastname",
                               port="portname",
                               user="username",
                               password="passwordname",
                               database="store_db")

mycursor = mydb.cursor()


class Server(object):
    def insert(self, brand, model, stock, price):
        sql = "INSERT INTO `stock` (`product_brand`, `product_model`, `product_stock`, `product_price`) VALUES (%s, %s, %s, %s)"
        val = (brand, model, stock, price)
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def update(self, id, brand, model, stock, price):
        if brand != None:
            sql = "UPDATE `stock` SET `product_brand` = %s, `product_model` = %s, `product_stock` = %s, `product_price` = %s WHERE `product_id` = %s"
            val = (brand, model, stock, price, id)
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record is up to date.")
        else:
            sql = "SELECT * FROM `stock` WHERE `product_id` = %s"
            val = (id, )
            mycursor.execute(sql, val)

            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)

    def drop(self, id):
        sql = "DELETE FROM `stock` WHERE `product_id`=%s"
        val = (id, )
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "row deleted.")

    def table(self):
        mycursor.execute("SELECT * FROM `stock`")
        myresult = mycursor.fetchall()

        for product in myresult:
            print(product)
