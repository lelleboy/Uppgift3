import csv
import os
import locale


           #lista

def format_currency(value):
    return locale.currency(value,grouping=True)


def load_data(filename): 
    
    products = []
    
    
    with open(filename, 'r') as file:       #öppnar en fil med read-rättighet
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



#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id





products = load_data('C:\\Users\\leo.juthberg\\Documents\\tillprog\\Uppgift3\\Uppgift3\\db_products.csv')

for idx, product in enumerate(products, 1):
    print(f"{idx} {product["name"]} {product["price"]}")


def load_specific_product():
    asked_id = int(input("Vilket id söker du?: ")) -1 
    for product in products:
        if product['id'] == asked_id:
            print(product)
            return product
    
    print("Produkten hittades inte!")
    return None
load_specific_product()


def delete_specific_product():
    frogat_id = int(input("Vilket id vill du ta bort?: "))
    
    for p in products:
        if p["id"] == frogat_id:
            products.remove(p)
            print(f"Produkten är borttagen.")
            
        
    print("Producten hittades inte!")
    
    

delete_specific_product()

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
os.system('cls')
    




