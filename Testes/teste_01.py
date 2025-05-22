#teste 01 

# 📌 Instalação da biblioteca (caso ainda não esteja instalada no ambiente do Colab)
!pip install requests --quiet

# 📦 Importando a biblioteca necessária
import requests

# 🔧 Função para testar a requisição GET em uma API pública
def testar_requisicao_get(url):
    """
    Realiza uma requisição GET para a URL informada e exibe os resultados.

    Parâmetros:
    url (str): URL da API que será testada.

    Retorno:
    None
    """
    try:
        # ⏱️ Fazendo a requisição GET
        resposta = requests.get(url)

        # ✅ Verificando o código de status HTTP da resposta
        if resposta.status_code == 200:
            print("✅ Requisição bem-sucedida!")
            print("Conteúdo da resposta:")
            print(resposta.json())  # Mostra o conteúdo em formato JSON
        else:
            print(f"⚠️ Requisição falhou com status: {resposta.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro durante a requisição: {e}")

# ▶️ Executando o teste com uma API pública de exemplo (JSON Placeholder)
url_teste = "https://jsonplaceholder.typicode.com/posts/1"
testar_requisicao_get(url_teste)
