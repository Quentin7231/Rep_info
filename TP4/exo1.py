class Product:
    code = "1455QGSDEF5842qsdqd"
    name = "Simon"
    priceET = 20000

    def get_price_it(self,tax):
        return self.priceET + (self.priceET*tax)/100

print(Product().get_price_it(2.1))


n=int(input("nombre de poduit"))
for i in range(n):
    class Product:
        code = str(input("code"))
        name = str(input("nom"))
        priceET = float(input("prix"))
        tax=0.2

        def get_price_it(self):
            return self.priceET + (self.priceET*self.tax)/100

    print(Product().get_price_it())