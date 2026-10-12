import pandas as pd
from pathlib import Path

thu_muc = Path("data")
danh_sach = []

for file in thu_muc.glob("*.xlsx"):
    df = pd.read_excel(file)
    print(f"Đọc {file.name}: {len(df)} dòng")
    danh_sach.append(df)

gop = pd.concat(danh_sach, ignore_index=True)
so_dong_goc = len(gop)

# 1. Chuẩn hóa tên cột: bỏ khoảng trắng thừa
gop.columns = gop.columns.str.strip()

# 2. Xóa dòng trống hoàn toàn
gop = gop.dropna(how="all")

# 3. Xóa dòng trùng
gop = gop.drop_duplicates()

# 4. Xuất file kết quả
gop.to_excel("ket_qua.xlsx", index=False)

print("--- BÁO CÁO ---")
print(f"Số file đã gộp: {len(danh_sach)}")
print(f"Số dòng ban đầu: {so_dong_goc}")
print(f"Số dòng sau làm sạch: {len(gop)}")
print(f"Đã xóa: {so_dong_goc - len(gop)} dòng")
print(gop)