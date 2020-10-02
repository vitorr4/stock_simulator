# stock_simulator

# ABOUT

The general idea was to create a simple application that used a MySQL database. The best solution was to use python to create the user side,
because python is a particularly simple language that enabled me to save a lot of time on the user side thou focusing mainly on the database.
I decided that I wanted to simulate a store’s stock. Probably because a product stock is something easy to conceive and, relatively, easy to work with.

The database was created using MAMP [link here]. MAMP is a platform that serves as a medium to deal with MySQL and Apache servers.
There are many options when it comes to managing MySQL servers, but MAMP is tool fairly easy to use. 

# database structure

The database structure is pretty simple; it contains a few informations (fields) about a given product. Those info are: 
product id: a number that marks each product, each product has its own and unique id;
product brand: the name of the company that manufactures the product (e.g Apple)
product  model:  this is much like the product’s name (e.g Iphone X)
product stock: how many many models are in stock
product price: the selling price for 1 unity

# user and server sides

On the user side, it shows a menu with four options (1, 2, 3 and 4), each of these options corresponds to a function on the server side.
These four options are responsible for adding, changing and deleting products in stock and there’s an option responsible for displaying all products in stock.

# HOW TO USE

The file 'store_db.sql' is the database itself. You should import it to your host first.
Basically, you just need to run 'client_menu.py' from cmd or any ide you use. 

