#pedimos los datos de entrada

user = input("Ingrese su Usuario: ")
password = int(input("Ingrese su Password: "))

#validamos la clave y user de admin 

if user == "admin" and password == 1234 :
    print("Bienvenido al Sistema")
else:
    print("ingrese su contraseña y usuario valido")    