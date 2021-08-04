class ThailandPackage:
    def detail(self):
        print("방콕, 파타야 여행, 50만원")

if __name__=="__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할때만 실행")
    trip_to=ThailandPackage()
    trip_to.detail()
else:
    print("thailand 외부에서 모듈 호출")