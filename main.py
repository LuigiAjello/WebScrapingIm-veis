from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
from db_connection import engine


def main():
    #importando funcao de extrair os detalhes
    from suports.extracoes import extrair_detalhes,extrair_precos
    #importando todos os xpaths
    from suports.xpaths import xpath_venda, xpath_imovel, xpath_estado, xpath_cidade, xpath_bairro, xpath_endereco, xpath_quartos
    #importando classe dos filtros
    from suports.Filtro_Pesquisa import Filtro_pesquisa

    TIPO_VENDA = 'VENDA'
    TIPO_IMOVEl = 'APARTAMENTO'
    ESTADO = 'DF'
    CIDADE = 'BRASILIA / PLANO PILOTO'
    BAIRRO = 'ASA SUL'
    NUM_QUARTOS = 2 # "TODOS OS QUARTOS" / 1 / 2 / 3 / 4 / "5 OU +"
    ENDERECO = 'sqs'

    # Configuração do navegador
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    url = 'https://www.dfimoveis.com.br/'
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # Aplicando os filtros
    Filtro_pesquisa(driver, wait).add_filtro_digitavel_e_selecionavel(xpath_venda, TIPO_VENDA)
    Filtro_pesquisa(driver, wait).add_filtro_digitavel_e_selecionavel(xpath_imovel, TIPO_IMOVEl)
    Filtro_pesquisa(driver, wait).add_filtro_digitavel_e_selecionavel(xpath_estado, ESTADO)
    Filtro_pesquisa(driver, wait).add_filtro_digitavel_e_selecionavel(xpath_cidade, CIDADE)
    Filtro_pesquisa(driver, wait).add_filtro_digitavel_e_selecionavel(xpath_bairro, BAIRRO)
    Filtro_pesquisa(driver, wait).add_filtro_somente_selecionavel(xpath_quartos, NUM_QUARTOS)
    Filtro_pesquisa(driver, wait).add_filtro_somente_digitavel(xpath_endereco, ENDERECO)

    # Clicar no botão de busca
    botao_busca = wait.until(EC.presence_of_element_located((By.ID, "botaoDeBusca")))
    botao_busca.click()

    # Encontrar número de páginas
    try:
        pagination = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".pagination li")))
        pagination_numbers = [elem.text.strip() for elem in pagination if elem.text.strip().isdigit()]
        numero_paginas = int(pagination_numbers[-1]) if pagination_numbers else 1
        print("Total páginas:", numero_paginas)
    except Exception as e:
        print("Erro ao obter a paginação:", e)
        numero_paginas = 1

    sleep(2)

    # Lista para armazenar os imóveis
    lst_imoveis = []
    lst_paginas = []

    # Loop pelas páginas
    for pagina in range(1, numero_paginas + 1):
        print(f"Coletando dados da página {pagina}...")

        resultados_container = wait.until(EC.presence_of_element_located((By.ID, "resultadoDaBuscaDeImoveis")))
        elementos = resultados_container.find_elements(By.TAG_NAME, "a")
        
        print(f"Página {pagina} - {len(elementos)} imóveis encontrados")  # Debug

        lst_paginas.append({'Numero Pagina': pagina, 'Quantidade de Imóveis Coletados': len(elementos)})
        
        #loop pelos elementos da pagina 
        for elem in elementos:
            try:
                
                imovel = {}

                    # Título do imóvel
                try:
                    imovel['title'] = elem.find_element(By.CLASS_NAME, "new-title").text
                except:
                    imovel['title'] = None
                    #Detalhes separados
                try:
                    detalhes = elem.find_element(By.CLASS_NAME, "new-details-ul").text
                    imovel.update(extrair_detalhes(detalhes))
                except Exception as e:
                    print(f"Erro ao extrair detalhes do imóvel: {e}")
                    imovel.update({'metragem': None, 'quartos': None, 'suites': None, 'vagas': None})

                    # Pequena descricao do imóvel
                try:
                    imovel['PequenaDescricao'] = elem.find_element(By.CSS_SELECTOR, ".new-simple.phrase").text
                except:
                    imovel['PequenaDescricao'] = None
                                    
                    # Preços
                try:
                    imovel["preco"], imovel["ValorMetroQuadrado"] = extrair_precos(elem)
                except Exception as e:
                    print(f"Erro ao extrair preços do imóvel: {e}")
                    imovel["preco"], imovel["ValorMetroQuadrado"] = None, None

                    
                lst_imoveis.append(imovel)

            except Exception as e:
                print(f"Erro ao processar imóvel: {e}")
                continue

        # Ir para a próxima página, se houver
        if pagina < numero_paginas:
            try:
                botao_proximo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.next")))
                driver.execute_script("arguments[0].click();", botao_proximo)
                sleep(3)
            except Exception as e:
                print(f"Erro ao ir para próxima página: {e}")
                break
    # Criar DataFrame e salvar
    df_imoveis = pd.DataFrame(lst_imoveis)
    df_paginas = pd.DataFrame(lst_paginas)


    #Insert no db no MySQL
    df_imoveis.to_sql('imoveis', con=engine, if_exists='append', index=False)

    df_imoveis.to_csv("imoveis_dfimoveis.csv", index=False, encoding="utf-8")
    df_paginas.to_csv("paginas_dfimoveis.csv", index=False, encoding="utf-8")

    driver.quit()

if __name__ == "__main__":
    main()




