import os

root_dir = 'D:\dataset\\5_棉花病害数据\\5_fus'
# label_dir = 'screenshot'

img_path = os.path.join(root_dir)
# print(screenshot_img_path)

for idx, filename in enumerate(os.listdir(img_path)):

    new_name = f'5_fus{idx+1:04d}.jpg'
    new_path = os.path.join(img_path, new_name)  # 更改名字后需要放入的文件路径，需要加上名称

    os.rename(os.path.join(img_path, filename), new_path)  # old_name to new_name
    print(f'{filename} to {new_name}')