# Actividad 2: Concurrencia sin Sincronización (Condición de Carrera)

## 📌 Enlace de la Carpeta en GitHub
[Ver carpeta en el Repositorio](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/2_concurrente_sin_lock)

---

## 📖 Descripción del Ejemplo de la Vida Real: *Venta de Boletos de Concierto* 🎟️

Imaginemos una boletería virtual donde solo quedan **3 boletos disponibles** para un concierto muy esperado. En el mismo milisegundo, **5 personas** (Carlos, Sofía, Andrés, Valentina y Mateo) dan clic en "Comprar":

1. Cada usuario consulta el sistema y lee que aún quedan 3 boletos (`boletos > 0`).
2. Cada usuario es redirigido a la pasarela de pago (tarda una fracción de segundo).
3. Como **no existe ningún bloqueo (Lock)** en la base de datos o memoria compartida, el sistema aprueba la compra de los 5 usuarios y descuenta el inventario de forma descontrolada.
4. **Resultado:** ¡Sobreventa (overbooking)! Se vendieron 5 boletos teniendo solo 3, y el stock final queda en valores negativos o inconsistentes.

### 🧠 Concepto Técnico
- **Concurrencia con Hilos (`threading.Thread`):** Múltiples flujos de ejecución se ejecutan de manera intercalada o simultánea.
- **Condición de Carrera (Race Condition):** Ocurre cuando dos o más hilos acceden a un recurso compartido (`boletos_disponibles`) y al menos uno lo modifica sin sincronización. El resultado final depende del orden arbitrario en que la CPU planifica los hilos.

---

## 🐳 Cómo Ejecutar con Docker Compose

Asegúrate de estar ubicado dentro de esta carpeta:

```bash
cd 2_concurrente_sin_lock
```

### 1. Construir y ejecutar el contenedor
```bash
docker compose up --build
```
*(o con la sintaxis clásica de Docker: `docker-compose up --build`)*

### 2. Salida esperada en consola
```text
======================================================================
   EJEMPLO 2: CONCURRENCIA SIN LOCK (VENTA DE BOLETOS DE CONCIERTO)
======================================================================
🎫 Boletos iniciales disponibles: 3
👥 Clientes concurrentes: Carlos, Sofía, Andrés, Valentina, Mateo

🎟️ [Carlos] consulta disponibilidad...
   🔎 [Carlos] ve que quedan 3 boletos e inicia proceso de pago...
🎟️ [Sofía] consulta disponibilidad...
   🔎 [Sofía] ve que quedan 3 boletos e inicia proceso de pago...
...
----------------------------------------------------------------------
📊 RESULTADO FINAL DE LA BOLETERÍA:
   - Boletos iniciales puestos a la venta: 3
   - Compras aprobadas: 5
   - Boletos restantes registrados: -2

⚠️ ¡PROBLEMA DETECTADO (SOBREVENTA)!:
   Se vendieron más boletos de los que existían porque múltiples clientes
   consultaron y modificaron el inventario a la vez sin sincronización.
======================================================================
```

### 3. Detener y limpiar el contenedor
```bash
docker compose down
```
