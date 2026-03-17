# Spatial-Intelligence-Learning
软件工程大二学生空间智能自学记录

---

# 空间智能学习日志

## 第一阶段 - 稀疏重建与数据解析
> **项目状态**：Phase 1 完结（点云重构 + 坐标提取）

---

### 项目背景
作为一名软件工程专业大二学生，本项目旨在探索空间智能（Spatial Intelligence）的底层实现。
由于个人电脑硬件为 **ThinkBook 16+ 集显版**，本项目重点记录了如何在非独显环境下完成 3D 重建流程。

### 环境配置与排坑指南
1. **硬件限制 (No-CUDA)**：
   - 选择了 COLMAP 的 `nocuda` 编译版本，利用 CPU 代替 GPU 进行特征点匹配。虽然速度较慢，但成功跑通了整个流程。

### 第一阶段实现成果

---

#### 1. 自动化三维重建
利用ETH3D数据集status 11 张测试图像，通过COLMAP三维重建工具和 SfM (Structure from Motion) 算法成功恢复了场景的稀疏点云和相机运动轨迹。

#### 2. 二进制数据解析
编写 Python 脚本调用 `read_write_model.py`，将 COLMAP 生成的二进制文件（.bin）转化为可读的相机位姿数据。
* **关键实现**：使用 NumPy 批量计算了不同相机位置之间的欧式距离，实现了对相机运动幅度的量化。

#### 3. 运行截图
![COLMAP 3D点云效果](./colmap_result.png)
![PyCharm 坐标解析结果](./pycharm_output1.png)(./pycharm_output2.png)(./pycharm_output3.png)

---

### 文件夹说明
- `/Phase1_Sparse_Reconstruction`: 存放核心代码、导出的 .txt 坐标文件以及 .ply 模型文件。

### 下一步计划
- [ ] 在云端（Google Colab）尝试 3DGS (Gaussian Splatting) 渲染。
- [ ] 学习如何使用 MeshLab 进行点云清理与表面重建。
