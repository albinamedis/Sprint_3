import datetime

class OnlineSalesRegisterCollector():

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    @property
    def item_price(self):
        return self.__item_price

    @property
    def tax_rate(self):
        return self.__tax_rate

    @number_items.setter
    def number_items(self, kol):
        if kol>=0:
            self.__number_items = kol

#Добавить товар в чек    
    def add_item_to_cheque(self, name):
        try:
            if 0 < len(name) <=40:
                if name in list(self.item_price.keys()):
                    self.name_items.append(name)
                    self.number_items = self.number_items + 1
                    result = self.name_items
                else:
                    raise NameError
            else:
                raise ValueError
        except ValueError:
            result = 'Нельзя добавить товар, если в его названии нет символов или их больше 40'
        except NameError:
            result = 'Позиция отсутствует в товарном справочнике'
        return result

#Удалить товар из чека
    def delete_item_from_check(self, name):
        try:
            if name not in self.name_items:
                raise NameError
            else:
                self.name_items.remove(name)
                self.number_items = self.number_items - 1
                result = self.name_items
        except NameError:
            result = 'Позиция отсутствует в чеке'
        return result    

#Посчитать общую стоимость товаров
    def check_amount(self):
        total = []
        sum_check = 0
        for tovar in self.name_items:
            for key in self.item_price.keys():
                if tovar == key:
                    total.append(self.item_price[tovar])
        for i in total:
            sum_check = sum_check + i
        if len(total) > 10:
            sum_check = sum_check - (sum_check * 0.1)    
        return sum_check

#Вычисление НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        sum_check = 0
        for i in self.name_items:
            for key,value in self.tax_rate.items():
                if i==key and value == 20:
                    twenty_percent_tax.append(key)
                    total.append(self.item_price[key])
                    sum_check = sum_check + self.item_price[key]
        if len(self.name_items) > 10:
            nds = (sum_check - (sum_check * 0.1)) * 0.2
        else:
            nds = sum_check * 0.2
        return nds

#Вычисление НДС для товаров со ставкой 20%    
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        sum_check = 0
        for i in self.name_items:
            for key,value in self.tax_rate.items():
                if i==key and value == 10:
                    ten_percent_tax.append(key)
                    total.append(self.item_price[key])
                    sum_check = sum_check + self.item_price[key]
        if len(self.name_items) > 10:
            nds = (sum_check - (sum_check * 0.1)) * 0.1
        else:
            nds = sum_check * 0.1
        return nds

#Общая сумму налогов
    def total_tax(self):
        all_nds = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return all_nds

#номер телефона покупателя
    def get_telephone_number(self, telephone_number):
        try:
            if type(telephone_number).__name__ != int:
                raise ValueError('Необходимо ввести цифры')
            elif len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            else:
                return (f'+7{telephone_number}')
        except ValueError as e:
            print(e)