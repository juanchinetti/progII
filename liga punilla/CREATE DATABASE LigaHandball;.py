-- #Crear la base de datos
DROP DATABASE IF EXISTS `LigaHandball`;
CREATE DATABASE IF NOT EXISTS LigaHandball;
USE LigaHandball;

-- #Tabla de Localidades
CREATE TABLE Localidades (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- #Tabla de Géneros
CREATE TABLE Generos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL UNIQUE
);

-- #Tabla de Clubes
CREATE TABLE Clubes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    logo VARCHAR(255),  -- Almacena la ruta del archivo del logo
    localidad_id INT,
    tipo ENUM('Masculino', 'Femenino', 'Mixto') NOT NULL,
    fecha_fundacion DATE,
    FOREIGN KEY (localidad_id) REFERENCES Localidades(id)
);

-- #Tabla de Jugadores
CREATE TABLE Jugadores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(10) NOT NULL UNIQUE,  -- Limitar a 10 caracteres para evitar datos inconsistentes
    correo_electronico VARCHAR(100) UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    genero_id INT NOT NULL,
    localidad_id INT NOT NULL,
    club_id INT,
    ficha_medica_activa BOOLEAN NOT NULL DEFAULT 0,  -- Indicador de ficha médica activa
    carnet VARCHAR(255),  -- Almacena la ruta del archivo del carnet
    FOREIGN KEY (genero_id) REFERENCES Generos(id),
    FOREIGN KEY (localidad_id) REFERENCES Localidades(id),
    FOREIGN KEY (club_id) REFERENCES Clubes(id)
);

-- #Insertar Localidades
INSERT INTO Localidades (nombre) VALUES 
('Bialet Massé'), 
('Capilla del Monte'), 
('Cosquín (cabecera)'), 
('Huerta Grande'), 
('La Cumbre'), 
('La Falda'), 
('Los Cocos'), 
('San Antonio de Arredondo'), 
('San Esteban'), 
('Santa María'), 
('Tanti'), 
('Valle Hermoso'), 
('Villa Carlos Paz'), 
('Villa Giardino'), 
('Villa Icho Cruz'), 
('Villa Santa Cruz del Lago'), 
('Cabalango'), 
('Casa Grande'), 
('Charbonier'), 
('Cuesta Blanca'), 
('Estancia Vieja'), 
('Mayu Sumaj'), 
('San Roque'), 
('Tala Huasi'), 
('Villa Parque Siquiman'), 
('Malagueño'), 
('Córdoba Capital');

--# Insertar Géneros
INSERT INTO Generos (descripcion) VALUES 
('Masculino'),
('Femenino'),
('No binario');

INSERT INTO clubes (id, nombre) VALUES 
(1, 'Club A'),
(2, 'Club B'), 
(3, 'Club C');

-- #Insertar Jugadores de Ejemplo
INSERT INTO Jugadores (nombre, apellido, dni, correo_electronico, fecha_nacimiento, genero_id, localidad_id, club_id) VALUES
('Juan', 'Pérez', '12345678', 'juan.perez@example.com', '1995-05-15', 1, 1, 1),
('Maria', 'González', '87654321', 'maria.gonzalez@example.com', '1998-08-22', 2, 2, 2),
('Luis', 'Martínez', '11223344', 'luis.martinez@example.com', '2002-03-30', 1, 3, 3),
('Ana', 'Lopez', '44332211', 'ana.lopez@example.com', '1999-11-11', 2, 1, 1);