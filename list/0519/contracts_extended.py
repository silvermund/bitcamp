'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''
class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def get_contact(self):
        return f'주소록: 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}, 주소 {self.address}'
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.Exit 1.입력 2.출력 3.삭제 4.수정)
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소')))
            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.get_contact()}')
            elif menu == '3':
                del_name = input('삭제할 이름: ')
                for i, j in enumerate(ls):
                    if j.name == 'a':
                        del ls[i]
            elif menu == '4':
                edit_name = input('수정할 이름: ')
                edit_info - Contacts
                for i, j in enumerate(ls):
                    if j.name == 'a':
                        del ls[i]
            else:
                print('잘못된 주문입니다.')
                continue
Contacts.main()
