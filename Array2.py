array=[]

total= 0

n=int(input("Masukan Jumlah elemen array :"))

for x in range (n) :
    nilai=float(input("Masukan nilai ke{} :". format(x+1)))
    array.append(nilai)
print("\nHasil nilai total adalah : {} ".format(sum(array)))
print("Nilai hasil Rata rata adalah : {}".format(sum(array)/n))