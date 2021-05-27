from main import PlugBoard, Reflector, Rotor, EnigmaMachine


if __name__ == '__main__':

    Basic = 3634002679907005990063343349387990626
    code = 3816522995074514006442698286220752001

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

    #エニグマコード復号化
    p = PlugBoard(n2(Basic))
    r1 = Rotor(n2(Basic), 3)
    r2 = Rotor(n2(Basic), 2)
    r3 = Rotor(n2(Basic), 1)
    reflector = Reflector(n2(code))

    #メインエンジン
    machine = EnigmaMachine(p, [r1, r2, r3], reflector)
    souce = 'node'
    d = machine.decrypt(souce)

    #一文字目を大文字化
    text = d.capitalize()