angka1=int(input('Masukkan Bilangan Awal :'))
angka2=int(input('Masukkan Batas Bilangan :'))

def prime(x):
    prim = True
    if x >= 2:
        for i in range (2,x):
            if x % i == 0:
                prim = False

    else:
        prim = False
    return prim
        
for i in range(angka1,angka2):
    if prime(i):
        print (i)
