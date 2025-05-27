danhsach1 = [1.,3.]
danhsach2 = [5.,7.]
danhsach = danhsach1 + danhsach2
print(danhsach)
#kết quả [1.0, 3.0, 5.0, 7.0]
danhsach_gapdoi = 2*danhsach
print(danhsach_gapdoi)
#kết quả [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]
print(danhsach*2)
#kết quả [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]
#print(danhsach/2)
#kết quả TypeError: unsupported operand type(s) for /: 'list' and 'int'