CREATE TABLE usuarios(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  nombre_completo VARCHAR(255),
  telefono VARCHAR(255),
  email VARCHAR(255) NOT NULL UNIQUE
);