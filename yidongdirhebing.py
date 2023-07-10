import os
import shutil

def move_files(source_folders, target_folder):
    for folder in source_folders:
        # 获取源文件夹中的所有文件
        files = os.listdir(folder)
        for file in files:
            # 构建源文件的完整路径
            source_file = os.path.join(folder, file)
            # 构建目标文件的完整路径
            target_file = os.path.join(target_folder, file)
            # 移动文件
            shutil.move(source_file, target_file)
    print("move completeed.")

# 源文件夹列表
source_folders = ["00img", "11img", "22img", "33img", "44img", "55img", "66img", "77img", "img2"]

# 目标文件夹
target_folder = "images/train"

# 移动文件
move_files(source_folders, target_folder)
