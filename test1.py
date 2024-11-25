
#修改文件名方法
import os

# 设置文件夹路径
folder_path = r"C:\Users\admin\Desktop\商品图"  # 注意加上 r，防止路径中的反斜杠被转义

# 获取文件夹中的所有文件并排序
files = sorted(os.listdir(folder_path))

# 初始化计数
count = 51

for file_name in files:
    # 检查是否为图片格式
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        # 生成新文件名
        new_name = f"{count}.jpg"
        # 获取文件的完整路径
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)
        # 重命名
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")
        count += 1

print("重命名完成！")
