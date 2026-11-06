# Actividad 1: Ejecución Secuencial

## 📌 Enlace de la Carpeta en GitHub
[Ver carpeta en el Repositorio](https://github.com/MartinCordero7/Ejercicios-Python-Distribuidas/tree/main/1_secuencial)

---

## 📖 Descripción del Ejemplo de la Vida Real: *Proceso de Lavandería* 🧺

En la vida cotidiana, muchas tareas no se pueden realizar a la vez debido a dependencias estrictas. Un caso claro es el proceso de lavado de ropa:
1. **Lavar la ropa:** La ropa sucia entra a la lavadora.
2. **Secar la ropa:** No se puede meter la ropa a la secadora hasta que el ciclo de lavado termine.
3. **Planchar la ropa:** No se puede planchar ropa húmeda; debe esperarse a que termine la secadora.
4. **Doblar y guardar:** Solo se organiza la ropa una vez que está seca y planchada.

### 🧠 Concepto Técnico
- **Ejecución Secuencial:** El flujo del programa se ejecuta paso a paso en un único hilo de ejecución. Cada instrucción bloquea a la siguiente hasta que finalice.
- **Ventaja:** Predecible, determinista y sin riesgo de conflictos sobre datos compartidos.
- **Desventaja:** El tiempo total es la suma de los tiempos individuales ($T_{total} = T_1 + T_2 + T_3 + T_4$), sin aprovechar recursos paralelos.

---

## 🐳 Cómo Ejecutar con Docker Compose

Asegúrate de estar ubicado dentro de esta carpeta:

```bash
cd 1_secuencial
```

### 1. Construir y ejecutar el contenedor
```bash
docker compose up --build
```
*(o con la sintaxis clásica de Docker: `docker-compose up --build`)*

### 2. Salida esperada en consola
```text
=================================================================
   EJEMPLO 1: EJECUCIÓN SECUENCIAL (PROCESO DE LAVANDERÍA)
=================================================================
[1/4] 🧺 Iniciando lavado de ropa...
      ✅ Ropa lavada con éxito.
[2/4] ☀️ Pasando ropa a la secadora...
      ✅ Ropa completamente seca.
[3/4] 👔 Planchando camisas y pantalones...
      ✅ Ropa planchada y sin arrugas.
[4/4] 🚪 Guardando la ropa en el armario...
      ✅ Ropa organizada en el armario.
-----------------------------------------------------------------
⏱️ Tiempo total de ejecución secuencial: 5.51 segundos
=================================================================
```

### 3. Detener y limpiar el contenedor
```bash
docker compose down
```
