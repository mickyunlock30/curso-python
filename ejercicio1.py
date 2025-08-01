class Estudiante:
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Grado: {self.grado}")

    def evaluar_aprobacion(self, nota):
        if nota >= 3.0:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} no ha aprobado.")

# Crear objeto fuera de la clase
est1 = Estudiante("Carlos", "Décimo")

# Usar métodos
est1.mostrar_info()
nota_final = float(input("Ingrese la nota final del estudiante: "))
est1.evaluar_aprobacion(nota_final)


