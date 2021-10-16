import string
import random
from datetime import datetime


otrosCaracteres = "áÁäÄåÅàÀâÂéÉêÊëËèÈíÍîÎïÏìÌóñÓÑöÖ¡ôæÔÆòðÒÐøßØþúÞÚçüÇÜœùŒÙÿûÛ"
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()ñ{+*´|°" + otrosCaracteres)
password = []


def generate_random_password():
    length = int(input("Ingrese el largo de la contraseña: "))

    random.shuffle(characters)

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))


generate_random_password()

with open("contrasena.txt", 'a', encoding='utf8') as contrasena:
    contrasena.write(f'dia: {datetime.today()} contreseña: ')
    contrasena.write(''.join(password))
    contrasena.write('\n')
