import os

os.system("dir")

# Os 명령어를 빌려서 현재 경로를 알아냄
workDir = os.path.abspath("./")
print(workDir)
