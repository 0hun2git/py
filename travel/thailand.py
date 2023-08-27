class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행되요.")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("외부에서 실행할 떄 실행되요.")