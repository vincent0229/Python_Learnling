import matplotlib.pyplot as plt

# 读取日志文件
def read_fio_log(file_path):
    timestamps = []
    bandwidths = []
    with open(file_path, 'r') as file:
        # 跳过可能的标题行
        next(file)
        for line in file:
            timestamp, bandwidth = map(float, line.strip().split(','))
            timestamps.append(timestamp/1000)
            bandwidths.append(bandwidth/1024)
    return timestamps, bandwidths

# 绘制折线图
def plot_bandwidth(timestamps_list, bandwidths_list, labels):
    plt.figure(figsize=(10, 6))
    for timestamps, bandwidths, label in zip(timestamps_list, bandwidths_list, labels):
        plt.plot(timestamps, bandwidths, marker='', linestyle='-', label=label)
    plt.title("Bandwidth over Timestamp ")
    plt.xlabel('Timestamp (s)')
    plt.ylabel('Bandwidth (MB/s)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 文件路径和标签
file_paths = ['C:\\Users\\Administrator\\Documents\\Python\\bw_1-128.log', 'C:\\Users\\Administrator\\Documents\\Python\\bw_2-64.log', 'C:\\Users\\Administrator\\Documents\\Python\\bw_4-32.log']  # 替换为实际的日志文件路径
labels = ['bw_1-128', 'bw_2-64', 'bw_4-32']  # 数据的标签

# 读取所有文件的数据
data = [read_fio_log(file_path) for file_path in file_paths]

# 提取时间戳和带宽数据
timestamps_list = [d[0] for d in data]
bandwidths_list = [d[1] for d in data]

# 绘制折线图
plot_bandwidth(timestamps_list, bandwidths_list, labels)
