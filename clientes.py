class Clientes:
    """
    Clase para gestionar los clientes de Happy Burger.
    """

    def __init__(self, conexion, cursor):
        """
        Constructor de la clase Clientes.

        Args:
            conexion: Objeto de conexión a la base de datos.
            cursor: Objeto de cursor para ejecutar consultas SQL.
        """
        self.conexion = conexion
        self.cursor = cursor

    def agregar_cliente(self, clave, nombre, direccion, correo_electronico, telefono):
        """
        Agrega un nuevo cliente a la base de datos.

        Args:
            clave: Clave única del cliente.
            nombre: Nombre del cliente.
            direccion: Dirección del cliente.
            correo_electronico: Correo electrónico del cliente.
            telefono: Número de teléfono del cliente.
        """
        query = "INSERT INTO clientes (clave, nombre, direccion, correo_electronico, telefono) VALUES (?, ?, ?, ?, ?)"
        valores = (clave, nombre, direccion, correo_electronico, telefono)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def eliminar_cliente(self, clave):
        """
        Elimina un cliente de la base de datos.

        Args:
            clave: Clave única del cliente a eliminar.
        """
        query = "DELETE FROM clientes WHERE clave = ?"
        valores = (clave,)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def actualizar_cliente(self, clave, nombre, direccion, correo_electronico, telefono):
        """
        Actualiza los datos de un cliente en la base de datos.

        Args:
            clave: Clave única del cliente a actualizar.
            nombre: Nuevo nombre del cliente.
            direccion: Nueva dirección del cliente.
            correo_electronico: Nuevo correo electrónico del cliente.
            telefono: Nuevo número de teléfono del cliente.
        """
        query = "UPDATE clientes SET nombre = ?, direccion = ?, correo_electronico = ?, telefono = ? WHERE clave = ?"
        valores = (nombre, direccion, correo_electronico, telefono, clave)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    # Otros métodos de la clase Clientes...
