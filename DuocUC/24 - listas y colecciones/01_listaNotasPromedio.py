import os

notas = []

while True:
    try:
        os.system("cls")
        notas.append(float(input("\nIngrese nota: ")))
        prom = sum(notas) / len(notas)
        print(f"""
            Notas:    {notas}
            Prom:     {prom}
            """)
        os.system("pause")
    except ValueError:
        print("Intente de nuevo")
        os.system("pause")
