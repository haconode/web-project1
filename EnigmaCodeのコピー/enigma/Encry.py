import random
from main import ALPHABET, PlugBoard, Reflector, Rotor, EnigmaMachine


if __name__ == '__main__':
   
    Basic = 3634002679907005990063343349387990626

    #初期値配列定義
    num2alpha = lambda c: chr(c+64)
    n2 = num2alpha

    def n2(num):
        if num <= 26:
            return chr(64+num)

        elif num % 26 == 0:
            return n2(num//26-1)+chr(90)

        else:
            return n2(num//26)+chr(64+num%26)

    #エニグマコード暗号化
    p = PlugBoard(n2(Basic))
    r1 = Rotor(n2(Basic), 3)
    r2 = Rotor(n2(Basic), 2)
    r3 = Rotor(n2(Basic), 1)

    r = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes)/2)):
        x = indexes.pop(random.randint(0, len(indexes)-1))
        y = indexes.pop(random.randint(0, len(indexes)-1))
        r[x], r[y] = r[y], r[x]
    reflector = Reflector(''.join(r))

    #メインエンジン
    machine = EnigmaMachine(p, [r1, r2, r3], reflector)
    source = 'kjhiaxehao'
    e = machine.encrypt(source)

    #エニグマコードパス作成
    alpha2num = lambda c: ord(c) - ord('A') + 1
    a2 = alpha2num

    def a2(alpha):
        num = 0

        for index, item in enumerate(list(alpha)):
            num += pow(26, len(alpha)-index-1)*(ord(item)-ord('A')+1)
        return num
    
    code = a2(''.join(r))
