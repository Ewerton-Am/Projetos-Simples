def calcular_consumo(distancia, litros, preco_litro):
    consumo = distancia / litros
    custo_km = (litros * preco_litro) / distancia
    return consumo, custo_km

if __name__ == "__main__":
    try:
        d = float(input("Distância percorrida (km): "))
        l = float(input("Litros consumidos: "))
        p = float(input("Preço por litro: "))
        consumo, custo = calcular_consumo(d, l, p)
        print(f"Consumo médio: {consumo:.2f} km/l")
        print(f"Custo por km: R${custo:.2f}")
    except ValueError:
        print("Por favor, insira apenas números válidos.")
