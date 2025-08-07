import html
import json

# Chuỗi bạn copy từ Tiki là một đoạn JSON string chứa HTML bị escape
raw_json = '"description": "\\u003Cp\\u003E\\u003Cstrong\\u003EĐồ Chơi Xếp Hình MyndToys \\u003C/strong\\u003E\\u003Cstrong\\u003E- ..."'

# Lấy phần sau dấu ":" (nếu cần), rồi xử lý
json_value_part = raw_json.split(":", 1)[1].strip()

# Xóa dấu phẩy cuối và dấu ngoặc kép đầu cuối
json_value_part = json_value_part.rstrip(',').strip('"')

# Giải mã unicode escape (\u003C -> <, etc.)
unicode_decoded = json_value_part.encode().decode('unicode_escape')

# Unescape HTML entities (&lt; -> <, etc.)
html_content = html.unescape(unicode_decoded)

# Ghi ra file HTML
with open("demo.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Đã tạo file demo.html. Mở bằng trình duyệt để xem kết quả.")
