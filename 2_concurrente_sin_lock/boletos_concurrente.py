import threading
import time

# Recurso compartido sin protección
boletos_disponibles = 3
ventas_exitosas = 0

def comprar_boleto(nombre):
    global boletos_disponibles, ventas_exitosas
    print(f"🎟️ [{nombre}] consulta disponibilidad...")

    # CONDICIÓN DE CARRERA:
    # Varios hilos leen el mismo valor de 'boletos_disponibles' antes de que cualquiera lo actualice.
    boletos_actuales = boletos_disponibles

    if boletos_actuales > 0:
        print(f"   🔎 [{nombre}] ve que quedan {boletos_actuales} boletos e inicia proceso de pago...")
        time.sleep(0.5)  # Simula el tiempo que tarda la pasarela de pagos

        # Ambos hilos descuentan sobre la variable global sin exclusión mutua
        boletos_disponibles = boletos_disponibles - 1
        ventas_exitosas += 1
        print(f"   🎉 [{nombre}] compró su boleto con éxito. (Quedan según sistema: {boletos_disponibles})")
    else:
        print(f"   ❌ [{nombre}] lo intentó, pero no quedan boletos disponibles.")

def main():
    global boletos_disponibles, ventas_exitosas

    print("=" * 70)
    print("   EJEMPLO 2: CONCURRENCIA SIN LOCK (VENTA DE BOLETOS DE CONCIERTO)")
    print("=" * 70)
    print("Descripción de la vida diaria:")
    print("Una boletería en línea tiene solo 3 boletos para un concierto popular.")
    print("5 personas intentan comprar al mismo milisegundo.")
    print("Al no existir un mecanismo de bloqueo (Lock), ocurre una condición de carrera (Race Condition)")
    print("y sobreventa (overbooking).\n")

    compradores = ["Carlos", "Sofía", "Andrés", "Valentina", "Mateo"]
    hilos = []

    print(f"🎫 Boletos iniciales disponibles: {boletos_disponibles}")
    print(f"👥 Clientes concurrentes: {', '.join(compradores)}\n")

    # Iniciar hilos casi al mismo tiempo
    for nombre in compradores:
        hilo = threading.Thread(target=comprar_boleto, args=(nombre,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos terminen
    for hilo in hilos:
        hilo.join()

    print("\n" + "-" * 70)
    print("📊 RESULTADO FINAL DE LA BOLETERÍA:")
    print(f"   - Boletos iniciales puestos a la venta: 3")
    print(f"   - Compras aprobadas: {ventas_exitosas}")
    print(f"   - Boletos restantes registrados: {boletos_disponibles}")
    
    if ventas_exitosas > 3 or boletos_disponibles < 0:
        print("\n⚠️ ¡PROBLEMA DETECTADO (SOBREVENTA)!:")
        print("   Se vendieron más boletos de los que existían porque múltiples clientes")
        print("   consultaron y modificaron el inventario a la vez sin sincronización.")
    print("=" * 70)

if __name__ == "__main__":
    main()

