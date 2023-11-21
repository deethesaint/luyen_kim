import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def animateTSP(history, points):
    '''

        Danh sách tham số
        ----------
        history : list
            Danh sách tất cả các giải pháp đã được chọn bởi thuật toán
        points: array_like
            Danh sách các điểm với tọa độ
    '''

    ''' Tối đa 1500 frames cho toàn bộ quá trình mô phỏng đồ họa '''
    key_frames_mult = len(history) // 1500

    fig, ax = plt.subplots()

    ''' Vẽ đường thẳng bằng hàm plot - Đường thẳng này là đường giữa 2 Node được chọn là giải pháp'''
    line, = plt.plot([], [], lw=2)

    def init():
        ''' Tạo node '''
        x = [points[i][0] for i in history[0]]
        y = [points[i][1] for i in history[0]]
        plt.plot(x, y, 'co')

        ''' Tăng kích thước 2 trục lớn hơn 5% so với mặc định (Cho dễ quan sát :D)  '''
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

        ''' Khởi tạo giải pháp = rỗng '''
        line.set_data([], [])
        return line,

    def update(frame):
        ''' Update cứ mỗi frame thì cập nhật lại danh sách giải pháp '''
        x = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        y = [points[i, 1] for i in history[frame] + [history[frame][0]]]
        line.set_data(x, y)
        return line

    ''' Mô phỏng tiền tính toán (Cho dễ quan sát các đường thẳng và Node ban đầu) '''

    ani = FuncAnimation(fig, update, frames=range(0, len(history), key_frames_mult),
                        init_func=init, interval=3, repeat=False)

    plt.show()
