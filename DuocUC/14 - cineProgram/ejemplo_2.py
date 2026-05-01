import os

#solicitamos tipo de licencia de conducir
#enviamos un mensaje

os.system("cls")

licencia=str(input('''

Ingrese el tipo de licencia de conducir (A1, A2, B2, ...):

''')).strip().upper()

# if licencia=="A1":
#     print("Licencia profesional!!!")
    
# elif licencia == "A2":
#     print("Otro tipo de licencia profesional")
    
# elif licencia =="B2":
#     print("Licencia NO profesional!!!")
    
# else:
#     print("Licencia NO VALIDA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#se puede reescribir con MATCH-CASE    
    
match licencia:
    case "A1":
        print("Licencia profesional!!!")

    case "A2":
        print("Otro tipo de licencia profesional")

    case "B2":
        print("Licencia NO profesional!!!")

    case _:              #este es el "else"
        print("Licencia NO VALIDA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")        