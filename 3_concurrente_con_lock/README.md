# Actividad 3: Concurrencia con Sincronización (Hilos con Lock)

## 📌 Enlace de la Carpeta en GitHub
[Ver carpeta en el Repositorio](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/3_concurrente_con_lock)

---

## 📖 Descripción del Ejemplo de la Vida Real: *Cajero Automático Bancario* 🏧

Imaginemos una cuenta bancaria compartida entre dos personas (Juan y María) con un saldo inicial de **$100**:
1. Ambos usuarios van a cajeros automáticos diferentes en la misma ciudad e intentan retirar **$80** exactamente al mismo segundo.
2. Para evitar que ambos retiren dinero simultáneamente y dejen la cuenta en saldo negativo o con sobregiro, el sistema bancario implementa un **cerrojo de exclusión mutua (`Lock`)**.
3. **Flujo de la transacción:**
   - Juan entra a la sección crítica y adquiere el `Lock`.
   - El cajero de Juan consulta el saldo ($100), descuenta $80 y entrega el dinero. El saldo actualizado pasa a ser $20.
   - Juan libera el `Lock`.
   - María adquiere el `Lock` inmediatamente después, consulta el saldo actual ($20) y el sistema rechaza la operación por **saldo insuficiente**.
4. **Resultado:** Se respeta la integridad financiera de la cuenta bancaria.

### 🧠 Concepto Técnico
- **Exclusión Mutua (`threading.Lock`):** Garantiza que solo un hilo a la vez pueda ejecutar la **sección crítica** (el bloque de código donde se lee y actualiza la variable compartida `saldo`).
- **Context Manager (`with lock:`):** En Python, asegura que el cerrojo sea adquirido (`acquire`) al entrar y liberado (`release`) de forma segura al salir, incluso si ocurre una excepción.

---

## 🐳 Cómo Ejecutar con Docker Compose

Asegúrate de estar ubicado dentro de esta carpeta:

```bash
cd 3_concurrente_con_lock
```

### 1. Construir y ejecutar el contenedor
```bash
docker compose up --build
```
*(o con la sintaxis clásica de Docker: `docker-compose up --build`)*

### 2. Salida esperada en consola
```text
======================================================================
   EJEMPLO 3: CONCURRENCIA CON LOCK (CAJERO AUTOMÁTICO BANCARIO)
======================================================================
💰 Saldo inicial en la cuenta: $100
👥 Usuarios listos para retirar $80 casi en simultáneo: Juan y María

🏧 [Juan] se acerca al cajero automático...
🏧 [María] se acerca al cajero automático...

🔒 [Juan] ADQUIERE EL LOCK (Cajero ocupado exclusivamente por Juan)
   💳 [Juan] consulta el saldo disponible. Saldo actual: $100
   ⏳ [Juan] procesando retiro de $80 (contando billetes)...
   💵 [Juan] retiró con éxito $80. Nuevo saldo en cuenta: $20
🔓 [Juan] LIBERA EL LOCK (Cajero disponible para el siguiente usuario)

🔒 [María] ADQUIERE EL LOCK (Cajero ocupado exclusivamente por María)
   💳 [María] consulta el saldo disponible. Saldo actual: $20
   ❌ [María]: Transacción denegada. Saldo insuficiente para retirar $80.
🔓 [María] LIBERA EL LOCK (Cajero disponible para el siguiente usuario)

----------------------------------------------------------------------
💳 Saldo final verificado en la cuenta: $20
💡 Conclusión: El uso de 'Lock' evitó un sobregiro bancario o inconsistencia,
   garantizando la integridad del saldo en un entorno concurrente.
======================================================================
```

### 3. Detener y limpiar el contenedor
```bash
docker compose down
```
