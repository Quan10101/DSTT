mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
anh_xa_list = list(anh_xa)
print("Kết quả zip (anh_xa):")
#[(2, 'ToanCC', 10), (3, 'DSTT', 9), (4, 'ToanRR', 8), (1, 'LaptrinhCB', 7)]
print(anh_xa_list)
tap_hop = set(anh_xa_list)
print("Tập hợp tap_hop:")
#{(1, 'LaptrinhCB', 7), (2, 'ToanCC', 10), (4, 'ToanRR', 8), (3, 'DSTT', 9)}
print(tap_hop)
lay_TT, lay_monhoc, lay_diem = zip(*tap_hop)
print("Danh sách thứ tự:", lay_TT)
print("Danh sách môn học:", lay_monhoc)
print("Danh sách điểm:", lay_diem)
#Danh sách thứ tự: (1, 2, 4, 3)
#Danh sách môn học: ('LaptrinhCB', 'ToanCC', 'ToanRR', 'DSTT')
#Danh sách điểm: (7, 10, 8, 9)