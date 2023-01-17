tugas= float(input("Masukan nilai tugas: "))
uts=float(input("Masukan nilai UTS: "))
uas= float(input("Masukan nilai UAS:"))

nilai= (0.15*tugas) + (0.38*uts) +  (0.50*uas)

if nilai > 80:
    grade= 'A'
elif nilai >70:
    grade= "B"
elif nilai >60:
    grade= "C"
elif nilai >50:
    grade= "D"
else:
    print("Grade= E")

if nilai > 60:
    status="lulus"
else:
    status="Tidak lulus"

print('Nilai akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))