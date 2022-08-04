import pandas as pd

class Obtain_Prediction_Data:

    """ This class will obtain the data from the source for prediction. """

    def __init__(self, file_object, logger_object):
        self.prediction_file='/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/Prediction_Batch_files/bikeshare_prediction_data.csv'
        self.file_object=file_object
        self.logger_object=logger_object

    def get_data(self):

        """ This method reads the data from source into a pandas dataframe. It also raises exception if fails. """

        self.logger_object.log(self.file_object,'Entered the get_data method of Obtain_Prediction_Data class')
        try:
            self.data= pd.read_csv(self.prediction_file) # reading the data file
            self.logger_object.log(self.file_object,'Data Load Successful. Exited the get_data method of Obtain_Prediction_Data class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_data method of Obtain_Prediction_Data class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful. Exited the get_data method of Obtain_Prediction_Data class')
            raise Exception()


