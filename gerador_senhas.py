import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    try:
        tamanho = int(input("Informe o tamanho da senha: "))
        print("Senha gerada:", gerar_senha(tamanho))
    except ValueError:
        print("Por favor, insira um número válido.")
