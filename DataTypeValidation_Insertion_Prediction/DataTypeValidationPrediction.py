from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import shutil
from datetime import datetime
from os import listdir
import os
import csv
from application_logging.logger import App_Logger


class dBOperation:

    """ This class shall be used for handling all the Cassandra operations. """

    def __init__(self):
        self.path = '/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/Prediction_Database'
        self.badFilePath = "/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/Prediction_Raw_Files_Validated/Bad_Raw"
        self.goodFilePath = "/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/Prediction_Raw_Files_Validated/Good_Raw"
        self.logger = App_Logger()


    def dataBaseConnection(self,DatabaseName):

        """ This method opens the connection to the Cassandra DB. """

        try:
            cloud_config = {
                'secure_connect_bundle': '<</PATH/TO/>>secure-connect-bikeshareprediction.zip'
            }
            auth_provider = PlainTextAuthProvider('gbtfDNAheHBnuDJZARulFNOo',
                                                  'DFx+DXOLmG2EI2wdA4t,fCqqSP0eScAbZy1Bjnx6n1TuWExiCK021k55P2SC4G-+WIsioIEOfZ,_j.-Y3MYMaQcIZZsNnGTXArSO3muSSUf2T8AEctChtmGCUkNmofY1')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            file = open("/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/Prediction_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Opened database successfully")
            file.close()
        except ConnectionError:
            file = open("/Users/umadevipotnuru/PycharmProjects/BikeSharePrediction_new/Prediction_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Error while connecting to database: %s" %ConnectionError)
            file.close()
            raise ConnectionError


    def createTableDb(self,DatabaseName,column_names):

        """ This method creates a table in the given database which will be used to insert the Good data
            after raw data validation.
            On Failure: Raises Exception """

        try:
            cloud_config = {
                'secure_connect_bundle': '<</PATH/TO/>>secure-connect-bikeshareprediction.zip'
            }
            auth_provider = PlainTextAuthProvider('gbtfDNAheHBnuDJZARulFNOo',
                                                  'DFx+DXOLmG2EI2wdA4t,fCqqSP0eScAbZy1Bjnx6n1TuWExiCK021k55P2SC4G-+WIsioIEOfZ,_j.-Y3MYMaQcIZZsNnGTXArSO3muSSUf2T8AEctChtmGCUkNmofY1')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            CREATE TABLE BikeSharePrediction.GoodData(dteday PRIMARY KEY,season,yr,mnth,hr,holiday,weekday,workingday,weathersit,temp,atemp,hum,windspeed)
            if c.fetchone()[0] ==1:
                file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
                self.logger.log(file, "Tables created successfully!!")
                file.close()

                file = open("Training_Logs/DataBaseConnectionLog.txt", 'a+')
                self.logger.log(file, "Closed %s database successfully" % DatabaseName)
                file.close()

        except Exception as e:
            file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
            self.logger.log(file, "Error while creating table: %s " % e)
            file.close()
            file = open("Training_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Closed %s database successfully" % DatabaseName)
            file.close()
            raise e


    def insertIntoTableGoodData(self,Database):

        """ This method inserts the Good Data files from the Good_Raw folder into the above created table.
             On Failure: Raises Exception """

        goodFilePath= self.goodFilePath
        badFilePath = self.badFilePath
        onlyfiles = [f for f in listdir(goodFilePath)]
        log_file = open("Prediction_Logs/DbInsertLog.txt", 'a+')

        for file in onlyfiles:
            try:
                cloud_config = {
                    'secure_connect_bundle': '<</PATH/TO/>>secure-connect-bikeshareprediction.zip'
                }
                auth_provider = PlainTextAuthProvider('gbtfDNAheHBnuDJZARulFNOo',
                                                      'DFx+DXOLmG2EI2wdA4t,fCqqSP0eScAbZy1Bjnx6n1TuWExiCK021k55P2SC4G-+WIsioIEOfZ,_j.-Y3MYMaQcIZZsNnGTXArSO3muSSUf2T8AEctChtmGCUkNmofY1')
                cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
                session = cluster.connect()
                with open(goodFilePath+'/'+file, "r") as f:
                    next(f)
                    reader = csv.reader(f, delimiter="\n")
                $ COPY BikeSharePrediction.GoodData FROM 'reader.csv' WITH DELIMITER = '\n' AND HEADER = TRUE
                self.logger.log(log_file," %s: File loaded successfully!!" % file)
                log_file.close()

            except Exception as e:

                self.logger.log(log_file,"Error while creating table: %s " % e)
                shutil.move(goodFilePath+'/' + file, badFilePath)
                self.logger.log(log_file, "File Moved Successfully %s" % file)
                log_file.close()


    def selectingDatafromtableintocsv(self,Database):

        """ This method exports the data in GoodData table as a CSV file.
            On Failure: Raises Exception """

        log_file = open("Prediction_Logs/ExprtToCsv.txt", 'a+')
        try:
            cloud_config = {
                'secure_connect_bundle': '<</PATH/TO/>>secure-connect-bikeshareprediction.zip'
            }
            auth_provider = PlainTextAuthProvider('gbtfDNAheHBnuDJZARulFNOo',
                                                  'DFx+DXOLmG2EI2wdA4t,fCqqSP0eScAbZy1Bjnx6n1TuWExiCK021k55P2SC4G-+WIsioIEOfZ,_j.-Y3MYMaQcIZZsNnGTXArSO3muSSUf2T8AEctChtmGCUkNmofY1')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            COPY BikeSharePrediction.GoodData TO 'Prediction_FileFromDB/BikePredictionData.csv' | STDOUT [ WITH delimiter = '\n', header = 'true']
            self.logger.log(log_file, "File exported successfully!!!")
            log_file.close()

        except Exception as e:
            self.logger.log(log_file, "File exporting failed. Error : %s" % e)
            log_file.close()





