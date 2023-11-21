from nodes_generator import NodeGenerator
from luyenkim import LuyenKim


def main():
    '''
    Các thông số ban đầu cho bài toán TSP
    
    temp: nhiệt độ
    stopping_temp: nhiệt độ dừng
    alpha: tỷ số giảm của nhiệt độ
    stopping_iter: số lần lặp tối đa
    
    '''
    temp = 1000 
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 10000000

    '''Thông số dài * rộng của ma trận'''
    size_width = 70
    size_height = 70

    '''Số lượng Node'''
    population_size = 25

    '''Tạo node ngẫu nhiên trên ma trận'''
    nodes = NodeGenerator(size_width, size_height, population_size).generate()

    '''Chạy thuật toán luyện kim'''
    sa = LuyenKim(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    '''Mô phỏng'''
    sa.animateSolutions()

    '''Cập nhật lại các giải pháp mới'''
    sa.plotLearning()


if __name__ == "__main__":
    main()
