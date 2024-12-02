import matplotlib.pyplot as plt

# 读取IOPS日志文件
def read_fio_iops_log(file_path):
    timestamps = []
    iops_values = []
    with open(file_path, 'r') as file:
        # 跳过可能的标题行
        next(file)
        for line in file:
            timestamp, iops = map(float, line.strip().split(','))
            timestamps.append(timestamp)
            iops_values.append(iops)
    return timestamps, iops_values

# 绘制折线图
def plot_iops(timestamps_list, iops_list, labels):
    plt.figure(figsize=(10, 6))
    for timestamps, iops, label in zip(timestamps_list, iops_list, labels):
        plt.plot(timestamps, iops, marker='', linestyle='-', label=label)
    plt.title('FIO IOPS Over Time')
    plt.xlabel('Timestamp (s)')
    plt.ylabel('IOPS')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 文件路径和标签
file_paths = ['C:\\Users\\Administrator\\Documents\\Python\\iops_1-128.log', 'C:\\Users\\Administrator\\Documents\\Python\\iops_2-64.log', 'C:\\Users\\Administrator\\Documents\\Python\\iops_4-32.log']  # 替换为实际的IOPS日志文件路径
labels = ['1-128', '2-64', '4-32']  # 数据的标签

# 读取所有文件的数据
data = [read_fio_iops_log(file_path) for file_path in file_paths]

# 提取时间戳和IOPS数据
timestamps_list = [d[0] for d in data]
iops_list = [d[1] for d in data]

# 绘制折线图
plot_iops(timestamps_list, iops_list, labels)
