def calcularSalud(sueldoBruto):
    return sueldoBruto * 0.07


def calcularPension(sueldoBruto):
    return sueldoBruto * 0.13


def calcularLiquido(sueldoBruto):
    return sueldoBruto - calcularSalud(sueldoBruto) - calcularPension(sueldoBruto)


def imprimirLiquidacion(rut, nombre, bruto, salud, pension, liquido):
    print(f"""
          ----------LIQUIDACIONES----------
          RUT:                  {rut}
          NOMBRE:               {nombre}
          SUELDO BRUTO:         {bruto}
          
          DSCTO SALUD 7%:       {salud}
          DSCTO PENSION 13%:    {pension}
          LIQUIDO A PAGAR:      {liquido}
          """)


def imprimirEmpleado(empleadosList):
    print(f"""
          ----------INFO EMPLEADO----------
          RUT:              {empleado[rut]}
          NOMBRE:           {empleado[nombre]}
          BRUTO             {empleado[bruto]}
          SALUD             {empleado[salud]}
          PENSION           {empleado[pension]}
          LIQUIDO           {empleado[liquido]}
          """)
