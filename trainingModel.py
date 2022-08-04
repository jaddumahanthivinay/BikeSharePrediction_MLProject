from sklearn.model_selection import train_test_split
from data_ingestion import data_loader_training
from data_preprocessing import preprocessing
from data_preprocessing import clustering
from best_model_finder import tuner
from file_operations import file_methods
from application_logging import logger



class trainModel:

    """ This class will be used to train the model """

    def __init__(self):
        self.log_writer = logger.App_Logger()
        self.file_object = open("Training_Logs/ModelTrainingLog.txt", 'a+')

    def trainingModel(self):
        self.log_writer.log(self.file_object, 'Training Started')
        try:
            # Getting the data from the source
            obtain_training_data = data_loader_training.Obtain_Training_Data(self.file_object,self.log_writer)
            data = obtain_training_data.get_data()

            # Data preprocessing
            # removing unnecessary columns
            preprocessor = preprocessing.Preprocessor(self.file_object,self.log_writer)
            data = preprocessor.remove_columns(data,['instant', 'yr', 'dteday', 'atemp', 'cnt', 'Unnamed: 0'])

            # checking if missing values are present in the dataset
            is_null_present = preprocessor.is_null_present(X)

            # if missing values are present, replacing them appropriately.
            if (is_null_present):
                X = preprocessor.impute_missing_values(X)  # missing value imputation

            # separating features and labels
            X, YC, YR = preprocessor.separate_label_feature(data, label1 = 'casual',label2 = 'registered')

            # Clustering
            kmeans = clustering.KMeansClustering(self.file_object,self.log_writer) # object initialization.
            number_of_clusters = kmeans.find_clusters(X)  #  using the elbow plot and knee locator to find the number of optimum clusters
            kmeans.save_model_kmeans(number_of_clusters, 'KMeans_model')

            # Dividing the data into clusters
            X = kmeans.create_clusters(X,number_of_clusters)

            # creating new columns in the dataset for labels
            X['casual'] = YC
            X['registered'] = YR

            # getting the unique clusters from dataset
            list_of_clusters = X['cluster'].unique()

            """parsing all the clusters and looking for the best ML algorithm to fit on individual cluster"""

            for i in list_of_clusters:
                cluster_data = X[X['cluster'] == i]
                cluster_features = cluster_data.drop(['casual', 'registered', 'cluster'], axis=1)
                cluster_label1 = cluster_data['casual']
                cluster_label2 = cluster_data['registered']
                x_train1, x_test1, y_train1, y_test1 = train_test_split(cluster_features, cluster_label1,test_size=0.20, random_state=300)
                x_train2, x_test2, y_train2, y_test2 = train_test_split(cluster_features, cluster_label2,test_size=0.20, random_state=300)

                # getting the best model for each of the clusters
                model_finder = tuner.Model_Finder(self.file_object,self.log_writer) # object initialization
                model_finder.best_model_casual(x_train1, y_train1, x_test1, y_test1)
                model_finder.best_model_registered(x_train2, x_test2, y_train2, y_test2)


            # logging the successful Training
            self.log_writer.log(self.file_object, 'Successful End of Training')
            self.file_object.close()

        except Exception:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception()