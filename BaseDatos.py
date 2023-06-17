import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conexion = sqlite3.connect("happyburger.db")
cursor = conexion.cursor()

# Crear tabla 'clientes'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        clave TEXT PRIMARY KEY,
        nombre TEXT,
        direccion TEXT,
        correo_electronico TEXT,
        telefono TEXT
    )
""")

# Crear tabla 'menu'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        clave TEXT PRIMARY KEY,
        nombre TEXT,
        precio REAL
    )
""")

# Crear tabla 'pedido'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        numero_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        producto TEXT,
        precio REAL,
        cantidad INTEGER
    )
""")




# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos y tablas creadas exitosamente.")
