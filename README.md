# Paradigmas de Ejecución en Python: Secuencial, Concurrencia y Sincronización con Lock

Este repositorio contiene tres implementaciones prácticas en Python aplicadas a situaciones de la vida cotidiana para comprender las diferencias clave entre:
1. **Ejecución Secuencial**
2. **Concurrencia sin Sincronización (Condición de Carrera / Race Condition)**
3. **Concurrencia con Sincronización (Exclusión Mutua con Lock)**

Todo el proyecto está dockerizado y listo para ser ejecutado fácilmente mediante **Docker Compose**.

---

## 📌 Enlace del Repositorio

- **URL Pública de GitHub:** [https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas.git](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas.git)

---

## 📂 Estructura del Proyecto

```text
.
├── 1_secuencial/
│   └── main.py              # Proceso de Lavandería (Paso a paso en orden estricto)
├── 2_concurrente_sin_lock/
│   └── main.py              # Venta de Boletos de Concierto (Race Condition y sobreventa)
├── 3_concurrente_con_lock/
│   └── main.py              # Cajero Automático Bancario (Exclusión mutua con Lock)
├── Dockerfile               # Imagen base ligera en Python
├── docker-compose.yml       # Orquestación de los 3 servicios
├── .gitignore
└── README.md
```

---

## 📖 Casos de la Vida Real Implementados

### 1. Ejecución Secuencial: *Proceso de Lavandería* 🧺
- **Carpeta:** `1_secuencial/main.py`
- **Analogía:** En una lavandería, el flujo de tareas es estrictamente dependiente:
  1. Lavar la ropa.
  2. Secar la ropa (no puedes secar antes de lavar).
  3. Planchar la ropa (no puedes planchar ropa mojada).
  4. Guardar en el armario.
- **Concepto técnico:** Las instrucciones se ejecutan una después de la otra en un solo hilo. El tiempo total es la suma exacta de los tiempos de cada tarea ($T_{total} = \sum T_i$). Es predecible y seguro, pero no aprovecha el paralelismo.

---

### 2. Concurrencia sin Lock: *Venta de Boletos de Concierto (Sobreventa)* 🎟️
- **Carpeta:** `2_concurrente_sin_lock/main.py`
- **Analogía:** Una plataforma de conciertos tiene solo **3 boletos disponibles**. Al mismo tiempo, 5 clientes intentan comprar el último inventario.
- **Concepto técnico:** Se lanzan múltiples hilos (`threading.Thread`) concurrentemente sin control de acceso al recurso compartido (`boletos_disponibles`).
- **Problema:** Varios hilos consultan la disponibilidad antes de que los demás descuenten el inventario, generando una **condición de carrera (Race Condition)** y provocando una sobreventa (quedando un inventario inconsistente o negativo).

---

### 3. Concurrencia con Lock: *Retiro en Cajero Automático (Cuenta Compartida)* 🏧
- **Carpeta:** `3_concurrente_con_lock/main.py`
- **Analogía:** Dos personas (Juan y María) tienen una cuenta bancaria compartida con un saldo de **$100**. Ambos acuden a cajeros diferentes al mismo segundo e intentan retirar **$80** cada uno.
- **Concepto técnico:** Se utiliza un cerrojo de exclusión mutua (`threading.Lock()`). Solo un hilo a la vez puede adquirir el `lock` para consultar y descontar el saldo.
- **Solución:** La sección crítica se ejecuta de forma atómica. El primer hilo procesa el retiro con éxito dejando $20; el segundo hilo entra inmediatamente después, verifica que $20 < $80 y deniega la transacción por saldo insuficiente, protegiendo la integridad de la cuenta.

---

## 🚀 Requisitos Previos

Tener instalado en el sistema:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🐳 Cómo Ejecutar con Docker Compose

### 1. Clonar el repositorio
```bash
git clone https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas.git
cd Ejercicios-Python-Distribuidas
```

### 2. Construir la imagen Docker
```bash
docker compose build
# (o docker-compose build)
```

### 3. Ejecutar los scripts individualmente

Puedes ejecutar cada uno de los 3 casos usando el servicio correspondiente:

#### A) Ejecutar el caso Secuencial:
```bash
docker compose run --rm secuencial
```
*(o con sintaxis clásica: `docker-compose run --rm secuencial`)*

#### B) Ejecutar el caso Concurrente sin Lock (Condición de carrera):
```bash
docker compose run --rm concurrente
```
*(o con sintaxis clásica: `docker-compose run --rm concurrente`)*

#### C) Ejecutar el caso Concurrente con Lock (Exclusión mutua):
```bash
docker compose run --rm con_lock
```
*(o con sintaxis clásica: `docker-compose run --rm con_lock`)*

---

### 4. Ejecutar todos los servicios en secuencia
Si deseas ver la ejecución de los tres casos juntos:
```bash
docker compose up
```

Para detener y limpiar los contenedores:
```bash
docker compose down
```
