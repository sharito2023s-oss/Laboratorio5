def cambio_voraz(cantidad, monedas):
    resultado = {}
    for moneda in monedas:
        if cantidad >= moneda:
            num = cantidad // moneda
            cantidad -= num * moneda
            resultado[moneda] = num
    return resultado

monedas = [50, 20, 10, 5, 1]
cambio = cambio_voraz(63, monedas)
print("💰 Cambio voraz para $63:")
for moneda, cantidad in cambio.items():
    print(f"  {cantidad} moneda(s) de ${moneda}")
