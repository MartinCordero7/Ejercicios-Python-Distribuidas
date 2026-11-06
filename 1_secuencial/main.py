import time

def lavar_ropa():
    print("[1/4] 🧺 Iniciando lavado de ropa...")
    time.sleep(1.5)
    print("      ✅ Ropa lavada con éxito.")

def secar_ropa():
    print("[2/4] ☀️ Pasando ropa a la secadora...")
    time.sleep(1.5)
    print("      ✅ Ropa completamente seca.")

def planchar_ropa():
    print("[3/4] 👔 Planchando camisas y pantalones...")
    time.sleep(1.5)
    print("      ✅ Ropa planchada y sin arrugas.")

def guardar_ropa():
    print("[4/4] 🚪 Guardando la ropa en el armario...")
    time.sleep(1.0)
    print("      ✅ Ropa organizada en el armario.")

def main():
    print("=" * 65)
    print("   EJEMPLO 1: EJECUCIÓN SECUENCIAL (PROCESO DE LAVANDERÍA)")
    print("=" * 65)
    print("Descripción de la vida diaria:")
    print("En la lavandería, las tareas deben realizarse estrictamente en orden:")
    print("No puedes secar la ropa antes de lavarla, ni plancharla antes de secarla.")
    print("Cada paso espera a que el anterior termine al 100%.\n")

    inicio = time.time()

    lavar_ropa()
    secar_ropa()
    planchar_ropa()
    guardar_ropa()

    fin = time.time()
    tiempo_total = fin - inicio

    print("\n" + "-" * 65)
    print(f"⏱️ Tiempo total de ejecución secuencial: {tiempo_total:.2f} segundos")
    print("💡 Conclusión: La ejecución secuencial es predecible y segura,")
    print("   pero el tiempo total es la suma de los tiempos de cada tarea.")
    print("=" * 65)

if __name__ == "__main__":
    main()
