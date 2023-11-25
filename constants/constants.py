DICT_TIPO_TIENDA = {
    'Tienda especializada': 1,
    'Tienda Outlet': 2,
    'Supermercado': 3,
    'Hipermercado': 4,
    'Minimercado': 5,
    'Tienda Regional': 6
}



QUERY_TABLE_TIPO_DOCUMENTO = """
CREATE TABLE IF NOT EXISTS tipo_documento(
    id INTEGER PRIMARY KEY,
    documento TEXT NOT NULL
);
"""

QUERY_TABLE_TIPO_TIENDA = """
CREATE TABLE IF NOT EXISTS tipo_tienda(
    id INTEGER PRIMARY KEY,
    tipo_tienda TEXT NOT NULL
);
"""

QUERY_TABLE_BARRIO = """
CREATE TABLE IF NOT EXISTS barrio(
    id INTEGER PRIMARY KEY,
    nombre_barrio TEXT NOT NULL
);
"""

QUERY_TABLE_TIENDA = """
CREATE TABLE IF NOT EXISTS tienda(
    id INTEGER PRIMARY KEY,
    id_tipo_tienda INTEGER NOT NULL,
    id_barrio INTEGER NOT NULL,
    latitud REAL NOT NULL,
    longitud REAL NOT NULL,
    FOREIGN KEY(id_tipo_tienda)
    REFERENCES tipo_tienda(id),
    FOREIGN KEY(id_barrio)
    REFERENCES barrio(id)
);
"""

QUERY_TABLE_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente(
    documento TEXT PRIMARY KEY,
    id_tipo_documento INTEGER NOT NULL,
    latitud REAL NOT NULL,
    longitud REAL NOT NULL,
    FOREIGN KEY(id_tipo_documento)
    REFERENCES tipo_documento(id)
);
"""

QUERY_TABLE_COMPRA = """
CREATE TABLE IF NOT EXISTS compra(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente TEXT NOT NULL,
    id_tienda INTEGER NOT NULL,
    valor_compra REAL NOT NULL,
    distancia_tienda_cliente REAL NOT NULL,
    FOREIGN KEY(id_cliente)
    REFERENCES cliente(documento),
    FOREIGN KEY(id_tienda)
    REFERENCES tienda(id)
);
"""

QUERY_INSERT_TIENDA = """
INSERT INTO tienda(id, id_tipo_tienda, id_barrio, latitud, longitud)
VALUES (?, ?, ?, ?, ?)
"""

QUERY_INSERT_CLIENTE = """
INSERT INTO cliente(documento, id_tipo_documento, latitud, longitud)
VALUES (?, ?, ?, ?)
"""

QUERY_INSERT_COMPRA = """
INSERT INTO compra(id_cliente, id_tienda, valor_compra, distancia_tienda_cliente)
VALUES (?, ?, ?, ?)
"""

QUERY_INSERT_TIPO_TIENDA = """INSERT INTO tipo_tienda(id, tipo_tienda) VALUES (?, ?)"""

QUERY_INSERT_TIPO_DOCUMENTO = """INSERT INTO tipo_documento(id, documento) VALUES (?, ?)"""

QUERY_INSERT_BARRIO = """INSERT INTO barrio(id, nombre_barrio) VALUES (?, ?)"""