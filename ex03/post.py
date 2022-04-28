# constructor 키워드
# self 는 heap 공간

class Post:
    def __init__(self, username, password):
        self.username = username
        self.password = password


p = Post("ssar", "1234")

# class를 dict으로 바꾸는 방법
print(p.__dict__)

print(p.username)
