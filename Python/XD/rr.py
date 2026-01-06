







def addsales():
   
    try:
        # aquí validas nombre del cliente
        while True:       
            customer = input("Add to names to customer: ").lower()           
            for letra in customer:
                if letra in "áéíóú":
                    print("Accents are not allowed")
                    break
                elif not letra.isalnum() and letra != " ":
                    print("Special characters are not allowed")
                    break
            else:
                break
        
        # fecha
        while True:
            fecha_str = input("Introduce the date (YYYY-MM-DD): ")
            try:
                fecha_obj = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        

        # 🔥 NUEVO: mostrar libros para elegir cuál se vende
        consultbooks()
        book_id = int(input("Choose the ID of the book to sell: "))

        # validar ID válido
        if not (1 <= book_id <= len(inventory)):
            print("Invalid ID number.")
            return

        # obtener libro seleccionado
        book_selected = inventory[book_id - 1]


        # cantidad
        while True:
            quantity = input("Add to stock: ")
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    break
                else:
                    print("Quantity must be > 0")
            else:
                print("Ingrese números sin decimal")

        # 🔥 VALIDAR STOCK CORRECTO
        if book_selected["stock"] < quantity:
            print("Stock insuficiente.")
            return
        

        # descuento
        while True:
            discount = int(input("Add to discount: "))
            if 0 < discount < 10:
                break
            else:
                print("El descuento debe ser entre 1 y 9")
        

        # descontar del inventario
        book_selected["stock"] -= quantity

        # guardar venta
        savesCustomers(customer, book_selected, quantity, discount, fecha_obj)

    except:
        print("Error: valores numéricos inválidos.")

def savesCustomers(customer, book_selected, quantity, discount, fecha_obj):
    user = {
        "client": customer,
        "title": book_selected["title"],
        "author": book_selected["author"],
        "quantity": quantity,
        "cost": book_selected["cost"],
        "discount": discount,
        "date": fecha_obj
    }
    sales.append(user)
    print("\nsales saved successfully")

def reports():
    try:
        if not sales:
            print("Aún no hay ventas.")
            return

        # Contar cantidad vendida por título
        counts = {}
        for sale in sales:
            title = sale["title"]
            counts[title] = counts.get(title, 0) + sale["quantity"]

        # Ordenar de mayor a menor
        sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        print("\nTop 3 books sold:")
        for title, total_sold in sorted_books[:3]:
            print(f"{title}: {total_sold} vendidos")

    except Exception as e:
        print("Error al calcular estadísticas. Por favor, verifique los datos del inventario.")
        print("DEBUG:", e)