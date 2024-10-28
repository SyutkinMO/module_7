# -------------"Режимы открытия файлов"-------------


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = str(weight)
        self.category = str(category)

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add(self, *products):

        for i in products:
            if i.name not in self.get_products() or self.get_products().count(i.weight) == 0:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name}, {i.weight}, {i.category} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
