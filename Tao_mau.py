import pandas as pd
from pathlib import Path

Path("data").mkdir(exist_ok=True)

for i in range(1, 4):
    df = pd.DataFrame({
        " Ten SP ": ["Áo", "Quần", "Áo", None, "Giày"],
        "So luong": [10, 5, 10, None, 3],
        "Gia": [100000, 200000, 100000, None, 500000],
    })
    df.to_excel(f"data/file{i}.xlsx", index=False)

print("Đã tạo xong 3 file mẫu")