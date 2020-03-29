#  psutil = process and system utilities
#  它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
#  支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块
import psutil

if __name__ == "__main__":
    # CPU逻辑数量
    print(psutil.cpu_count())
    # CPU物理核心
    print(psutil.cpu_count(logical=False))
    # 统计CPU的用户／系统／空闲时间
    print(psutil.cpu_times())
    # 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
    # for i in range(10):
    # print(psutil.cpu_percent(interval=1,percpu=True))

    # 获取物理内存和交换内存信息
    print(psutil.virtual_memory())
    print(psutil.swap_memory())

    # 获取磁盘分区、磁盘使用率和磁盘IO信息
    print(psutil.disk_partitions())
    print(psutil.disk_usage("/"))
    print(psutil.disk_io_counters())

    # 获取到所有进程的详细信息
    print(psutil.pids())
    # 获取指定进程ID=3776
    p = psutil.Process(896)
    print(p.name())
    print(p.ppid)
    print(p.children)

    # psutil还提供了一个test()函数，可以模拟出ps命令的效果
    psutil.test()
