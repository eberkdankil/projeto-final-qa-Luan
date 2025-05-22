#Teste_02

# 👉 Função a ser testada
def somar(a, b):
    """
    Soma dois valores numéricos.

    Parâmetros:
    a (int | float): Primeiro número
    b (int | float): Segundo número

    Retorno:
    int | float: Resultado da soma
    """
    return a + b

# 🔧 Instale o pytest se estiver no Google Colab
!pip install pytest pytest-cov --quiet


# 🧪 Criação do teste unitário
def test_somar():
    """
    Testa a função somar com diferentes tipos de entrada.
    """
    # Teste com inteiros
    assert somar(2, 3) == 5

    # Teste com floats
    assert somar(1.5, 2.5) == 4.0

    # Teste com zero
    assert somar(0, 0) == 0

    # Teste com negativos
    assert somar(-2, -3) == -5


# Executar o teste manualmente no Colab
test_somar()
print("✅ Todos os testes passaram!")
