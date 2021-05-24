# 이름, 출생년도, 주소를 입력받아서 회원가입한 사람의 이름, 나이, 주소를 출력하시오.

class Person(object):
    def __init__(self, name, year, address) -> None:
        self.name = name
        self.year = year
        self.address = address
    def get_age(self):
        return 2021-self.year

    @staticmethod
    def main():
        p=Person(input('이름'), int(input('출생연도')), input('주소'))
        print(p.name)
        print(p.get_age())
        print(p.address)


Person.main()