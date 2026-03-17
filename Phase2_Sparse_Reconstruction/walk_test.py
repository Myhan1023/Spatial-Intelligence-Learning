import trimesh #处理 3D 模型
import numpy as np

# 1. 加载模型
file_path = 'st.obj'
mesh = trimesh.load(file_path)

print(f"模型加载成功！包含 {len(mesh.vertices)} 个顶点，{len(mesh.faces)} 个三角面。")

# 2. 定义小人的起始位置（基于昨天算的相机坐标范围）
# 定义了小人散步的轨迹
start_x, end_x = 0.5, 1.5
y_sky = 10.0  # 小人从高空向下探测
z_pos = 3.8  # 固定一个深度

print(f"\n开始模拟小人散步探测高度：")
print("-" * 40)

# 核心
for x in np.linspace(start_x, end_x, 10):
    # 定义射线：起点在空中，方向垂直向下 [0, -1, 0]
    ray_origin = np.array([[x, y_sky, z_pos]]) #每次循环，起点X坐标都在变
    ray_direction = np.array([[0, -1, 0]]) #在3D坐标系里代表Y轴负方向

    # 执行射线检测：寻找交点
    # locations: 返回射线撞击到模型表面的坐标点。如果没撞到，它就是空的
    # index_tri: 它甚至能告诉你撞到了模型上的哪一个三角形
    locations, index_ray, index_tri = mesh.ray.intersects_location(
        ray_origins=ray_origin,
        ray_directions=ray_direction
    )

    if len(locations) > 0:
        # 拿第一个交点（地面）
        ground_height = locations[0][1]
        print(f"坐标 (x={x:.2f}, z={z_pos:.2f}) -> 踩到了！高度 y={ground_height:.4f}")
    else:
        print(f"坐标 (x={x:.2f}, z={z_pos:.2f}) -> 哎呀！踩空了，下面是悬崖！")

print("-" * 40)
print(" 探测结束。这些高度差就是机器人需要感知的高低起伏。")