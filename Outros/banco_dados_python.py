import pymysql
#pip install PyMySQL  


conexao_db = pymysql.connect(db='nome_bd',user='root',passwd='')
#host='localhost',user='user',password='passwd',db='db',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor

cursor = conexao_db.cursor()
#criar um cursor(o nome da varável pode ser diferente de cursor, apenas botei para facilitar a leitura)
    #sua variavel da conexão do banco de dados concatenado com a função cursor()


cursor.execute("SELECT current_user()") #-> execute qualquer comando sql
# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao_db.commit()

aqui = cursor.fetchall()
#recuperar os resultados da query
for x in aqui:
    print(x)

# Finaliza a conexão
conexao_db.close()







