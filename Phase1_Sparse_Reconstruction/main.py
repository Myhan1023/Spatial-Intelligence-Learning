import read_write_model  # 这行代码的意思是：在这个文件里调用旁边那个工具脚本
import os
import numpy as np  #

# 这里的路径一定要改成你存放 .bin 文件的那个 D 盘路径
input_model_path = r"D:\colmap\first_3d_project\sparse\0"

# 开始读取数据
cameras, images, points3D = read_write_model.read_model(path=input_model_path, ext=".bin")

print(f"成功读取！总共有 {len(images)} 张图片的信息。")

# 循环打印出每张图片的坐标
for image_id, image_data in images.items():  #用字典结构
    print(f"图片名: {image_data.name}")
    print(f"  坐标 (tvec): {image_data.tvec}")

# 把所有图片存入一个列表，方便用索引访问
image_list = list(images.values())
num_images = len(image_list)

print(f"\n--- 全局位移分析 (总计 {num_images} 张) ---")

# 假设我们将第一张照片作为参考基准 (Base)
base_img = image_list[0]
base_pos = base_img.tvec

print(f"基准图片: {base_img.name}  位置: {base_pos}\n")

# 使用 for 循环遍历剩下的图片
for i in range(1,num_images):
    current_img = image_list[i]
    current_pos = current_img.tvec

    # 计算相对于第一张图片的距离
    dist_from_base = np.linalg.norm(current_pos - base_pos)
    print(f"[{i}] 图片: {current_img.name}")
    print(f"    坐标: {current_pos}")
    print(f"    相对于基准的位移距离: {dist_from_base:.4f}")
    print("-" * 20)