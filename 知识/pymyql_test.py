

import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='saber2014',db='xinpianchang')
cur = conn.cursor()
sql = 'insert into test (id) values (4)'

cur.execute(sql)
conn.commit()
cur.close()
conn.close()