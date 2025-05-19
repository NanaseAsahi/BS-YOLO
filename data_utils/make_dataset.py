import os
import shutil
import random

def move_files(src_folder, dest_folder):
    """移动文件夹下的所有文件到目标文件夹"""
    # 遍历源文件夹中的子文件夹 (train, test, val)
    for subfolder in ['train', 'test', 'val']:
        subfolder_path = os.path.join(src_folder, subfolder)
        if os.path.exists(subfolder_path):
            # 遍历子文件夹中的所有文件
            for file_name in os.listdir(subfolder_path):
                src_file = os.path.join(subfolder_path, file_name)
                dest_file = os.path.join(dest_folder, file_name)
                if os.path.isfile(src_file):
                    shutil.move(src_file, dest_file)
            # 删除空子文件夹
            os.rmdir(subfolder_path)

def create_val_txt(images_folder, val_ratio=0.1):
    """根据指定的验证集比例创建val.txt文件"""
    # 获取所有图片文件
    all_images = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
    
    # 计算验证集的数量
    val_count = int(len(all_images) * val_ratio)
    
    # 随机选择验证集图片
    val_images = random.sample(all_images, val_count)
    
    # 写入val.txt文件
    val_txt_path = os.path.join(images_folder, 'val.txt')
    with open(val_txt_path, 'w') as f:
        for img in val_images:
            img_path = os.path.join(images_folder, img)
            f.write(img_path + '\n')

def main():
    # 定义图片和标签文件夹路径
    images_folder = 'D:/yolo/yolodatasets/images'  # 替换为你的images文件夹路径
    labels_folder = 'D:/yolo/yolodatasets/labels'  # 替换为你的labels文件夹路径
    
    # 移动图片和标签文件
    move_files(images_folder, images_folder)  # 将图片文件移动到images文件夹下
    move_files(labels_folder, labels_folder)  # 将标签文件移动到labels文件夹下
    
    # 创建val.txt文件
    create_val_txt(images_folder, val_ratio=0.1)

    print("文件移动和验证集划分完成！")

if __name__ == '__main__':
    main()
