
# class MyException(Exception):
#     pass
# f = open(file) , Java는 컴파일 전에 try_catch 안 넣어주면 빨간줄 생기나 Python은 안 생김.


try:

    print(2/0)
except Exception() as e:
    print(e)
finally:
    print("무조건 실행됨")
