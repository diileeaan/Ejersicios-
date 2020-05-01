tarifa = 50
dias = int(input("¿Cuantos dias trabajaste completos trabajaste?(Completo son 8 horas): "))
horas = int(input("¿Cuantas horas trabajaste ademas de los dias?: "))
print("Ganaste: ", ((dias*8)*tarifa)+(tarifa*horas))
