import os

def rename_directories():
    # 获取当前目录下的所有目录和文件
    for dir_name in os.listdir('.'):
        if os.path.isdir(dir_name):  # 仅处理目录
            print(f"    \"{dir_name}\",")

# 调用函数
rename_directories()
