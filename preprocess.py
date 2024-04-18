import csv
import json


class Preprocess:
    def __init__(self):
        self.data = None
        self.original_dictionary = None

    def load_data(self, filename):
        csvfile = open(filename, newline='')
        data = csv.reader(csvfile)
        __headers = next(data)
        self.data = list(data)
        return self

    def load_original_dictionary(self, filename):
        file = open(filename).read()
        self.original_dictionary = json.loads(file)
        return self

    def save_preprocess(self, filename):
        file_out = open(filename, 'w')
        csv.writer(file_out, lineterminator='\n').writerows(self.data)
        file_out.close()
        return self

    def to_index_types(self):
        new_data = []
        for row in self.data:
            new_row = []
            for i in range(len(row)):
                if self.original_dictionary[i]['name'] == 'HbA1c_level':
                    continue
                if self.original_dictionary[i]['name'] == 'gender':
                    value = 0.0 if row[i] == 'Female' else 1.0
                elif self.original_dictionary[i]['name'] == 'smoking_history':
                    value = 0.0 if row[i] in ["No Info", "never", "former"] else 1.0
                else:
                    value = float(row[i])
                new_row.append(value)
            new_data.append(new_row)
        self.data = new_data
        return self

    def create_new_columns(self):
        for row in self.data:
            glucose = int(row[6])
            diabetes = int(row[7])
            fast = self.__get_fast_value_from_row(glucose, diabetes)
            glucose_level = self.__get_glucose_from_row(fast, glucose)
            carbohydrates = self.__get_carbohydrates(fast, diabetes, glucose)
            row.pop(6)
            row.append(float(fast))
            row.append(float(carbohydrates))
            row.append(float(glucose_level))
        return self

    def __get_fast_value_from_row(self, glucose, diabetes):
        tolerance = 126 if diabetes == 0 else 140
        fast = 1 if glucose < tolerance else 0
        return fast

    def __get_glucose_from_row(self, fast, glucose):
        if fast == 1:
            if glucose < 100:
                return 0
            if glucose < 126:
                return 1
            return 2
        if glucose < 140:
            return 0
        if glucose < 200:
            return 1
        return 2

    def __get_carbohydrates(self, fast, diabetes, glucose):
        if fast == 1:
            return 0
        if diabetes == 1:
            return glucose - 126
        return glucose - 100


if __name__ == '__main__':
    print('Start')

    Preprocess(). \
        load_data('in/dataset_original.csv'). \
        load_original_dictionary('data_dictionaries/original_data_dictionary.json'). \
        to_index_types(). \
        create_new_columns(). \
        save_preprocess('in/dataset_processed.csv')

    print('Finish')
