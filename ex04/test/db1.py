# python -m pip install pymysql
from db import connect as db

# INSERT 쿼리
insert_sql = "INSERT INTO my_member(username, password) VALUES(%s, %s)"
db.cursor.execute(insert_sql, ["love", "1234"])  # buffer로 통신하기(실행) (쿼리, [배열])
db.conn.commit()  # 커밋해주기
