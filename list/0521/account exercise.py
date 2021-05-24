import random

class Account(object):

    def __init__(self, account_number, name, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def to_string(self):
        return f'Bank Name:' {self.BANK_NAME},' \
               f'Name: {self.name},'\
               f'Account Number: {self.account_number},' \
               f'Money: {self.money}'


    @staticmethod
    def create_account_number():
        ls = [str(random.radnint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))
        return "".join(ls)


    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2. 계좌내용 3.입금 4.출금 5.계좌탈퇴')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(Account.create_account_number()))