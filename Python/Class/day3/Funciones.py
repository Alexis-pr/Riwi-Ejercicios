

# -------------------------------------------------------
# Sistema de Inventario y Ventas - Versión Simple (Danny)
# -------------------------------------------------------

import datetime   # Para registrar la fecha de cada venta

# -------------------------------------------------------
# Inventario inicial con 5 productos (obligatorio)
# -------------------------------------------------------

# La lista "inventory" guarda diccionarios, cada diccionario es un producto
inventory = [
    {"id": "001", "title": "Dune", "author": "Frank Herbert", "category": "Sci-Fi", "price": 25.0, "stock": 10},
    {"id": "002", "title": "It", "author": "Stephen King", "category": "Horror", "price": 20.0, "stock": 8},
    {"id": "003", "title": "1984", "author": "George Orwell", "category": "Dystopia", "price": 18.0, "stock": 12},
    {"id": "004", "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": 22.0, "stock": 15},
    {"id": "005", "title": "Foundation", "author": "Isaac Asimov", "category": "Sci-Fi", "price": 24.0, "stock": 9}
]

# Lista donde se guardarán todas las ventas realizadas
sales = []


# -------------------------------------------------------
# FUNCIONES DEL INVENTARIO
# -------------------------------------------------------

def list_products():
    """Muestra todos los productos en el inventario."""
    print("\n--- LISTA DE PRODUCTOS ---")

    if not inventory:
        print("No hay productos.")
        return

    for p in inventory:
        print(f"{p['id']} | {p['title']} | {p['author']} | {p['category']} | ${p['price']} | Stock: {p['stock']}")


def register_product():
    """Registra un nuevo producto en el inventario."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")

    pid = input("ID del producto: ").strip()

    # Validar si el ID ya existe
    for p in inventory:
        if p["id"] == pid:
            print("El ID ya existe.")
            return

    title = input("Título: ").strip()
    author = input("Autor: ").strip()
    category = input("Categoría: ").strip()

    # Validar números correctos
    try:
        price = float(input("Precio: "))
        stock = int(input("Cantidad en stock: "))

        if price < 0 or stock < 0:
            print("Precio y stock deben ser positivos.")
            return

    except:
        print("Error: debes ingresar números válidos.")
        return

    new_product = {
        "id": pid,
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("Producto agregado correctamente.")


def update_product():
    """Actualiza los datos de un producto."""
    print("\n--- ACTUALIZAR PRODUCTO ---")
    pid = input("Ingresa el ID del producto: ")

    for p in inventory:
        if p["id"] == pid:

            print("\nSi dejas un campo vacío, no se modifica.\n")

            new_title = input(f"Nuevo título ({p['title']}): ")
            new_author = input(f"Nuevo autor ({p['author']}): ")
            new_category = input(f"Nueva categoría ({p['category']}): ")
            new_price = input(f"Nuevo precio ({p['price']}): ")
            new_stock = input(f"Nuevo stock ({p['stock']}): ")

            # Actualizar solo si escriben algo
            if new_title: p["title"] = new_title
            if new_author: p["author"] = new_author
            if new_category: p["category"] = new_category
            if new_price: p["price"] = float(new_price)
            if new_stock: p["stock"] = int(new_stock)

            print("Producto actualizado.")
            return

    print("Producto no encontrado.")


def delete_product():
    """Elimina un producto del inventario."""
    print("\n--- ELIMINAR PRODUCTO ---")
    pid = input("ID del producto: ")

    for p in inventory:
        if p["id"] == pid:
            inventory.remove(p)
            print("Producto eliminado.")
            return

    print("Producto no encontrado.")


# -------------------------------------------------------
# FUNCIONES DE VENTAS
# -------------------------------------------------------

def register_sale():
    """Registra una venta y descuenta stock."""
    print("\n--- REGISTRAR VENTA ---")
    pid = input("ID del producto vendido: ")

    product = None
    for p in inventory:
        if p["id"] == pid:
            product = p
            break

    if product is None:
        print("Producto no encontrado.")
        return

    try:
        client = input("Nombre del cliente: ").strip()
        quantity = int(input("Cantidad vendida: "))
        discount = float(input("Descuento (0 si no hay): "))

        if quantity <= 0 or discount < 0:
            print("Valores inválidos.")
            return

        if product["stock"] < quantity:
            print("Stock insuficiente.")
            return

    except:
        print("Error: valores numéricos inválidos.")
        return

    # Descontar el stock
    product["stock"] -= quantity

    # Registrar la venta en "sales"
    sale = {
        "client": client,
        "product": product["title"],
        "author": product["author"],
        "quantity": quantity,
        "price": product["price"],
        "discount": discount,
        "date": datetime.date.today().isoformat()
    }

    sales.append(sale)
    print("Venta registrada correctamente.")


# -------------------------------------------------------
# REPORTES
# -------------------------------------------------------

def top_3_products():
    """Muestra los 3 productos más vendidos."""
    print("\n--- TOP 3 PRODUCTOS MÁS VENDIDOS ---")

    if not sales:
        print("Aún no hay ventas.")
        return

    counts = {}  # Diccionario para contar ventas por título

    for s in sales:
        book = s["product"]
        counts[book] = counts.get(book, 0) + s["quantity"]

    # Ordenar por cantidad vendida (de mayor a menor)
    sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for title, qty in sorted_books[:3]:
        print(f"{title}: {qty} vendidos")


def sales_by_author():
    """Agrupa las ventas por autor."""
    print("\n--- VENTAS AGRUPADAS POR AUTOR ---")

    if not sales:
        print("Aún no hay ventas.")
        return

    totals = {}

    for s in sales:
        author = s["author"]
        amount = s["quantity"] * s["price"]
        totals[author] = totals.get(author, 0) + amount

    for author, total in totals.items():
        print(f"{author}: ${total}")


def income_report():
    """Calcula ingreso bruto y neto."""
    print("\n--- REPORTE DE INGRESOS ---")

    gross = sum(s["quantity"] * s["price"] for s in sales)
    net = sum((s["quantity"] * s["price"]) - s["discount"] for s in sales)

    print(f"Ingreso bruto: ${gross}")
    print(f"Ingreso neto: ${net}")


# -------------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------------

def menu():
    """Menú principal del programa."""
    while True:
        print("""
======== SISTEMA DE LIBRERÍA ========
1. Ver productos
2. Registrar producto
3. Actualizar producto
4. Eliminar producto
5. Registrar venta
6. Top 3 productos
7. Ventas por autor
8. Reporte de ingresos
9. Salir
""")

        option = input("Elige una opción: ")

        if option == "1": list_products()
        elif option == "2": register_product()
        elif option == "3": update_product()
        elif option == "4": delete_product()
        elif option == "5": register_sale()
        elif option == "6": top_3_products()
        elif option == "7": sales_by_author()
        elif option == "8": income_report()
        elif option == "9":
            print("Adiós.")
            break
        else:
            print("Opción inválida.")


# Ejecutar menú
menu() 