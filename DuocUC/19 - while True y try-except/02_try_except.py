while True:
    try:
        edad = int(input("Ingrese edad: "))

        print(f"La edad es {edad}, y es válida")
    except ValueError:
        print("\n Error: debe ser un numero!!")
