import pickle
import os
import shutil


class File_Operation:
    """ This class will be used save the model after training
        and load the saved model for prediction. """

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object


    def save_model_casual(self,model,filename):

        """ This method saves the model file for casual users to directory.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the save_model_casual method of the File_Operation class')
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/saved_models/casual'
        try:
            path = os.path.join(self.model_directory,filename) #create seperate directory for each cluster
            if os.path.isdir(path): #remove previously existing saved_models for each clusters
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path) #
            with open(path +'/' + filename+'.sav',
                      'wb') as f:
                pickle.dump(model, f) # save the model to file
            self.logger_object.log(self.file_object,
                                   'Model File '+filename+' saved. Exited the save_model_casual method of the File_Operation class')
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in save_model_casual method of the File_Operation class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,
                                   'Model File '+filename+' could not be saved. Exited the save_model_casual method of the File_Operation class')
            raise Exception()


    def load_model_casual(self,filename):

        """ This method loads the saved model for casual users.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the load_model_casual method of the File_Operation class')
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/saved_models/casual'
        try:
            with open(self.model_directory + filename + '/' + filename + '.sav',
                      'rb') as f:
                self.logger_object.log(self.file_object,
                                       'Model File ' + filename + ' loaded. Exited the load_model_casual method of the File_Operation class')
                return pickle.load(f)
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in load_model_casual method of the File_Opearation class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Model File ' + filename + ' could not be saved. Exited the load_model_casual method of the File_Operation class')
            raise Exception()


    def save_model_registered(self,model,filename):

        """ This method saves the model file for registered users to directory.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the save_model_registered method of the File_Operation class')
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/saved_models/registered'
        try:
            path = os.path.join(self.model_directory,filename) #create seperate directory for each cluster
            if os.path.isdir(path): #remove previously existing saved_models for each clusters
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path) #
            with open(path +'/' + filename+'.sav',
                      'wb') as f:
                pickle.dump(model, f) # save the model to file
            self.logger_object.log(self.file_object,
                                   'Model File '+filename+' saved. Exited the save_model_registered method of the File_Operation class')
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in save_model_registered method of the File_Operation class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,
                                   'Model File '+filename+' could not be saved. Exited the save_model_registered method of the File_Operation class')
            raise Exception()


    def load_model_registered(self,filename):

        """ This method loads the saved model for registered users.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the load_model_registered method of the File_Operation class')
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/saved_models/registered'
        try:
            with open(self.model_directory + filename + '/' + filename + '.sav',
                      'rb') as f:
                self.logger_object.log(self.file_object,
                                       'Model File ' + filename + ' loaded. Exited the load_model_registered method of the File_Operation class')
                return pickle.load(f)
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in load_model_registered method of the File_Opearation class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Model File ' + filename + ' could not be saved. Exited the load_model_registered method of the File_Operation class')
            raise Exception()


    def find_correct_model_file_casual(self,cluster_number):

        """ This method selects the correct model for casual users based on cluster number.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the find_correct_model_file_casual method of the File_Operation class')
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/saved_models/casual'
        try:
            self.cluster_number = cluster_number
            self.folder_name = self.model_directory
            self.list_of_model_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if (self.file.index(str( self.cluster_number))!=-1):
                        self.model_name=self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger_object.log(self.file_object,
                                   'Exited the find_correct_model_file_casual method of the File_Operation class.')
            return self.model_name
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in find_correct_model_file_casual method of the File_Operation class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Exited the find_correct_model_file_casual method of the File_Operation class with failure')
            raise Exception()


    def find_correct_model_file_registered(self,cluster_number):

        """ This method selects the correct model for registered users based on cluster number.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the find_correct_model_file_registered method of the File_Operation class')
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/saved_models/registered'
        try:
            self.cluster_number = cluster_number
            self.folder_name = self.model_directory
            self.list_of_model_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if (self.file.index(str( self.cluster_number))!=-1):
                        self.model_name=self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger_object.log(self.file_object,
                                   'Exited the find_correct_model_file_registered method of the File_Operation class.')
            return self.model_name
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in find_correct_model_file_registered method of the File_Operation class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Exited the find_correct_model_file_registered method of the File_Operation class with failure')
            raise Exception()