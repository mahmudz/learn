# -*- coding: utf-8 -*-
horas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
HI, HF = input().split()
HI = int(HI)
HF = int(HF)
aux = 0
if HI == HF:
    print("O JOGO DUROU 24 HORA(S)")
else:
    while HI != HF:
        if HI != 24:
            HI += 1
            aux += 1
        else:
            HI = 0;
    print("O JOGO DUROU %d HORA(S)"  %aux)