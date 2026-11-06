import threading
import time

# Recurso compartido
saldo = 100

# Mecanismo de sincronización (Exclusión Mutua)
lock = threading.Lock()

def retirar(nombre, monto):
    global saldo
    print(f"🏧 [{nombre}] se acerca al cajero automático...")

    # El bloque 'with lock' garantiza que SOLO UN HILO ejecute esta sección crítica a la vez.
    with lock:
        print(f"\n🔒 [{nombre}] ADQUIERE EL LOCK (Cajero ocupado exclusivamente por {nombre})")
        print(f"   💳 [{nombre}] consulta el saldo disponible. Saldo actual: ${saldo}")
        
        if saldo >= monto:
            saldo_actual = saldo
            print(f"   ⏳ [{nombre}] procesando retiro de ${monto} (contando billetes)...")
            time.sleep(1.2)  # Simula tiempo de procesamiento en el cajero
            saldo = saldo_actual - monto
            print(f"   💵 [{nombre}] retiró con éxito ${monto}. Nuevo saldo en cuenta: ${saldo}")
        else:
            print(f"   ❌ [{nombre}]: Transacción denegada. Saldo insuficiente para retirar ${monto}.")
        
        print(f"🔓 [{nombre}] LIBERA EL LOCK (Cajero disponible para el siguiente usuario)\n")

def main():
    print("=" * 70)
    print("   EJEMPLO 3: CONCURRENCIA CON LOCK (CAJERO AUTOMÁTICO BANCARIO)")
    print("=" * 70)
    print("Descripción de la vida diaria:")
    print("Dos titulares de una cuenta conjunta (Juan y María) van a cajeros diferentes")
    print("e intentan retirar $80 al mismo tiempo de una cuenta que solo tiene $100.")
    print("Gracias al 'Lock' (cerrojo/exclusión mutua), la sección crítica de consulta y retiro")
    print("se ejecuta de forma atómica: el primero en llegar retira, y el segundo")
    print("encuentra saldo insuficiente de forma consistente.\n")

    print(f"💰 Saldo inicial en la cuenta: ${saldo}")
    print("👥 Usuarios listos para retirar $80 casi en simultáneo: Juan y María\n")

    hilo1 = threading.Thread(target=retirar, args=("Juan", 80))
    hilo2 = threading.Thread(target=retirar, args=("María", 80))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print("-" * 70)
    print(f"💳 Saldo final verificado en la cuenta: ${saldo}")
    print("💡 Conclusión: El uso de 'Lock' evitó un sobregiro bancario o inconsistencia,")
    print("   garantizando la integridad del saldo en un entorno concurrente.")
    print("=" * 70)

if __name__ == "__main__":
    main()

