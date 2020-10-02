from python_mysql import Server

product = {'Brand': '', 'Model': '', 'Stock': '', 'Price': ''}
newproduct = Server()
id = 0
print('SHOP STOCK')

while True:
    option = int(
        input(
            f'STOCK\n Add new product {" " * 4}[1]\n Change Product Info [2]\n Delete Product {" " * 5}[3]\n Show Products Table [4]\n OPTION: '
        ))

    if (option == 1):
        for key in product.keys():
            product[key] = input(f'{key}: ')

        newproduct.insert(product['Brand'], product['Model'], product['Stock'],
                          product['Price'])

    if (option == 2):
        id = int(
            input('Please, specify which product you want to change [id]: '))
        newproduct.update(id, None, None, None, None)
        for key, value in product.items():
            product[key] = input(f'Field: {key}; former {value}; New Value: ')
        # Add some call some query function from the other file
        newproduct.update(id, product['Brand'], product['Model'],
                          product['Stock'], product['Price'])

    if (option == 3):
        id = int(
            input(
                'Please, specify what porduct do you want to remove from your storage [id]: '
            ))
        # Add some call some query function from the other file
        newproduct.drop(id)
        print(f'The product id {id} was removed from stock.')

    if (option == 4):
        newproduct.table()
