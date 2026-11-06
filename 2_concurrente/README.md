# Actividad 2: Concurrencia con Asyncio (Corutinas y Bucle de Eventos)

## 📌 Enlace de la Carpeta en GitHub
[Ver carpeta en el Repositorio](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/2_concurrente)

---

## 📖 Descripción del Ejemplo de la Vida Real: *Atención de Clientes en Cafetería* ☕

Imaginemos una cafetería atendida por un único barista/cajero:
1. Llega **Juan** y pide un Café Americano. El barista inicia la cafetera (tarda 2 segundos).
2. Mientras la máquina prepara el café de Juan, el barista **no se queda de brazos cruzados esperando**; de inmediato toma el pedido de **Pedro** (Capuchino) e inicia su preparación.
3. Luego, toma la orden de **María** (Té Matcha).
4. A medida que las bebidas van quedando listas, el barista las entrega.

### 🧠 Concepto Técnico
- **Concurrencia Cooperativa (`asyncio`):** A diferencia de los hilos del sistema operativo (multithreading), `asyncio` opera sobre un único hilo usando un **Event Loop (bucle de eventos)** y **corutinas** (`async def`).
- **No bloqueante (`await`):** La palabra clave `await asyncio.sleep(...)` suspende temporalmente la corutina actual y cede el control al bucle de eventos para que avance con otras tareas pendientes.
- **Eficiencia:** 
  - Si fuera secuencial, atender a 3 clientes que tardan 2 segundos tomaría **6 segundos** en total.
  - De forma concurrente con `asyncio.gather`, las 3 preparaciones se solapan y terminan en solo **~2 segundos**.

---

## 🐳 Cómo Ejecutar con Docker Compose

Asegúrate de estar ubicado dentro de esta carpeta:

```bash
cd 2_concurrente
```

### 1. Construir y ejecutar el contenedor
```bash
docker compose up --build
```
*(o con la sintaxis clásica de Docker: `docker-compose up --build`)*

### 2. Salida esperada en consola
```text
======================================================================
   EJEMPLO 2: CONCURRENCIA CON ASYNCIO (ATENCIÓN EN CAFETERÍA)
======================================================================
☕ [Barista] Iniciando atención a Juan (Pedido: Café Americano)...
   ⏳ [Juan] Esperando preparación de 2s (el barista atiende a otros mientras)...
☕ [Barista] Iniciando atención a Pedro (Pedido: Capuchino)...
   ⏳ [Pedro] Esperando preparación de 2s (el barista atiende a otros mientras)...
☕ [Barista] Iniciando atención a María (Pedido: Té Matcha)...
   ⏳ [María] Esperando preparación de 2s (el barista atiende a otros mientras)...
   ✅ [Juan] Pedido listo y entregado.
   ✅ [Pedro] Pedido listo y entregado.
   ✅ [María] Pedido listo y entregado.

----------------------------------------------------------------------
⏱️ Tiempo total concurrente: 2.00 segundos
💡 Conclusión:
   De forma secuencial habría tardado 6 segundos (2s + 2s + 2s).
   Gracias a la concurrencia con 'asyncio', los 3 clientes son atendidos
   en paralelo sobre el mismo hilo en apenas ~2 segundos.
======================================================================
```

### 3. Detener y limpiar el contenedor
```bash
docker compose down
```
