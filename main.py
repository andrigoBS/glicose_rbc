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
            self.log('coluna: caso corrente -> caso escolhido da base de casos')
            labels = [
                'gender', 'age', 'hypertension', 'heart_disease', 'smoking',
                'bmi', 'diabetes', 'fast', 'carbohydrates', 'glucose'
            ]
            data_in_array = data_dto.to_array()
            for i in range(len(data_in_array)):
                self.log('{}: {} -> {}'.format(labels[i], float(data_in_array[i]), predicted_case[i]))
            self.log('--------- Resultados ---------------------------------------------')

        self.log('Erro: {}'.format(error))
        self.log('Similaridade: {}%'.format(similarity))
        self.log('Nivel de glicose predito: {}'.format(predicted_glucose_string))
        if similarity < trust:
            self.log('--------- Atenção ------------------------------------------------')
            self.log('O nivel de confiabilidade apresentado pelo sistema para este caso é muito baixo!')
            self.log('Por favor utilize o aparelho (Glicosímetro) para medir sua glicose!')


if __name__ == '__main__':
    main = Main('in/dataset_processed.csv')
    print('Caso 1')
    main.run(
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
    print('')
    print('Caso 2')
    main.run(
        DataDTO()
        .set_gender(1)
        .set_age(23)
        .set_hypertension(0)
        .set_heart_disease(1)
        .set_smoking(0)
        .set_bmi(25.9)
        .set_diabetes(0)
        .set_fast(1)
        .set_carbohydrates(0)
    )
    print('')
    print('Caso 3')
    main.run(
        DataDTO()
        .set_gender(0)
        .set_age(90)
        .set_hypertension(0)
        .set_heart_disease(0)
        .set_smoking(0)
        .set_bmi(25.9)
        .set_diabetes(1)
        .set_fast(0)
        .set_carbohydrates(25)
    )
