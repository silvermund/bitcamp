import random

class Account(object):
    def __init__(self, owner, balance):
        self.BANK_NAME = 'SC은행'
        self.owner = owner
        self.balance = balance
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

    def get_account(self):
        return f'은행이름:{self.BANK_NAME}\n계좌번호:{self.owner}\n예금주{self.account_number}\n잔액{self.balance}'

    @staticmethod
    def main():
        while 1:
            menu = input('0.Exit 1.입력 2.출력')
            if menu == '0':
                print('종료합니다.')
                break
            elif menu == '1':
                c = Account(input('예금주'), input('잔액'))
            elif menu == '2':
                print(f'출력결과: {c.get_account()}')
                continue

Account.main()


