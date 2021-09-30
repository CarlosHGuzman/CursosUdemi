# and 0
# not 1
# or 2

age = 40
is_adult = 16 < age < 60
print(is_adult)

user, password = 'root', '123'
is_login = user == 'admin' and password == '123'
print(is_login)

is_not_adult = not(is_adult)
print(is_not_adult)

is_not_allow = not(is_login)
print(is_not_allow)

name = "Paul"
is_student = 'Paul' == name or name  == 'Mark'
print(is_student)