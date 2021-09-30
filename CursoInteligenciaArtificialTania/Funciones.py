#lower
word = 'Hello there'
print(word.lower())
print(word.islower())

#count
print(word.count('e'))# Nos devuelve el numero de la cantidad de veces que encuentre la letra
print(word.find('e')) # Nos ayuda a encontrar la primera posicion del caracter que indiquemos

# format
print('welcome {} to the AI coruse'.format('paul'))
print("{} has {} pets".format('Mary', 4))

# split 
new_word = 'I like extreme sports'
print(new_word.split())
print(new_word.split(' ',2))