# Ejercicios de Programación Concurrente y Distribuida

Este repositorio contiene tres actividades independientes que abordan diferentes paradigmas de ejecución mediante ejemplos prácticos de la vida cotidiana en Python y Dockerizados con **Docker Compose**.

Cada actividad está organizada en su propia subcarpeta con su respectivo código fuente (`main.py`), contenedor (`Dockerfile`), configuración de orquestación (`docker-compose.yml`) y documentación detallada (`README.md`).

---

## 📌 Enlaces Directos a Cada Actividad

| Actividad | Paradigma | Caso de la Vida Real | Enlace a la Carpeta |
| :--- | :--- | :--- | :--- |
| **Actividad 1** | **Secuencial** | 🧺 Proceso de Lavandería (paso a paso estricto) | [📂 Ver Actividad 1](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/1_secuencial) |
| **Actividad 2** | **Concurrencia sin Lock** | 🎟️ Venta de Boletos de Concierto (Race Condition y sobreventa) | [📂 Ver Actividad 2](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/2_concurrente_sin_lock) |
| **Actividad 3** | **Concurrencia con Lock** | 🏧 Cajero Automático Bancario (Exclusión mutua y consistencia) | [📂 Ver Actividad 3](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/3_concurrente_con_lock) |

---

## 📂 Estructura General del Repositorio

```text
Ejercicios-Python-Distribuidas/
├── 1_secuencial/
│   ├── main.py                  # Script Python: Lavandería
│   ├── Dockerfile               # Contenedor independiente
│   ├── docker-compose.yml       # Orquestación de la actividad 1
│   └── README.md                # Documentación de la actividad 1
├── 2_concurrente_sin_lock/
│   ├── main.py                  # Script Python: Boletos de concierto
│   ├── Dockerfile               # Contenedor independiente
│   ├── docker-compose.yml       # Orquestación de la actividad 2
│   └── README.md                # Documentación de la actividad 2
├── 3_concurrente_con_lock/
│   ├── main.py                  # Script Python: Cajero automático
│   ├── Dockerfile               # Contenedor independiente
│   ├── docker-compose.yml       # Orquestación de la actividad 3
│   └── README.md                # Documentación de la actividad 3
├── docker-compose.yml           # Compose raíz para ejecutar cualquier actividad
├── .gitignore
└── README.md                    # Índice general del repositorio
```

---

## 🚀 Cómo Ejecutar Cada Actividad

Puedes ejecutar cada actividad de dos formas: ingresando directamente a la subcarpeta de cada una o desde la raíz del proyecto.

### Opción A: Ejecutar desde la subcarpeta de la actividad (Recomendado para entrega individual)

1. **Actividad 1 (Secuencial):**
   ```bash
   cd 1_secuencial
   docker compose up --build
   ```

2. **Actividad 2 (Concurrente sin Lock):**
   ```bash
   cd 2_concurrente_sin_lock
   docker compose up --build
   ```

3. **Actividad 3 (Concurrente con Lock):**
   ```bash
   cd 3_concurrente_con_lock
   docker compose up --build
   ```

---

### Opción B: Ejecutar desde la raíz del proyecto

Si te encuentras en la raíz del repositorio, puedes ejecutar cualquiera de las tres actividades directamente:

```bash
# Ejecutar Actividad 1
docker compose run --rm secuencial

# Ejecutar Actividad 2
docker compose run --rm concurrente

# Ejecutar Actividad 3
docker compose run --rm con_lock
```
*(Nota: También puedes usar `docker-compose` con guion según la versión de Docker instalada).*
