class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self._battery = battery  # Encapsulated attribute

    def use(self, minutes):
        usage_rate = 0.5
        self._consume_battery(usage_rate * minutes)
        print(f"{self.model} used for {minutes} mins. Battery: {self._battery:.1f}%")

    def charge(self, minutes):
        charge_rate = 1
        self._battery += charge_rate * minutes
        if self._battery > 100:
            self._battery = 100
        print(f"{self.model} charged for {minutes} mins. Battery: {self._battery:.1f}%")

    def show_status(self):
        print(f"{self.brand} {self.model} - Battery: {self._battery:.1f}%")

    def _consume_battery(self, amount):
        self._battery -= amount
        if self._battery < 0:
            self._battery = 0

# Inherited class for gaming phones (Polymorphism in use method)
class GamingPhone(Smartphone):
    def use(self, minutes):
        usage_rate = 1.2  # Consumes more battery
        self._consume_battery(usage_rate * minutes)
        print(f"{self.model} (Gaming) used for {minutes} mins. Battery: {self._battery:.1f}%")

# Inherited class for business phones
class BusinessPhone(Smartphone):
    def use(self, minutes):
        usage_rate = 0.3  # Consumes less battery
        self._consume_battery(usage_rate * minutes)
        print(f"{self.model} (Business) used for {minutes} mins. Battery: {self._battery:.1f}%")

# Example usage
phone1 = GamingPhone("ASUS", "ROG Phone 6")
phone2 = BusinessPhone("BlackBerry", "Key2")

phone1.use(30)       # Uses more battery
phone2.use(30)       # Uses less battery
phone1.charge(20)
phone1.show_status()
phone2.show_status()

