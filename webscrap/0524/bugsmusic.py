class BugsMusic(object):

    url = ' '

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input(' 0.Exit\n 1.Input URL\n 2.Print URL'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URl')
            elif menu == 2:
                print(f'Input URL is {bugs}')
            else:
                print('Wrong Number')
                continue

BugsMusic.main()