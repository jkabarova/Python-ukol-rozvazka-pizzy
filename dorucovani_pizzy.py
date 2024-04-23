# zakladni trida pro všechny polozky, ktere je mozne objednat
# s atributy jmeno a cena
class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    # retezcova reprezentace polozky
    def __str__(self):
        return f"{self.name}: {self.price} Kč"

# trida Pizza, která dedi z tridy Item a pridava atribut ingredience v 
# v podobě slovníku
class Pizza(Item):
    def __init__(self, name: str, price: int, ingredients: dict):
        super().__init__(name, price)   
        self.ingredients = ingredients

    # metoda pridavajici extra ingredience do pizzy
    def add_extra(self, ingredient, quantity, price_per_ingredient):
        # overi, zda uz je ingredience ve slovníku ingredients
        # pokud je, prida pouze mnozstvi k polozce
        # jinak prida celou polozku vcetne vahy
        if ingredient in self.ingredients:
            quantity1 = self.ingredients[ingredient]
            self.ingredients[ingredient] = quantity + quantity1
        else:
            self.ingredients[ingredient] = quantity
        self.price += price_per_ingredient

    # retezcova reprezentace polozky vcetne pridavanych ingredienci
    def __str__(self):
        return super().__str__() + f"{self.ingredients}"
    
# trida Drink, která dedi z tridy Item a pridava atribut volume, ktery 
# udava objem napoje v ml
class Drink(Item):
    def __init__(self, name: str, price: int, volume: int):
        super().__init__(name, price) 
        self.volume = volume

    # retezcova reprezentace nápoje vcetne množství
    def __str__(self):
        return f"Nápoj: {self.name}, objem: {self.volume}, cena: {self.price} EUR"

# trida pro objednavku jídla a pití
class Order:
    def __init__(self, customer_name: str, delivery_address: str, items: list, status: str = "Nová"):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = status

    # metoda, ktera zmeni stav objednavky na doruceno
    def mark_delivered(self):
        self.status = "Doručeno"

    # retezcova reprezentace objednavky s kompletnim vypisem
    def __str__(self):
        # do promenne se ulozi polozka ze seznamu v datovem typu String, kterou si projdu cyklem a spojim pres odradkovani
        string_item = "\n".join([str(item) for item in self.items])
        return f"Objednávka pro: {self.customer_name} \nNa adresu: {self.delivery_address} \nObjednané zboží: \n{string_item} \nStav objednávky: {self.status}\n"

# trida reprezentujici dorucovatele
class DeliveryPerson:
    def __init__(self, name: str, phone_number: str, available = True, current_order = Order): 
        self.name = name
        self.phone_number = phone_number
        self.available = available
        self.current_order = current_order

    # metoda priradi objednavku dorucovateli, pokud je dostupny a objednavka bude oznacena jako dorucena
    def assign_order(self, order):
        if self.available:
            self.current_order = order
            order.status = "Na cestě"
            self.available = False
        else:
            print(f"Doručovatel momentálně doručuje jinou objednávku.")    
        
    def complete_delivery(self):
        self.current_order.mark_delivered()
        self.available = True

    def __str__(self):
        return f"Doručovatel: {self.name}, {self.phone_number}, dostupný: {self.available}, objednávka: \n{self.current_order}" 
    
# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1.5, 500)

# Vytvoření a výpis objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print()
print("OBJEDNAVKA:")
print("-----------")
print(order)

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)

print("PRIDELENA OBJEDNAVKA DORUCOVATELI")
print("---------------------------------")
print(delivery_person)
print("DORUCOVATEL PRAVE DORUCUJE!")
print("---------------------------")
delivery_person.assign_order(order)
print()

# Dodání objednávky
delivery_person.complete_delivery()
print("OBJEDNAVKA DORUCENA, DORUCOVATEL JE VOLNY!")
print("------------------------------------------")
print(delivery_person)

# Kontrola stavu objednávky po doručení
print("OBJEDNAVKA:")
print("-----------")
print(order)