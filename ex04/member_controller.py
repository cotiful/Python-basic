# python -m pip install flask , flask= Spring 같은 framework
# python -m 은 파일이 있는 위치에 가게 해줌
# 파일 위치가 잘못돼있어서 pip install flask 로 해줌

from flask import Flask, request, jsonify
import member_dao as dao
# __name__ -> __main__
flask = Flask(__name__)

# controller 만듦


@flask.route("/my-member")
def list():

    return jsonify(dao.selset_all())


@flask.route("/my_member/<id>")
def detail(id):
    # **data key, value로 넣어줘야함 고정해서 id=1 이렇게 넣을 수 없음.
    return jsonify(dao.select_one(id=id))


@flask.route("/my-member/<id>", methods=['DELETE'])
def delete(id):
    return dao.delete_one(id=id)  # 1이 return 되면 잘됨, -1이면 잘 안됨


@flask.route("/my-member/<id>", methods=['PUT'])
def update(id):
    data = request.get_json()
    # dic 타입은 . 으로 하면 안됨 , 1 & -1 로 성공여부 확인
    return dao.update_one(id=id, username=data["username"], password=data["password"])


@flask.route("/my-member", methods=['POST'])
def save():
    # data = request.data -> x-www-urlencoded 받을 때 사용
    data = request.get_json()  # application/json 받을 때 사용
    return dao.insert_one(username=data["username"], password=data["password"])


flask.run(
    host="0.0.0.0",
    port=5001,
    debug=True  # 이 부분이 설정되면 파일 저장시 서버 자동 리로드 된다.
)
