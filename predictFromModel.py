import pandas as pd
from file_operations import file_methods
from data_preprocessing import preprocessing
from data_ingestion import data_loader_prediction
from application_logging import logger
from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation


class prediction:

    """ This class will be used to predict using best regression model """

    def __init__(self,path):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.log_writer = logger.App_Logger()
        if path is not None:
            self.pred_data_val = Prediction_Data_validation(path)

    def predictionFromModel(self):

        try:
            self.pred_data_val.deletePredictionFile() #deletes the existing prediction file from last run!
            self.log_writer.log(self.file_object,'Start of Prediction')
            obtain_prediction_data = data_loader_prediction.Obtain_Prediction_Data(self.file_object,self.log_writer)
            data = obtain_prediction_data.get_data()

            # Data preprocessing
            # removing unnecessary columns
            preprocessor = preprocessing.Preprocessor(self.file_object, self.log_writer)
            data = preprocessor.remove_columns(data, ['instant', 'yr', 'dteday', 'atemp', 'cnt', 'Unnamed: 0'])

            # checking if missing values are present in the dataset
            is_null_present = preprocessor.is_null_present(data)

            # if missing values are present, replacing them appropriately.
            if (is_null_present):
                data = preprocessor.impute_missing_values(data)  # missing value imputation

            # loading cluster data
            kmeans = clustering.KMeansClustering(self.file_object, self.log_writer)  # object initialization.
            kmeans_model = kmeans.load_model_kmeans('KMeans_model')

            clusters = kmeans_model.predict(data)
            data['clusters'] = clusters
            clusters = data['clusters'].unique()
            file_loader = file_methods.File_Operation(self.file_object, self.log_writer)  # object initialization.
            for i in clusters:
                cluster_data = data[data['clusters']==i]
                cluster_data_prediction = cluster_data.drop(['clusters'],axis=1)

                casual_model_name = file_loader.find_correct_model_file_casual(i)
                casual_model = file_loader.load_model_casual(casual_model_name)
                casual_result = list(casual_model.predict(cluster_data_prediction))
                casual_result = pd.DataFrame(list(zip(casual_result)),columns=['casual_users'])
                cluster_data['casual_users'] = casual_result

                registered_model_name = file_loader.find_correct_model_file_registered(i)
                registered_model = file_loader.load_model_registered(registered_model_name)
                registered_result = list(registered_model.predict(cluster_data_prediction))
                registered_result = pd.DataFrame(list(zip(registered_result)), columns=['registered_users'])
                cluster_data['registered_users'] = registered_result

                path="/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/prediction_output_files/predictions.csv"
                cluster_data.to_csv("/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/prediction_output_files/predictions.csv",header=True,mode='a+') #appends result to prediction file
            self.log_writer.log(self.file_object,'End of Prediction')
        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the prediction!! Error:: %s' % ex)
            raise ex
        return path,"success"




