#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_multi as tb


# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 아이디를 입력받습니다.
idfile = sys.argv[1]

# 트윗할 내용들이 적힌 파일을 입력받습니다.
filename = sys.argv[2]

# 아이디와 비밀번호를 세트로 저장해 둘 리스트를 만듭니다.
IDs = []

# 아이디가 기재된 파일을 불러옵니다.
idfile = open(idfile, encoding="utf-8")

# 이걸 한 줄씩 읽어옵니다.
for line in idfile:
    # 각 줄을 컴마로 쪼개 줍니다.
    splt = line.split(",")
    # 내용물이 두개가 아닌 라인은 모두 날려줍니다.
    if len(splt) != 2:
        continue
    # IDs에 아이디와 비밀번호를 저장합니다.
    IDs.append((splt[0].strip(), splt[1].strip()))

# 크롤러를 불러옵니다.
BOT = tb.TwitterBot(filename)

# IDs에 저장된 계정을 하나씩 불러옵니다.
for i in range(len(IDs)):
    # 로그인을 시도합니다.
    ID, PS = IDs[i]
    BOT.login(ID, PS)
    # 로그인에 성공했으니 스크린샷이나 한 번 찍어줍시다.
    BOT.save_screenshot(str(time.time) + ".png")
    # 트위터에 모든 멘션을 올립니다.
    BOT.tweet_all()
    time.sleep(10)
    # 크롤러를 닫아줍니다.
    BOT.kill()
    # 아직 작업이 덜 끝난 계정이 있다면
    if i < len(IDs)-1:
        # 크롤러를 다시 켜서 트위터로 접속합니다.
        BOT.go_to_twitter()
        time.sleep(3)


# 크롤러를 닫아줍니다.
BOT.kill()

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
