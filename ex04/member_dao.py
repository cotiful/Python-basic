# DAO(Data Access Object)

from db import connect as db

# %s 사이에 (value)를 넣어서 바인딩 가능하다.
# insert_one(username="ssar", password="1234")


def insert_one(**data):  # {"username":"ssar", "password":"1234"}
    sql = "INSERT INTO my_member(username, password) VALUES(%(username)s, %(password)s)"

    try:
        db.cursor.execute(sql, data)  # 실행
    except Exception as e:  # 실패시
        print(e)  # 오류코드 출력
        db.conn.rollback()  # 롤백시키고
        return -1  # -1을 리턴

    db.conn.commit()  # 성공시 커밋
    return 1  # 1을 리턴

# SELECT는 try-catch를 안탄다.


def selset_all():
    sql = "SELECT * FROM my_member"
    db.cursor.execute(sql)
    rows = db.cursor.fetchall()  # 데이터 받기
    return rows


def select_one(**data):
    sql = "SELECT * FROM my_member WHERE id = %(id)s"
    db.cursor.execute(sql, data)
    row = db.cursor.fetchone()  # 데이터 받기
    return row


def update_one(**data):
    sql = "UPDATE my_member SET username=%(username)s, password=%(password)s WHERE id=%(id)s"

    try:
        db.cursor.execute(sql, data)  # 실행
    except Exception as e:  # 실패시
        print(e)  # 오류코드 출력
        db.conn.rollback()  # 롤백시키고
        return -1  # -1을 리턴

    db.conn.commit()  # 성공시 커밋
    return 1  # 1을 리턴


def delete_one(**data):
    sql = "DELETE FROM my_member WHERE id=%(id)s"

    try:
        db.cursor.execute(sql, data)  # 실행
    except Exception as e:  # 실패시
        print(e)  # 오류코드 출력
        db.conn.rollback()  # 롤백시키고
        return -1  # -1을 리턴
    db.conn.commit()  # 성공시 커밋
    return 1  # 1을 리턴
