'''
2.1 Feladat
Adott egy függvény. Értelmezési tartománya: [-3; 4] intervallumon az egész számok halmaza. Hozzárendelési szabálya: y = 2x-3.
A program egy lista formájában tárolja az értelmezési tartomány elemeit. Listaelemek leképezésével állítsa elő, tárolja listában és írja ki az értékkészlet elemeit.
'''
erttar = [i for i in range(-3, 4) ]

y = [2*i-3 for i in erttar]
print(y)