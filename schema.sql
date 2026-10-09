-- 1. Crear tabla de Plantas
CREATE TABLE IF NOT EXISTS plantas (
    planta_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(100)
);

-- 2. Crear tabla de Inventario de Scrap
CREATE TABLE IF NOT EXISTS inventario_scrap (
    material_id SERIAL PRIMARY KEY,
    planta_origen_id INT REFERENCES plantas(planta_id),
    tipo_material VARCHAR(50) NOT NULL,
    calibre VARCHAR(20) NOT NULL,
    largo_mm NUMERIC(10,2) NOT NULL,
    ancho_mm NUMERIC(10,2) NOT NULL,
    cantidad INT NOT NULL,
    estado VARCHAR(20) DEFAULT 'Disponible'
);

-- 3. Crear tabla de Necesidades de Material
CREATE TABLE IF NOT EXISTS necesidades_material (
    necesidad_id SERIAL PRIMARY KEY,
    planta_solicitante_id INT REFERENCES plantas(planta_id),
    tipo_material VARCHAR(50) NOT NULL,
    calibre VARCHAR(20) NOT NULL,
    largo_max_mm NUMERIC(10,2) NOT NULL,
    ancho_max_mm NUMERIC(10,2) NOT NULL,
    cantidad INT NOT NULL,
    estado VARCHAR(20) DEFAULT 'Pendiente'
);

-- 4. Datos de prueba
INSERT INTO plantas (nombre, ubicacion) VALUES 
('Planta A - Metalúrgica', 'Zona Norte'),
('Planta B - Piezas Pequeñas', 'Zona Sur');

INSERT INTO inventario_scrap (planta_origen_id, tipo_material, calibre, largo_mm, ancho_mm, cantidad, estado) VALUES
(1, 'Lámina de acero', '2mm', 500.0, 300.0, 10, 'Disponible');

INSERT INTO necesidades_material (planta_solicitante_id, tipo_material, calibre, largo_max_mm, ancho_max_mm, cantidad, estado) VALUES
(2, 'Lámina de acero', '2mm', 400.0, 250.0, 5, 'Pendiente');
