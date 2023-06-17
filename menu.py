import sqlite3

class Menu:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor

    def agregar_producto(self):
        clave = input("Ingrese la clave del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))

        self.cursor.execute("INSERT INTO menu VALUES (?, ?, ?)", (clave, nombre, precio))
        self.conexion.commit()
        print("Producto agregado al menú exitosamente.")

    def eliminar_producto(self):
        clave = input("Ingrese la clave del producto a eliminar: ")

        self.cursor.execute("DELETE FROM menu WHERE clave = ?", (clave,))
        self.conexion.commit()
        print("Producto eliminado del menú exitosamente.")

    def actualizar_producto(self):
        clave = input("Ingrese la clave del producto a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = float(input("Ingrese el nuevo precio del producto: "))

        self.cursor.execute("""
            UPDATE menu SET nombre = ?, precio = ?
            WHERE clave = ?
        """, (nombre, precio, clave))
        self.conexion.commit()
        print("Producto actualizado exitosamente.")
