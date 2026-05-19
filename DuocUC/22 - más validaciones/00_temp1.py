import os

email = ""

while True:
    email = str(input("Ingrese email: ")).strip()

    # evalúa si NO se cumple la primera condición
    if not (len(email) >= 3):
        print("ERROR: el email debe tener al menos 3 carácteres. ")

    # si no se cumple la segunda condición
    elif not ("@" in email):
        print("ERROR: el email debe contener una @ para ser válido. ")

    # si se cumplen ambas condiciones:
    elif (len(email >= 3)) and ("@" in email):
        break

    # if len(email) >= 3 and "@" in email:
    #     break
    # else:
    #     print("ERRROR: email inválido!!!!")

print("Email almacenado exitosamente!!!")
