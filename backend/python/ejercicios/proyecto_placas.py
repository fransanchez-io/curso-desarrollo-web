def precio_instalacion(numero_placas):
     if numero_placas == 6:
        return 5506.61
     elif numero_placas == 7:
        return 6076.86
     elif numero_placas == 8:
        return 6663.64
     elif numero_placas == 9:
        return 6903.31
     elif numero_placas == 10:
        return 7647.11
     elif numero_placas == 11:
        return 7944.63
     elif numero_placas == 12:
        return 8151.24
     else:
        return None
     
print("Bienvenido a Calculador de precio por placa")
print("Indica en numero lo que necesitas.")

try:
   numero_placas=int(input("¿Cuantas placas necesitas?: "))
except ValueError:
   print("Por favor, introduce un numero valido.")
   exit()

precio_total_placas= precio_instalacion(numero_placas)
if precio_total_placas is None:
   print("El número de placas debe estar entre 6 y 12")
   exit()

while True:
    try:
        optimizadores = int(input("¿Cuántos optimizadores necesitas?: "))
        
        
        if optimizadores < 0:
            raise ValueError("El número de optimizadores no puede ser negativo.")  
        elif optimizadores > numero_placas:
            print("El número de optimizadores tiene que ser menor o igual al número de placas.")
        else:
            break  

    except ValueError as e:
        print(f"Error: {e}. Intenta nuevamente.")
precio_por_optimizador=55.0
precio_total_optimizador= optimizadores*precio_por_optimizador

triangulos=input("¿Necesita triangulos? (SI/NO): ").strip().upper()
if triangulos=="SI":
   precio_triangulos=550.0
else:
   precio_triangulos=0.0

descuento=0.0
descuento_aplicar=input("¿Se le aplicara algun descuento? (SI/NO): ").strip().upper()
if descuento_aplicar=="SI":
    while True:  
        try:
            descuento = float(input("¿Cuánto es el descuento?: "))
            if descuento < 0:
                print("El descuento no puede ser negativo. Inténtalo de nuevo.")
            else:
                break  
        except ValueError:
            print("Por favor, introduce un número válido.")
    
      

precio_sin_iva = precio_total_placas + precio_total_optimizador + precio_triangulos
precio_con_descuento= max(precio_sin_iva-descuento, 0)

iva=1.21
precio_con_iva=precio_con_descuento*iva

print("\n --- Detalle del costo ---")
print(f"Precio de las placas: {numero_placas} placas = {precio_total_placas:.2f} €")
print(f"Precio de los optimizadores: {optimizadores} x {precio_por_optimizador:.2f} = {precio_total_optimizador:.2f} €")
print(f"Precio de los triangulos: {precio_triangulos:.2f} €")
if descuento_aplicar == "SI":
   print(f"Descuento aplicado: -{descuento:.2f} €")
else:
   print("No se aplico descuento.")

print("\n --- Total ---")
print(f"Precio total SIN IVA : {precio_con_descuento:.2f} €")
print(f"Precio total CON IVA (21%): {precio_con_iva:.2f} €")