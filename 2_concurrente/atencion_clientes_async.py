import asyncio
import time

async def atender_cliente(nombre, tiempo_espera, pedido):
    print(f"☕ [Barista] Iniciando atención a {nombre} (Pedido: {pedido})...")
    print(f"   ⏳ [{nombre}] Esperando preparación de {tiempo_espera}s (el barista atiende a otros mientras)...")
    await asyncio.sleep(tiempo_espera)
    print(f"   ✅ [{nombre}] Pedido listo y entregado.")

async def main():
    print("=" * 70)
    print("   EJEMPLO 2: CONCURRENCIA CON ASYNCIO (ATENCIÓN EN CAFETERÍA)")
    print("=" * 70)
    print("Descripción de la vida diaria:")
    print("En una cafetería con un solo cajero/barista, este toma la orden de Juan,")
    print("pone la máquina de café a trabajar y, mientras el café se prepara,")
    print("atiende inmediatamente a Pedro y luego a María.")
    print("El barista no se queda congelado esperando; maneja las tareas concurrentemente.")
    print("=" * 70 + "\n")

    inicio = time.perf_counter()

    # asyncio.gather ejecuta las corutinas de forma concurrente en el Event Loop
    await asyncio.gather(
        atender_cliente("Juan", 2, "Café Americano"),
        atender_cliente("Pedro", 2, "Capuchino"),
        atender_cliente("María", 2, "Té Matcha"),
    )

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print("\n" + "-" * 70)
    print(f"⏱️ Tiempo total concurrente: {tiempo_total:.2f} segundos")
    print("💡 Conclusión:")
    print("   De forma secuencial habría tardado 6 segundos (2s + 2s + 2s).")
    print("   Gracias a la concurrencia con 'asyncio', los 3 clientes son atendidos")
    print("   en paralelo sobre el mismo hilo en apenas ~2 segundos.")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(main())

