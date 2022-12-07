thisislist01 = ['carro', 'moto', ' barco']
thisislist01.append('helicoptero')

new_list = ['avião', 'trator']
new_list.insert(0, 'carroça')

thisislist01.extend(new_list)

new_tuple = ('cadeira de rodas', 'bicicleta')

thisislist01.extend(new_tuple)

print(thisislist01, "\n")

new_list_01 = ['mostarda', 'catchup', 'maionese']
new_list_01.append('molho verde')
new_list_01.insert(2, 'molho de alho')

new_list_02 = ['barbecue', 'azeite']
new_list_01.extend(new_list_02)

print(new_list_01)
