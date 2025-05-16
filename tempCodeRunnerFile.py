test = OnlineSalesRegisterCollector()
#print(test.add_item_to_cheque(''))
#print(test.add_item_to_cheque('apple'))
#print(test.add_item_to_cheque('book'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))
print(test.add_item_to_cheque('кола'))

print(test.add_item_to_cheque('молоко'))
#print(test.add_item_to_cheque('молоко'))
#print(test.add_item_to_cheque('молоко'))



#print(test.add_item_to_cheque('12345678901234567890123456789012345678901'))

#print(test.number_items)

#print(test.delete_item_from_check('тарелка'))
#print(test.name_items, test.number_items)
#print(test.delete_item_from_check('чипсы'))
print(test.name_items, test.number_items)
print(test.check_amount())
print(test.twenty_percent_tax_calculation())
print(test.ten_percent_tax_calculation())
print(test.total_tax())
test.get_telephone_number(1234567890)