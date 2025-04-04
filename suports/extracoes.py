from selenium.webdriver.common.by import By
import re
# Função para extrair detalhes do imóvel
def extrair_detalhes(detalhes):
    metragem = re.search(r"(\d+) m²", detalhes)
    quartos = re.search(r"(\d+) Quartos?", detalhes)
    suites = re.search(r"(\d+) Suítes?", detalhes)
    vagas = re.search(r"(\d+) Vagas?", detalhes)

    return {
        'metragem': int(metragem.group(1)) if metragem else None,
        'quartos': int(quartos.group(1)) if quartos else None,
        'suites': int(suites.group(1)) if suites else None,
        'vagas': int(vagas.group(1)) if vagas else None
    }

def extrair_precos(elemento):
    try:
        precos_nao_divididos = elemento.find_element(By.CLASS_NAME, "new-price").text
        precos_divididos = precos_nao_divididos.split("\n") if "\n" in precos_nao_divididos else [precos_nao_divididos, ""]

        preco = float(precos_divididos[0].removeprefix("R$ ").replace(".", "").replace(",", "."))
        valor_metro_quadrado = float(precos_divididos[1].removeprefix("Valor m² R$ ").replace(".", "").replace(",", ".")) if len(precos_divididos) > 1 else None
        
        return preco, valor_metro_quadrado
    except Exception as e:
        print(f"Erro ao extrair preços: {e}")
        return None, None
