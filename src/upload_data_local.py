import os
import pandas as pd
import sqlalchemy



#Definindo uma string de conexão
str_connection = 'sqlite:///{path_to_data}'


# Os endereços do projeto e sub-pastas
BASE_DIR = os.path.dirname( os.path.dirname(os.path.abspath(__file__))) 
DATA_DIR = os.path.join(BASE_DIR,'data')

# Encontrando os arquivos de dados
files_names = [i for i in os.listdir(DATA_DIR) if i.endswith('.csv')]

# Abrindo uma conexão com o banco...
connection = sqlalchemy.create_engine(str_connection.format(path_to_data = os.path.join(DATA_DIR, 'olist.db')))

# Para cada Arquivo é realizado uma inserção no banco
for i in files_names:
    df_tmp = pd.read_csv(os.path.join (DATA_DIR, i))
    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset","")
    df_tmp.to_sql(table_name, connection)