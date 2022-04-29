from pymysql import connect, cursors

conn = connect(
    host="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"
)

# python 은 java(Result Set)와는 다르게 파싱해서 받아준다.
# python 은 기본 tuple로 받아준다.
cursor = conn.cursor(cursors.DictCursor)
