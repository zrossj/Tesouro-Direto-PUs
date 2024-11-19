Projeto de webscraping usando selenium para consultar as cotações dos ativos disponíveis no tesouro direto e armazenar em banco de dados. 

Banco de Dados: 
- Postgres


Bibliotecas:
- pandas
- selenium (GECKODRIVER version: 0.35.0)
- bs4
- SQLAlchemy
- psycopg2




Instruções:

Para executar o noteobook, é necessário:

1. Instalar as bibliotecas utilizadas e PostgreSQL. O arquivo 'libs.txt' possui as principais libs usadas e necessarias ao projeto.

2. Crie um arquivo com o nome 'creds.txt' com a string URL para conectar ao banco de dados usando a engine do SQLAlchemy.

3. Execute o notebook.


References: 
	https://docs.sqlalchemy.org/en/20/core/engines.html
