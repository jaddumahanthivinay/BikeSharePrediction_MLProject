from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': '<</PATH/TO/>>secure-connect-bikeshareprediction.zip'
}
auth_provider = PlainTextAuthProvider('gbtfDNAheHBnuDJZARulFNOo', 'DFx+DXOLmG2EI2wdA4t,fCqqSP0eScAbZy1Bjnx6n1TuWExiCK021k55P2SC4G-+WIsioIEOfZ,_j.-Y3MYMaQcIZZsNnGTXArSO3muSSUf2T8AEctChtmGCUkNmofY1')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

