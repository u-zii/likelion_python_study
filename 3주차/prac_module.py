# import module
# module.price(3) # 3명이서 영화보러 갔을때 가격
# module.price_morning(4) # 4명이서 조조로 영화보러 갔을때 가격
# module.price_soldier(5) # 5명의 군인이 영화보러 갔을때 가격

# import module as mv
# mv.price(3)

# from module import *
# price(3)

# from module import price, price_morning
# price(5)
# price_soldier(5) // import를 안해줘서 쓸수가 없다.

# from module import price as a
# a(4)

# import travel.thailand # 모듈이나 클래스만 가능, 클래스는 import 불가
# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from 쓰면 가능
# trip_to=ThailandPackage()
# trip_to.detail()

# from travel import *
# # trip_to=thailand.ThailandPackage()
# # trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())