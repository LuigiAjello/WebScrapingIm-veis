# Web Scraping de Imóveis - DF Imóveis 🤖

Este projeto é um web scraper desenvolvido em Python para coletar dados de imóveis do site DF Imóveis (https://www.dfimoveis.com.br/). O sistema permite filtrar imóveis por diversos critérios, extrair informações detalhadas e armazená-las em um banco de dados MySQL e arquivos CSV.

---
Desenvolvido por - 
Luigi Ajello
   Linkedin: [Luigi Ajello](www.linkedin.com/in/luigi-pedroso-ajello-346934278)
   Github: [Luigi Ajello](https://github.com/LuigiAjello)

---

 ## 📋 Funcionalidades
- Filtros avançados:

    -  Tipo de negociação (Venda)

    -  Tipo de imóvel (Apartamento)

    -  Localização (Estado, Cidade, Bairro)

    -    Número de quartos

    -    Endereço parcial

- Extração de dados:

    -    Título do imóvel

    -   Metragem

    -   Número de quartos, suítes e vagas

    -   Descrição breve

    -   Preço e valor por metro quadrado

- Armazenamento:

    -   Banco de dados MySQL

    -   Arquivos CSV para backup

- Navegação automática:

    - Identificação e navegação por páginas de resultados

    - Coleta de todos os imóveis disponívei

## 🛠️ Tecnologias utilizadas
- Python 3

- Selenium (automação web)

- Pandas (manipulação de dados)

- SQLAlchemy (conexão com banco de dados)

- MySQL (banco de dados relacional)

- Dotenv (gerenciamento de variáveis de ambiente)
## 📁 Estrutura do projeto
    ```bash
        dfimoveis-scraper/
        │
        ├── main.py                # Script principal que orquestra a coleta de dados
        ├── db_connection.py       # Configurações de conexão com o banco de dados
        ├── create_db_imoveis.sql  # Script SQL para criação do banco de dados
        ├── requirements.txt       # Dependências do projeto
        │
        ├── suports/
        │   ├── Filtro_Pesquisa.py # Classe para manipulação dos filtros de pesquisa
        │   ├── xpaths.py          # Seletores XPath dos elementos da página
        │   └── extracoes.py       # Funções para extração e tratamento de dados
        │
        └── .env                   # Arquivo de configuração (não versionado)

## ⚙️ Configuração
1. Pré-requisitos:

    - Python 3.8+

    - MySQL instalado e configurado

    - Google Chrome instalado

    - ChromeDriver compatível com sua versão do Chrome
2. Instalação:
    ```bash
    git clone [URL_DO_REPOSITORIO]
    cd dfimoveis-scraper
    pip install -r requirements.txt
3. Configuração do banco de dados:
    - Execute o script create_db_imoveis.sql no seu MySQL

    - Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
    ```bash
    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_NAME=dfimoveis_db
4. Execução:
    ```bash
    python main.py
## 🎯 Personalização
Você pode modificar os parâmetros de pesquisa diretamente no arquivo main.py:
```bash
TIPO_VENDA = 'VENDA'
TIPO_IMOVEl = 'APARTAMENTO'
ESTADO = 'DF'
CIDADE = 'BRASILIA / PLANO PILOTO'
BAIRRO = 'ASA NORTE'
NUM_QUARTOS = 1
ENDERECO = 'sh'
```
##  📊 Saída
O projeto gera dois arquivos CSV e armazena os dados no banco MySQL:

  -  imoveis_dfimoveis.csv: Dados detalhados de todos os imóveis coletados

   - paginas_dfimoveis.csv: Metadados sobre as páginas processadas
## ⚠️ Considerações legais 
Este projeto foi desenvolvido apenas para fins educacionais. Antes de usar web scraping em qualquer site, verifique os Termos de Serviço e a política de robots.txt do site alvo. O uso responsável de web scraping é essencial para respeitar os direitos de propriedade intelectual e as leis de proteção de dados.