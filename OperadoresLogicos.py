genero = input("Ingrese su Genero: ")
edad = int(input("Ingrese su edad: "))

if edad <18:
    print(f"Eres {genero} y Menor de edad")
else: 
    print(f"Eres {genero} y Mayor de edad")
if edad >150:
    print("Ya estas en el otro mundo")
elif edad <=0:
    print("no has venido a este mundo")
    
