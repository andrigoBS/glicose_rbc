from DataDTO import (DataDTO)
from Model import Model


class Main:
    def __init__(self, filename, verbose=True, log=print):
        self.verbose = verbose
        self.model = Model().load_data(filename)
        self.log = log

    def run(self, data_dto: DataDTO, trust=80):
        predicted_case, error, similarity = self.model.predict(data_dto)

        predicted_glucose = int(float(predicted_case[len(predicted_case) - 1]))
        predicted_glucose_string = [
            'Hipoglicemia',
            'Normal',
            'Hiperglicemia'
        ][predicted_glucose]

        if self.verbose:
            self.log('--------- Verbose mode -------------------------------------------')
            labels = [
                'gender', 'age', 'hypertension', 'heart_disease', 'smoking',
                'bmi', 'diabetes', 'fast', 'carbohydrates', 'glucose'
            ]
            data_in_array = data_dto.to_array()
            for i in range(len(data_in_array)):
                self.log('{}: input {} -> case {}'.format(labels[i], float(data_in_array[i]), predicted_case[i]))
            self.log('--------- Resultados ---------------------------------------------')

        self.log('Erro: {}'.format(error))
        self.log('Similaridade: {}%'.format(similarity))
        self.log('Nivel de glicose pedito: {}'.format(predicted_glucose_string))
        if similarity < trust:
            self.log('--------- Atenção ------------------------------------------------')
            self.log('O nivel de confiabilidade apresentado pelo sistema para este caso é muito baixo!')
            self.log('Por favor utilize o aparelho (Glicosímetro) para medir sua glicose!')


if __name__ == '__main__':
    Main('in/dataset_processed.csv').run(
        DataDTO()
        .set_gender(1)
        .set_age(23)
        .set_hypertension(0)
        .set_heart_disease(0)
        .set_smoking(0)
        .set_bmi(25.9)
        .set_diabetes(0)
        .set_fast(0)
        .set_carbohydrates(25)
    )
