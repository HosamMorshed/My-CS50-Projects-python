import qrcode
import os

# 1. البيانات اللي بدنا نحطها جوا الـ QR
# ممكن يكون رابط، نص، أو حتى رقم تليفون
data = "https://github.com/hossam-morshed" 

# 2. إعدادات الـ QR Code (شكل احترافي)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # حماية عالية من التلف
    box_size=10,
    border=4,
)

# 3. إضافة البيانات
qr.add_data(data)
qr.make(fit=True)

# 4. إنشاء الصورة مع ألوان مخصصة
# اخترت لك اللون الأزرق (قريب من شعار الشبكات) والخلفية بيضاء
img = qr.make_image(fill_color="blue", back_color="white")

# 5. حفظ الصورة
file_name = "hossam_github_qr.png"
img.save(file_name)

# 6. التأكد من النجاح
if os.path.exists(file_name):
    print("---" * 10)
    print(f"OK")
    print(f"{file_name}")
    print("---" * 10)
else:
    print("❌ NO")