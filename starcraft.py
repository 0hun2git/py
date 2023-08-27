# station = "사당"
# print( station+"행 열차가 들어오고 있습니다." )
# station = "신도림"
# print( station+"행 열차가 들어오고 있습니다." )
# station = "인천공항"
# print( station+"행 열차가 들어오고 있습니다." 

#from random import *
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정 되었습니다.") # str(int(random()*26)+3)

#url = "http://naver.com"
# url = "http://youtube.com"
# my_url = url.replace("http://","")
# my_url = my_url[:my_url.index(".")]
# print(my_url[:3]+str(len(my_url))+str(url.count("e"))+"!")

# from random import *
# list =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(list)
# winner = sample(list,4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자: {}".format(winner[0]))
# print("커피 당첨자: {}".format(winner[1:4]))
# print("축하합니다.")


# weather = input("오늘날씨는 어때요? ")
# if weather == "비":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스클을 챙기세요.")
# else:
#     print("준비물 필요 없어요.")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {}".format(waiting_no))

# from random import *
# total = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <=15:
#         print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         total += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {}분".format(total))

# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height*22
#     else:
#         return height*height*21
# height = 175
# gender = "남자"
# average = round(std_weight(height/100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, average))

# for i in range(1, 51):
#     # report_file = open("{}주차.txt".format(i), "w", encoding="utf8") # 처음쓰기
#     # print(" - {} 주차 주간보고 -".format(i), file=report_file)
#     # print("부서: ", file=report_file)
#     # print("이름: ", file=report_file)
#     # print("업무 요약: ", file=report_file)
#     # report_file.close(), # 파일 닫기
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" - {} 주차 주간보고 -".format(i))
#         report_file.write("\n부서: ")
#         report_file.write("\n이름: ")
#         report_file.write("\n업무 요약: ")

# 스타크래프트
# name = "마린"
# hp = 40
# damage = 5
# print("{0}유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
# def attack(name, location, damage):
#     print("{0}: {1} 방향으로 적군을 공격합니다. [공격력: {2}]".format(name, location, damage))
# attack(name, "1시", damage)

# 일반유닛
# class Unit: # 객체
#     def __init__(self, name, hp, speed):#, damage): # __init__ 생성자 / name, hp, damage 인스턴스
#         self.name = name # 멤버변수
#         self.hp = hp # 멤버변수
#         self.speed = speed # 멤버변수
#         #self.damage = damage # 멤버변수
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         #print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#         print("체력 {0}".format(self.hp,))

#     def move(self, location):        
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
#     def damaged(self, damage): # 메소드
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank1 = Unit("탱크", 150, 35)
# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 외부에서 멤버변수 호출
# # wraith2 = Unit("빼앗은 레이스", 80, 5)
# # wraith2.clocking = True # 외부에서 멤버변수 추가

# # if wraith2.clocking == True:
# #     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.clocking))

# # 날 수 있는 기능
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(name, location, self.flying_speed))

# # 공격유닛
# class AttackUnit(Unit): # 상속
#     def __init__(self, name, hp, speed, damage): # __init__ 생성자 / name, hp, damage 인스턴스
#         #self.name = name # 멤버변수
#         #self.hp = hp # 멤버변수
#         Unit.__init__(self, name, hp, speed) # 상속
#         self.damage = damage # 멤버변수
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

#     def attack(self, location): # 메소드
#         print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
#     # def damaged(self, damage): # 메소드
#     #     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#     #     self.hp -= damage
#     #     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#     #     if self.hp <=0:
#     #         print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16, 3) # 객체
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location): # 메소드 오버라이딩 move() 재정의
#         self.fly(self.name, location)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name,hp,0) # super 다중 상속에서는 X
#         self.location = location
#         pass

# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("player: gg")
#     print("[player]님이 게임에서 퇴장하셨습니다.")
#     pass

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
    
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0}: 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False
    
#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
#             #print("{0}: 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage*=2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드로 해재합니다.".format(self.name))
#             self.damage/=2
#             self.set_seize_mode = False

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clockef = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clockef = True

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
# t1 = Tank()
# t2 = Tank()
# w1 = Wraith()

# attack_unit=[]
# attack_unit.append(m1)
# attack_unit.append(m2)
# attack_unit.append(m3)
# attack_unit.append(t1)
# attack_unit.append(t2)
# attack_unit.append(w1)

# for unit in attack_unit:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# for unit in attack_unit:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# for unit in attack_unit:
#     unit.attack("1시")

# for unit in attack_unit:
#     unit.damaged(randint(5,21))

# game_over()
# class SoldOutError(Exception):
#     def __init__(self):
#         pass

# chicken = 10
# waiting = 1
# while(True):
#     print("[남은치킨 : {0}]".format(chicken))
#     try:
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order <= 0:
#             raise ValueError
#         elif order > chicken:
#             print("재료가 부족합니다.")
#         else: 
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력 하였습니다.")
#     except SoldOutError:
#         print("매진 되었습니다.")
#         break

# import theater_module # 모듈
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv # 모듈
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# from theater_module import price_soldier as price
# price(5)

# import travel.thailand
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()
# from travel.vietnam import VietnamPackage
# trip_to = VietnamPackage()
# trip_to.detail()

# from travel import *
# trip_tp = vietnam.VietnamPackage()
# trip_tp.detail()
# trip_tp = thailand.ThailandPackage()
# trip_tp.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())
# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import sign
sign.sign()


