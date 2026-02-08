#input: số giờ làm, lượng giờ, giờ tiêu chuẩn , giờ vượt chuẩn
#output: so tien thuc linh cua nhan vien

so_gio_lam = float(input("Nhap số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhap thù lao trên mỗi giờ lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Số tiền thuc linh cua nhan vien: {thuc_linh}")