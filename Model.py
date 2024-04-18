import csv

from DataDTO import DataDTO


class Model:
    def __init__(self):
        self.data = None
        self.weights = [1, 1, 2, 2, 2, 3, 6, 5, 4]

    def load_data(self, filename):
        csvfile = open(filename, newline='')
        data = csv.reader(csvfile)
        self.data = list(data)
        return self

    def predict(self, data_dto: DataDTO):
        data_in_array = data_dto.to_array()
        max_values = self.get_max_values()

        best_case = None
        best_global_error = 1000000

        for row in self.data:
            global_error = 0
            for i in range(len(row) - 1):
                global_error += self.__get_error_value(
                    float(row[i]),
                    data_in_array[i],
                    self.weights[i],
                    max_values[i]
                )
            if global_error < best_global_error:
                best_global_error = global_error
                best_case = row

        similarity = round((1 - best_global_error) * 100, 2)
        if similarity < 0:
            similarity = 0

        return best_case, best_global_error, similarity

    def __get_error_value(self, case_value, in_value, weight, max_value):
        pondered_case_value = self.__ponderate_value(case_value, weight, max_value)
        pondered_in_value = self.__ponderate_value(in_value, weight, max_value)
        return abs(pondered_case_value - pondered_in_value)

    def __ponderate_value(self, value, weight, max_value):
        return value / max_value * weight

    def get_max_values(self):
        max_values = [0 for _ in range(len(self.data))]

        for row in self.data:
            for i in range(len(row) - 1):
                if float(row[i]) > max_values[i]:
                    max_values[i] = float(row[i])
        return max_values
