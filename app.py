import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# 1. Tạo dữ liệu ban đầu
data = {
    "Ho_ten": [
        "Phuong Uyen",
        "Tran Minh",
        "Le Chi",
        "Thuy Dung",
        "Hoang Giang",
        "Vu Hanh",
        "Do Nhat",
        "Bui Lan",
        "Ngo Gia",
        "Vuong Nam",
    ],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 5, 9, 7, 4],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 4, 9, 6, 5],
    "Cuoi_ky": [9, 8, 7, 10, 6, 9, 5, 10, 7, 4],
}

df = pd.DataFrame(data, index=range(1, 11))

# 2. Tính điểm tổng kết (Chuyên cần 20%, Giữa kỳ 30%, Cuối kỳ 50%)
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]
)
df["Tong_ket"] = df["Tong_ket"].round(2)


# 3. Xếp loại sinh viên
def xep_loai(diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >= 7.0:
    return "Khá"
  elif diem >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# --- GIAO DIỆN STREAMLIT ---
st.set_page_config(
    page_title="Quản Lý Điểm Sinh Viên", page_icon="📚", layout="centered"
)

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Hiển thị bảng điểm
st.subheader("📋 Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

# Thống kê kết quả học tập
diem_trung_binh = df["Tong_ket"].mean()
diem_cao_nhat = df["Tong_ket"].max()
diem_thap_nhat = df["Tong_ket"].min()

sinh_vien_cao_nhat = df[df["Tong_ket"] == diem_cao_nhat]
sinh_vien_thap_nhat = df[df["Tong_ket"] == diem_thap_nhat]
so_sinh_vien_dat = (df["Tong_ket"] >= 5.0).sum()

st.subheader("📊 Thống kê chung của lớp")
col1, col2 = st.columns(2)
with col1:
  st.metric(
      label="Điểm trung bình của lớp", value=f"{diem_trung_binh:.2f}"
  )
  st.metric(label="Số sinh viên đạt (>= 5.0)", value=int(so_sinh_vien_dat))

with col2:
  st.write(
      f"**Điểm tổng kết cao nhất:** {diem_cao_nhat} ("
      f"{', '.join(sinh_vien_cao_nhat['Ho_ten'].tolist())})"
  )
  st.write(
      f"**Điểm tổng kết thấp nhất:** {diem_thap_nhat} ("
      f"{', '.join(sinh_vien_thap_nhat['Ho_ten'].tolist())})"
  )

# Danh sách xổ xuống (Selectbox) chọn sinh viên
st.subheader("🔍 Tra cứu thông tin cá nhân sinh viên")
selected_student = st.selectbox(
    "Chọn tên sinh viên để xem chi tiết:", df["Ho_ten"].tolist()
)

# Lọc thông tin sinh viên được chọn
student_info = df[df["Ho_ten"] == selected_student].iloc[0]
st.info(f"Thông tin chi tiết của **{selected_student}**:")
s_col1, s_col2, s_col3, s_col4, s_col5 = st.columns(5)
s_col1.metric("Chuyên cần", student_info["Chuyen_can"])
s_col2.metric("Giữa kỳ", student_info["Giua_ky"])
s_col3.metric("Cuối kỳ", student_info["Cuoi_ky"])
s_col4.metric("Tổng kết", student_info["Tong_ket"])
s_col5.metric("Xếp loại", student_info["Xep_loai"])

# Biểu đồ cột điểm tổng kết của 10 sinh viên
st.subheader("📈 Biểu đồ điểm tổng kết của sinh viên")
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(df["Ho_ten"], df["Tong_ket"], color="#1976D2")
ax.set_xlabel("Trục điểm")
import streamlit as st
import pandas as pd

st.subheader("Biểu đồ điểm tổng kết của sinh viên")
chart_data = df.set_index("Ho_ten")[["Tong_ket"]]
st.bar_chart(chart_data)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px; color: gray;'>Quản Nguyễn Phương Uyên - MSSV: [008308007984]</p>",
    unsafe_allow_html=True,
)
