import csv
import os
import locale


while True:
    print("1:Lista producterna")
    print("2:Lägga till product")
    print("3:Ta bort produkt")
    print("4:Ändra produkt")
    print("5: Avsluta")
    val = input("Vad vill du göra:")
    
    if val == "1":
        list_products()
    elif val == "2":
        add_product()
    elif val == "3":
        delete_specific_product()
    elif val == "4":
        change_product()
    elif val == "5":
        break
    



    def format_currency(value):
        return locale.currency(value,grouping=True)


    def load_data(filename): 
        products = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = int(row['id'])
                name = row['name']
                desc = row['desc']
                price = float(row['price'])
                quantity = int(row['quantity'])
                products.append(
                    {                   
                        "id": id,       
                        "name": name,
                        "desc": desc,
                        "price": price,
                        "quantity": quantity
                    }
                )
        return products


    products = load_data('C:\\Users\\leo.juthberg\\Documents\\tillprog\\Uppgift3\\Uppgift3\\db_products.csv')

    def list_products(products):
        for idx, product in enumerate(products, 1):
            print(f"{idx} {product['name']} {product['price']}")

    def load_specific_product():
        asked_id = int(input("Vilket id söker du?: "))
        for product in products:
            if product['id'] == asked_id:
                print(product)
                return product
        print("Produkten hittades inte!")
        return None

    def delete_specific_product():
        frogat_id = int(input("Vilket id vill du ta bort?: "))
        for p in products:
            if p["id"] == frogat_id:
                products.remove(p)
                print("Produkten är borttagen.")
                return
        print("Produkten hittades inte!")
        save_product()

    def add_product():
        new_id = max([p['id'] for p in products], default=0) + 1
        name = input("Produktnamn: ")
        desc = input("Beskrivning: ")
        price = float(input("Pris: "))
        quantity = int(input("Antal: "))
        products.append({"id": new_id, "name": name, "desc": desc, "price": price, "quantity": quantity})
        print("Produkten har lagts till.")
        save_product()

    
    def save_product(filepath, products):   
        try:
            with open(filepath, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames={'id', 'names', 'desc', 'price', 'quantity'})
                writer.writeheader()
                writer.writerows(products)
    
        except Exception as error_code:
            print("fel")   
            
            if isinstance(error_code, OSError) and error_code.errno == 13:
                return f"Orsak: Filen är skrivskyddad"
            else:
                return f"Orsak: {error_code}"
        
        return f"ok"
    
    
        
    def change_product():
        frogat_id = int(input("Vilket id vill du ändra?: "))
        for p in products:
            if p["id"] == frogat_id:
                print("Produkten hittad:")
                print(p)

                new_name = input(f"Nytt namn ({p['name']}): ") or p['name']
                new_desc = input(f"Ny beskrivning ({p['desc']}): ") or p['desc']
                new_price = input(f"Nytt pris ({p['price']}): ")
                new_quantity = input(f"Nytt antal ({p['quantity']}): ")

                p['name'] = new_name
                p['desc'] = new_desc
                if new_price:
                    p['price'] = float(new_price)
                if new_quantity:
                    p['quantity'] = int(new_quantity)

                print("Produkten har ändrats.")
                save_product()
                return
    print("Produkten hittades inte!")
        






