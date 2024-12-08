import json

# Đường dẫn tới file JSON
file_path = "F:/progress.json"

# Đọc và tải nội dung JSON
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)  # Load nội dung JSON

# In nội dung JSON với format đẹp
formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
print(formatted_json)git
