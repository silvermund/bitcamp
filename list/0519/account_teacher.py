class Account(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.BANK_NAME = 'SC은행'
        self.acc_number = self.create_acc_number()

    def create_acc_number(self):
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.create_acc_number = num1 + '-' + num2 + '-' + num3

    @staticmethod
    def del_account(ls, account):
        for i, j in enumerate(ls):
            if j.account == account:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('name'), input('balance')))
            elif menu == '2':
                for i in ls:
                    print(i.create_acc_number())
            elif menu == '3':
                name = input('이름')
                account = (input('계좌번호'), account)
                account.del_account(ls, account)
                ls.append(account)
            elif menu == '4':
                account = account(None, input('계좌번호'))
                account.del_account(ls, account)
            else :
                print('Wrong Number')
                continue

Account.main()