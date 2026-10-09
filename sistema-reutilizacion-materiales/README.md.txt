# Sistema de Gestión y Reutilización de Materiales Industriales

Prueba de Concepto (PoC) para la optimización de residuos y recortes de material (*scrap*) entre múltiples plantas o filiales industriales.


## 🚀 Características Principales

- **Base de Datos Centralizada:** Almacenamiento en PostgreSQL (vía Supabase) para inventario y necesidades.

- **Matching Engine (Algoritmo de Cruce):** Evaluación en tiempo real de material, calibre y dimensiones mínimas requeridas.

- **Economía Circular:** Filtrado automático para derivar excedentes de una planta a otra sin duplicar costos.


## 🛠️ Tecnologías

- **Lenguaje:** Python 3

- **Base de Datos:** PostgreSQL / Supabase REST API

- **Cliente:** `supabase-py`


## ⚙️ Configuración y Ejecución

1. Instalar dependencias:

   ```bash
  
   pip install supabase

2. Ejecutar el script SQL (schema.sql) en la consola de PostgreSQL / Supabase

3. Configurar la clave de API y ejecutar: python matching_engine.py
