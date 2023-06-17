import sqlite3

class Pedido:
    """
    Clase que representa un pedido en Happy Burger.

    Attributes:
        conexion: Conexión a la base de datos.
        cursor: Cursor de la base de datos.
    """

    def __init__(self, conexion, cursor):
        """
        Inicializa una instancia de Pedido.

        Args:
            conexion: Conexión a la base de datos.
            cursor: Cursor de la base de datos.
        """
        self.conexion = conexion
        self.cursor = cursor

    def consultar_pedido(self, numero_pedido):
        """
        Consulta un pedido por su número.

        Args:
            numero_pedido (int): Número del pedido a consultar.

        Returns:
            dict: Información del pedido encontrado o None si no se encuentra.
        """
        conexion = sqlite3.connect('happyburger.db')
        cursor = conexion.cursor()


        consulta = "SELECT * FROM pedidos WHERE numero_pedido = ?"
        cursor.execute(consulta, (numero_pedido,))
        pedido_info = cursor.fetchone()

        cursor.close()
        conexion.close()

        return pedido_info

        return None

    def agregar_pedido(self, nombre_cliente, items_pedido):
        """
        Agrega un nuevo pedido a la base de datos.

        Args:
            nombre_cliente (str): Nombre del cliente.
            items_pedido (list): Lista de items del pedido.

        Returns:
            int: Número asignado al nuevo pedido.
        """
        insercion = "INSERT INTO pedidos (cliente, items) VALUES (%s, %s)"
        self.cursor.execute(insercion, (nombre_cliente, items_pedido))
        self.conexion.commit()

        return self.cursor.lastrowid

    def actualizar_pedido(self, numero_pedido, items_pedido):
        """
        Actualiza un pedido existente en la base de datos.

        Args:
            numero_pedido (int): Número del pedido a actualizar.
            items_pedido (list): Lista de items actualizados del pedido.

        Returns:
            bool: True si la actualización fue exitosa, False si no se encuentra el pedido.
        """
        consulta = "SELECT * FROM pedidos WHERE numero = %s"
        self.cursor.execute(consulta, (numero_pedido,))
        resultado = self.cursor.fetchone()

        if resultado:
            actualizacion = "UPDATE pedidos SET items = %s WHERE numero = %s"
            self.cursor.execute(actualizacion, (items_pedido, numero_pedido))
            self.conexion.commit()
            return True

        return False

    def eliminar_pedido(self, numero_pedido):
        """
        Elimina un pedido de la base de datos.

        Args:
            numero_pedido (int): Número del pedido a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encuentra el pedido.
        """
        consulta = "SELECT * FROM pedidos WHERE numero = %s"
        self.cursor.execute(consulta, (numero_pedido,))
        resultado = self.cursor.fetchone()

        if resultado:
            eliminacion = "DELETE FROM pedidos WHERE numero = %s"
            self.cursor.execute(eliminacion, (numero_pedido,))
            self.conexion.commit()
            return True

        return False

    def listar_pedidos(self):
        """
        Obtiene una lista de todos los pedidos en la base de datos.

        Returns:
            list: Lista de diccionarios con la información de los pedidos.
        """
        consulta = "SELECT * FROM pedidos"
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()

        pedidos = []
        for resultado in resultados:
            pedido = {
                'numero': resultado[0],
                'cliente': resultado[1],
                'items': resultado[2]
            }
            pedidos.append(pedido)

        return pedidos

    def generar_ticket(self, numero_pedido):
        """
        Genera un archivo de ticket con la información del pedido.

        Args:
            numero_pedido (int): Número del pedido a generar el ticket.

        Returns:
            bool: True si se generó el ticket correctamente, False si no se encuentra el pedido.
        """
        pedido = self.consultar_pedido(numero_pedido)
        if pedido:
            # Generar contenido del ticket
            contenido = f"Número de Pedido: {pedido['numero']}\n"
            contenido += f"Cliente: {pedido['cliente']}\n"
            contenido += "Items:\n"
            for i, item in enumerate(pedido['items'], start=1):
                contenido += f"{i}. {item}\n"

            # Guardar contenido en el archivo ticket.txt
            with open('ticket.txt', 'w') as archivo:
                archivo.write(contenido)

            return True

        return False
