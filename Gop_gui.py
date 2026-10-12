import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from pathlib import Path


def chay():
    thu_muc = filedialog.askdirectory(title="Chọn thư mục chứa file Excel")
    if not thu_muc:
        return

    files = list(Path(thu_muc).glob("*.xlsx"))
    if not files:
        messagebox.showwarning("Không có file", "Thư mục này không có file .xlsx")
        return

    try:
        danh_sach = [pd.read_excel(f) for f in files]
        gop = pd.concat(danh_sach, ignore_index=True)
        so_dong_goc = len(gop)

        gop.columns = gop.columns.astype(str).str.strip()
        gop = gop.dropna(how="all").drop_duplicates()

        ket_qua = Path(thu_muc) / "ket_qua.xlsx"
        gop.to_excel(ket_qua, index=False)

        messagebox.showinfo(
            "Hoàn tất",
            f"Đã gộp {len(files)} file\n"
            f"Dòng ban đầu: {so_dong_goc}\n"
            f"Dòng sau làm sạch: {len(gop)}\n"
            f"Đã xóa: {so_dong_goc - len(gop)} dòng\n\n"
            f"File kết quả: {ket_qua}",
        )
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra:\n{e}")


cua_so = tk.Tk()
cua_so.title("Gộp và làm sạch file Excel")
cua_so.geometry("360x160")

tk.Label(cua_so, text="Gộp & làm sạch file Excel", font=("Arial", 14, "bold")).pack(pady=15)
tk.Button(cua_so, text="Chọn thư mục và chạy", command=chay, width=24, height=2).pack()

cua_so.mainloop()