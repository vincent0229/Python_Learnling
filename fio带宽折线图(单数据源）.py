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
            timestamps.append(timestamp/1000/60)
            bandwidths.append(bandwidth/1024)
    return timestamps, bandwidths

# 绘制折线图
def plot_bandwidth(timestamps, bandwidths):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, bandwidths, marker='', linestyle='-', color='r')
    plt.title('FIO Bandwidth Over Time')
    plt.xlabel('Timestamp (min)')
    plt.ylabel('Bandwidth (MB/s)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 使用函数
file_path = 'C:\\Users\\Administrator\\Documents\\Python\\bw.log'  # 替换为实际的日志文件路径
timestamps, bandwidths = read_fio_log(file_path)
plot_bandwidth(timestamps, bandwidths)
