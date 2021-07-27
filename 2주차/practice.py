# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance-money-commission

# balance=0
# balance=deposit(balance, 1000)
# commission, balance=withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile( main_lang="자바", age=25, name="김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#" "JS")
# profile("김태호", 25, "kotlin", "swift")

# gun=10

# def checkpoint(soldiers):
#     global gun
#     gun=gun-soldiers
#     print("함수 내 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun=gun-soldiers
#     print("함수 내 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun=checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

# def std_weight(height, gender):
#     if gender=="남자":
#         weight=height*height*0.0001*22
#         print("키 {0}cm {1} 의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight,2)))
#     else:
#         weight=height*height*0.0001*21
#         print("키 {0}cm {1} 의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight, 2)))

# height=int(input())
# gender=input()

# std_weight(height, gender)

# import sys
# print("파이썬","자바", file=sys.stdout)
# print("파이썬","자바", file=sys.stderr)

# scores={"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # n칸의 공간을 확보하고 왼쪽/오른쪽 정렬

# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3)) # n칸의 공간을 확보하고 남는 자리는 0으로 채움

# answer=input("아무값이나 입력하세요 : ")
# print("입력하신 값은 "+answer+"입니다")




# 빈자리는 빈 공간으로 두고, 오른쪽 정렬, 총 10자리 확보
# print("{0: >10}".format(500))
# #양수일땐 +, 음수일땐 -표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _를 채움
# print("{0:_<+10}".format(500))
# #3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# #3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# #3자리 마다 콤마를 찍어주기, +- 부호도 붙이기, 자릿수 확보, 빈자리는 ^로 확보
# print("{0:^<30,}".format(-10000000000))
# #소숫점 출력
# print("{0:f}".format(5/3))
# #소숫점을 특정 자릿수까지만 표시
# print("{0:.2f}".format(5/3))





# score_file=open("score.txt", "w", encoding="UTF8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file=open("score.txt", "a", encoding="utf8") #a는 덮어쓰기(append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # .write로 하면 줄바꿈이 안된다. 주의
# score_file.close

# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close() #한번에 출력

# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한줄 읽고 커서는 다음줄 이동
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# while True:
#     line=score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# lines=score_file.readlines()
# for line in lines:
#     print(line)
# score_file.close()







# import pickle # 리스트나 클래스같이 텍스트가 아닌 자료형을 저장하려고 사용...
# # profile_file=open("profile.pickle", "wb")
# # profile={"이름":"박명수", "나이":30, "취미":["축구", "골프","코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # profile_file.close()

# profile_file=open("profile.pickle", "rb")
# profile=pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8")as study_file: # with 쓰면 pickle안써도 됨.
#     study_file.write("파이썬 공부중!")

# with open("study.txt", "r", encoding="utf8")as study_file:
#     print(study_file.read( ))






# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank=Unit("탱크", 150, 35)

# #레이스 : 공중유닛, 비행기. 클로킹(상대방에게 보이지 않음)
# wraith1=Unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대 유닛 뺏음
# wraith2=Unit("빼앗은 레이스", 80 , 5)
# wraith2.clocking=True # 객체에 원래 없었는데 추가로 객체를 할당

# if wraith2.clocking==True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))

#공격유닛

class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속받아옴
        self.damage=damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}".format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 스팀팩을 사용합니다.".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    seize_developed=False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode=False

    def set_seize_mode(self):
        if Tank.seize_developed==False:
            return

        if self.seize_mode==False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mode=True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage/=2
            self.seize_mode=False


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed= flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 {2}".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80,20,5)  
        self.clocked=False

    def clocking(self):
        if self.clocked==True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked=False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked=True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Player : gg")
    print("Player 님이 게임에서 퇴장하셨습니다.")

game_start()

m1=Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군이동
for unit in attack_units:
    unit.move("1시")

Tank.seize_developed=True
print("탱크 시즈모드 개발이 완료되었습니다.")


for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))

game_over()