import math
import random
import matplotlib.pyplot
import tsp_utils
import animated_visualizer


class LuyenKim:
    def __init__(self, coords, temp, alpha, stopping_temp, stopping_iter):
        '''

            Danh sách tham số
            ----------
            coords: array_like
                danh sách các tọa độ
            temp: float
                nhiệt độ khởi tạo
            alpha: float
                tỷ lệ nhiệt độ giảm
            stopping_temp: float
                nhiệt độ tối thiểu == dừng thuật toán
            stopping_iter: int
                số lần lặp tối đa == dừng thuật toán

        '''

        self.coords = coords
        self.sample_size = len(coords)
        self.temp = temp
        self.alpha = alpha
        self.stopping_temp = stopping_temp
        self.stopping_iter = stopping_iter
        self.iteration = 1

        self.dist_matrix = tsp_utils.vectorToDistMatrix(coords)
        self.curr_solution = tsp_utils.nearestNeighbourSolution(self.dist_matrix)
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

    def weight(self, sol):
        '''
        Tính trọng số
        '''
        return sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])

    def acceptance_probability(self, candidate_weight):
        '''
        Hàm P()
        Xác suất.
        Định nghĩa bằng công thức bên dưới:
        '''
        return math.exp(-abs(candidate_weight - self.curr_weight) / self.temp)

    def accept(self, candidate):
        '''
        Hàm so sánh chi phí giữa giải pháp mới và giải pháp cũ
        Nếu giải pháp mới tốt hơn thì cập nhật trọng số và giải pháp mới ở Node đang xét
        Nếu không thì sẽ chỉ đồng ý dựa theo xác suất của hàm P()
        '''
        candidate_weight = self.weight(candidate)
        if candidate_weight < self.curr_weight:
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
            if candidate_weight < self.min_weight:
                self.min_weight = candidate_weight
                self.best_solution = candidate

        else:
            if random.random() < self.acceptance_probability(candidate_weight):
                self.curr_weight = candidate_weight
                self.curr_solution = candidate

    def anneal(self):
        '''
        Sinh ra một giải pháp ngẫu nhiên
        '''
        while self.temp >= self.stopping_temp and self.iteration < self.stopping_iter:
            candidate = list(self.curr_solution)
            l = random.randint(2, self.sample_size - 1)
            i = random.randint(0, self.sample_size - l)

            candidate[i: (i + l)] = reversed(candidate[i: (i + l)])

            self.accept(candidate)
            self.temp *= self.alpha
            self.iteration += 1
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)

    def animateSolutions(self):
        animated_visualizer.animateTSP(self.solution_history, self.coords)

    def plotLearning(self):
        plt.plot([i for i in range(len(self.weight_list))], self.weight_list)
        line_init = plt.axhline(y=self.initial_weight, color='r', linestyle='--')
        line_min = plt.axhline(y=self.min_weight, color='g', linestyle='--')
        plt.legend([line_init, line_min], ['Trọng số khởi tạo', 'Trọng số tối ưu'])
        plt.ylabel('Trọng số')
        plt.xlabel('Lần lặp')
        plt.show()
