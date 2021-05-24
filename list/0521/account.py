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
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        while 1:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
                print('종료합니다.')
                break
            elif menu == '1':
                c = Account(input('예금주'), input('잔액'))
            elif menu == '2':
                print(f'출력결과: {c.get_account()}')
            elif menu == '3':
                name = input('예금주')
                account = (input('계좌번호'), account_number)
                account.del_account(ls, account_number)
                ls.append(account_number)
            elif menu == '4':
                account = account(None, input('계좌번호'))
                account.del_account(ls, account)
            else :
                print('Wrong Number')
                continue

Account.main()


