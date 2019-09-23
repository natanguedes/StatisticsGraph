
import pymysql
import matplotlib.pyplot as plt

db = pymysql.connect("localhost","root","","Produto" )
cursor = db.cursor()# executa SQL usando método execute()
cursor.execute("SELECT * from marca where marcafk='1'")# Busca uma linha usando método fetchone()
data = cursor.fetchone()
plt.plot( [10,5] ) #[primeira coluna , segunda coluna ]
plt.show()
print(data)
