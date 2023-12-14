import math
import random
import numpy as np


def vectorToDistMatrix(coords):
    '''
    Tạo ma trận kề
    '''
    return np.sqrt((np.square(coords[:, np.newaxis] - coords).sum(axis=2)))


def nearestNeighbourSolution(dist_matrix):
    '''
    Tính giải pháp khởi tạo (Phương pháp là lấy là thuật toán NearestNeighbor - một thuật toán dùng để giải quyết TSP nhưng kém tối ưu hơn so với)
    -- Giải thích: Giải pháp khởi tạo là các giải pháp được tạo ra một cách ngẫu nhiên
    khi vừa execute chương trình.
    -- Các giải pháp của bài toán TSP sẽ được update theo thời gian.
    '''
    node = random.randrange(len(dist_matrix))
    result = [node]

    nodes_to_visit = list(range(len(dist_matrix)))
    nodes_to_visit.remove(node)

    while nodes_to_visit:
        nearest_node = min([(dist_matrix[node][j], j) for j in nodes_to_visit], key=lambda x: x[0])
        node = nearest_node[1]
        nodes_to_visit.remove(node)
        result.append(node)

    return result
