from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV

class Model_Finder:

    """ This class will be used to find the model with best accuracy. """

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.lr = LinearRegression()
        self.dt = DecisionTreeRegressor()
        self.svr = SVR()
        self.rf = RandomForestRegressor()
        self.lasso = LassoCV(cv=2)
        self.ridge = RidgeCV(cv=2)
        self.elastic = ElasticNetCV(cv=2)


    def best_model_casual(self,train_x,train_y,test_x,test_y):
        self.logger_object.log(self.file_object, 'Entered the best_model_casual method of the Model_Finder class')
        self.train_x = train_x
        self.train_y = train_y
        self.test_x = test_x
        self.test_y = test_y
        try:
            self.lr.fit(self.train_x, self.train_y)
            self.dt.fit(self.train_x, self.train_y)
            self.svr.fit(self.train_x, self.train_y)
            self.rf.fit(self.train_x, self.train_y)
            self.lasso.fit(self.train_x, self.train_y)
            self.ridge.fit(self.train_x, self.train_y)
            self.elastic.fit(self.train_x, self.train_y)
            self.lr_score = lr.score(self.test_x, self.test_y)
            self.dt_score = dt.score(self.test_x, self.test_y)
            self.svr_score = svr.score(self.test_x, self.test_y)
            self.rf_score = rf.score(self.test_x, self.test_y)
            self.lasso_score = lasso.score(self.test_x, self.test_y)
            self.ridge_score = ridge.score(self.test_x, self.test_y)
            self.elastic_score = elastic.score(self.test_x, self.test_y)
            self.maximum_score = max(self.lr_score, self.dt_score, self.svr_score, self.rf_score, self.lasso_score, self.ridge_score, self.elastic_score)
            if (self.maximum_score == self.lr_score):
                save_model_casual(lr, 'linear_regression' + str(i))
            elif (self.maximum_score == self.dt_score):
                save_model_casual(dt, 'decision_tree' + str(i))
            elif (self.maximum_score == self.svr_score):
                save_model_casual(svr, 'support_vector_regression' + str(i))
            elif (self.maximum_score == self.rf_score):
                save_model_casual(rf, 'random_forest' + str(i))
            elif (self.maximum_score == self.lasso_score):
                save_model_casual(lasso, 'lasso_regression' + str(i))
            elif (self.maximum_score == self.ridge_score):
                save_model_casual(ridge, 'ridge_regression' + str(i))
            elif (self.maximum_score == self.elastic_score):
                save_model_casual(elastic, 'elastic_regression' + str(i))
            self.logger_object.log(self.file_object,
                               'Casual model training and saving successful for cluster'+str(i))'. Exited the best_model_casual method of the Model_Finder class')
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in best_model_casual method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Casual model training and saving failed. Exited the best_model_casual method of the Model_Finder class')
            raise Exception()


    def best_model_registered(self,train_x,train_y,test_x,test_y):
        self.logger_object.log(self.file_object, 'Entered the best_model_registered method of the Model_Finder class')
        self.train_x = train_x
        self.train_y = train_y
        self.test_x = test_x
        self.test_y = test_y
        try:
            self.lr.fit(self.train_x, self.train_y)
            self.dt.fit(self.train_x, self.train_y)
            self.svr.fit(self.train_x, self.train_y)
            self.rf.fit(self.train_x, self.train_y)
            self.lasso.fit(self.train_x, self.train_y)
            self.ridge.fit(self.train_x, self.train_y)
            self.elastic.fit(self.train_x, self.train_y)
            self.lr_score = lr.score(self.test_x, self.test_y)
            self.dt_score = dt.score(self.test_x, self.test_y)
            self.svr_score = svr.score(self.test_x, self.test_y)
            self.rf_score = rf.score(self.test_x, self.test_y)
            self.lasso_score = lasso.score(self.test_x, self.test_y)
            self.ridge_score = ridge.score(self.test_x, self.test_y)
            self.elastic_score = elastic.score(self.test_x, self.test_y)
            self.maximum_score = max(self.lr_score, self.dt_score, self.svr_score, self.rf_score, self.lasso_score, self.ridge_score, self.elastic_score)
            if (self.maximum_score == self.lr_score):
                save_model_registered(lr, 'linear_regression' + str(i))
            elif (self.maximum_score == self.dt_score):
                save_model_registered(dt, 'decision_tree' + str(i))
            elif (self.maximum_score == self.svr_score):
                save_model_registered(svr, 'support_vector_regression' + str(i))
            elif (self.maximum_score == self.rf_score):
                save_model_registered(rf, 'random_forest' + str(i))
            elif (self.maximum_score == self.lasso_score):
                save_model_registered(lasso, 'lasso_regression' + str(i))
            elif (self.maximum_score == self.ridge_score):
                save_model_registered(ridge, 'ridge_regression' + str(i))
            elif (self.maximum_score == self.elastic_score):
                save_model_registered(elastic, 'elastic_regression' + str(i))
            self.logger_object.log(self.file_object,
                               'Registered model training and saving successful for cluster'+str(i))'. Exited the best_model_registered method of the Model_Finder class')
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in best_model_registered method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Registered model training and saving failed. Exited the best_model_registered method of the Model_Finder class')
            raise Exception()


