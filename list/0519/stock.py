class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_infor(self):
        return f'주식 = Stock("{self.name}", "{self.code}")'

    @staticmethod
    def main():
        while 1:
            menu = input('0.Exit 1.입력 2.출력')
            if menu == '0':
                print('종료합니다.')
                break
            elif menu == '1':
                c = Stock(input('종목명'), input('종목코드'))
            elif menu == '2':
                print(f'출력결과: {c.get_infor()}')
                continue


Stock.main()
