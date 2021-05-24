
def test(a, b):
    return a+b


class Grade:
    
    def __init__(self, kor, eng, math) -> None:
        self.kor=kor
        self.eng=eng
        self.math=math


    def sum(self):
        return self.kor+self.eng+self.math
    def avg(self):
        return self.sum() / 3

if __name__ == '__main__':
    g=Grade(int(input('국어점수')), int(input('영어점수')), int(input('수학점수'))) 
    print(g.sum())
    

        
        

        


