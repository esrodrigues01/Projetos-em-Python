from forex_python.converter import CurrencyRates

c = CurrencyRates()

v1 = float(input("\nQUAL VALOR EM EUROS DESEJA CONVERTER PARA REAIS? "))

r = round(c.convert("EUR", "BRL", v1), 2)

print(f"${v1} = R${r}")