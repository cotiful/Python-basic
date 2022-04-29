from unittest import result
import member_dao as dao

# 한건 insert


def set_data():
    result = dao.insert_one(username="hong", password="1234")
    print(f"result : {result}")

#  전체 가져오기 SELECT


def get_datas():
    my_members_entity = dao.selset_all()
    print(my_members_entity)

# 한 건 가져오기 select


def get_data():
    my_member_entity = dao.select_one(id=1)
    print(my_member_entity)

# 한 건 update 하기


def update_data():
    result = dao.update_one(id=1, username="kkk", password="8989")
    print(f"result:{result}")

# 한 건 삭제하기


def delete_data():
    result = dao.delete_one(id=1)
    print(f"result:{result}")

    delete_data()
