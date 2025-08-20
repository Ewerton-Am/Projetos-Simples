import requests
import pandas as pd
import tabulate

# Função para obter as taxas de câmbio
def get_rates():
    # Pega cotações BRL, USD, EUR, GBP, JPY, CHF
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,GBP-BRL,JPY-BRL,CHF-BRL"
    response = requests.get(url)
    data = response.json()
    
    rates = {
        "USD": float(data["USDBRL"]["bid"]),
        "EUR": float(data["EURBRL"]["bid"]),
        "GBP": float(data["GBPBRL"]["bid"]),
        "JPY": float(data["JPYBRL"]["bid"]),
        "CHF": float(data["CHFBRL"]["bid"]),
        "BRL": 1.0  # BRL como base
    }
    return rates

# Conversão de moedas
def converter(valor, de, para, rates):
    """
    Converte 'valor' da moeda 'de' para a moeda 'para' usando o dicionário rates.
    """
    if de not in rates or para not in rates:
        return "Moeda inválida!"
    
    # Converte o valor da moeda de origem para BRL
    valor_em_brl = valor * rates[de]
    
    # Converte de BRL para a moeda de destino
    valor_convertido = valor_em_brl / rates[para]
    
    return round(valor_convertido, 2)  # arredonda para 2 casas decimais
moedas = pd.DataFrame(get_rates(), index=[0])
print(tabulate.tabulate(moedas, headers='keys', tablefmt='grid', showindex=False))
print("====================================")
print("Bem-vindo!")
print("Opções de conversão: \n1. USD para BRL\n2. BRL para USD \n3. USD para EUR \n4. EUR para USD")
print("====================================")

while True:
    option = int(input("Escolha uma opção: "))
    if option == 1:
        valor = float(input("Digite o valor em USD: "))
        rates = get_rates()
        print(f"{valor} USD é {converter(valor, 'USD', 'BRL', rates)} BRL")
    elif option == 2:
        valor = float(input("Digite o valor em BRL: "))
        rates = get_rates()
        print(f"{valor} BRL é {converter(valor, 'BRL', 'USD', rates)} USD")
    elif option == 3:
        valor = float(input("Digite o valor em USD: "))
        rates = get_rates()
        print(f"{valor} USD é {converter(valor, 'USD', 'EUR', rates)} EUR")
    elif option == 4:
        valor = float(input("Digite o valor em EUR: "))
        rates = get_rates()
        print(f"{valor} EUR é {converter(valor, 'EUR', 'USD', rates)} USD")
    else:
        print("Opção inválida.")
        kit = input("Você deseja tentar novamente? (sim/não): ")
        if kit.lower() != "sim":
            break
print("Fechando o conversor. Obrigado!")

