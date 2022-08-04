from sklearn.cluster import KMeans
from kneed import KneeLocator


class KMeansClustering:
    """ This class will be used to divide the data into clusters """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object


    def find_clusters(self,data):

        """ This method saves the plot to decide the optimum number of clusters to the file.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the find_clusters method of the KMeansClustering class')
        wcss=[] # initializing an empty list
        self.data = data
        try:
            for i in range(1, 17):
                kmeans = KMeans(n_clusters=i, init='k-means++', random_state=30)
                kmeans.fit(self.data)
                wcss.append(kmeans.inertia_)
            self.kn = KneeLocator(range(1, 17), wcss, curve='convex', direction='decreasing')
            self.logger_object.log(self.file_object, 'The optimum number of clusters is: '+str(self.kn.knee)+'. Exited the elbow_plot method of the KMeansClustering class')
            return self.kn.knee
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in find_clusters method of the KMeansClustering class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Finding the number of clusters failed. Exited the find_clusters method of the KMeansClustering class')
            raise Exception()


    def create_clusters(self,data,number_of_clusters):

        """ This method creates a new dataframe consisting of the cluster information.
            On Failure: Raises Exception """

        self.logger_object.log(self.file_object, 'Entered the create_clusters method of the KMeansClustering class')
        self.data=data
        self.number_of_clusters = number_of_clusters
        try:
            self.kmeans = KMeans(n_clusters=self.number_of_clusters, init='k-means++', random_state=30)
            self.y_kmeans = self.kmeans.fit_predict(data) #  divide data into clusters
            self.data['Cluster'] = self.y_kmeans  # create a new column in dataset for storing the cluster information
            self.logger_object.log(self.file_object, 'succesfully created '+str(self.kn.knee)+ 'clusters. Exited the create_clusters method of the KMeansClustering class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in create_clusters method of the KMeansClustering class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Fitting the data to clusters failed. Exited the create_clusters method of the KMeansClustering class')
            raise Exception()


    def save_model_kmeans(self, number_of_clusters, filename):

        """ This method saves the kmeans model used for training. """

        self.number_of_clusters = number_of_clusters
        self.kmeans = KMeans(n_clusters=self.number_of_clusters, init='k-means++', random_state=30)
        self.logger_object.log(self.file_object, 'Entered the save_model_kmeans method of the KMeansClustering class')
        self.filename = filename
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/kmeans'
        try:
            path = os.path.join(self.model_directory, self.filename)
            if os.path.isdir(path):
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)
            with open(path + '/' + self.filename + '.sav', 'wb') as f:
                pickle.dump(self.kmeans, f)
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in save_model_kmeans method of the KMeansClustering class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Saving the kmeans model failed. Exited the save_model_kmeans method of the KMeansClustering class')
            raise Exception()


    def load_model_kmeans(self, filename):

        """ This method loads the kmeans model used for training. """

        self.logger_object.log(self.file_object, 'Entered the load_model_kmeans method of the KMeansClustering class')
        self.filename = filename
        self.model_directory = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/kmeans/'
        try:
            with open(model_directory + self.filename + '/' + self.filename + '.sav', 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in load_model_kmeans method of the KMeansClustering class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Loading the kmeans model failed. Exited the load_model_kmeans method of the KMeansClustering class')
            raise Exception()