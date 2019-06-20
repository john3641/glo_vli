import pandas as pd
import geopandas as gpd
import os
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import *

from tethysapp.glo_vli.app import GloVli as app
from tethysapp.glo_vli.model import Layer

def user_permission_test(user):
    return user.is_superuser or user.is_staff

def add_points():
    data_dir = '/home/dev/appsdev/glo_vli/tethysapp/glo_vli/public/data/'
    layers = os.listdir(data_dir)
    # Creating SQLAlchemy's engine to use
    # engine = create_engine('postgresql://tethys_super:pass@142.93.88.165:5435/layers')
    for layer in layers:
        l_files = os.listdir(os.path.join(data_dir, layer))
        for f in l_files:
            if f.endswith('.shp'):
                f_path = os.path.join(data_dir, layer, f)
                gdf = gpd.read_file(f_path)
                # print(gdf.columns.values)
                # gdf['geom'] = gdf['geometry'].apply(lambda x: WKTElement(x.wkt, srid=4326))
                # df = pd.DataFrame(gdf.drop(columns='geometry'))
                Session = app.get_persistent_store_database('layers', as_sessionmaker=True)
                session = Session()
                print(gdf.columns.values)
                print(f)
                for index, row in gdf.iterrows():

                    if 'LowWaterCrossings_Int' in f:
                        latitude = row.get('LAT')
                        longitude = row.get('LONG')
                        source = row.get('SOURCE')
                    if 'HighWaterMarks_Int' in f:
                        latitude = row.get('Lat')
                        longitude = row.get('Long')
                        source = row.get('Source')

                    table_name = f.split('.')[0]
                    point = Layer(table_name, latitude, longitude, 2019, source, 10, approved=True)
                    session.add(point)
                session.commit()
                session.close()
                # print(latitude, longitude, source)

            # Use 'dtype' to specify column's type
            # For the geom column, we will use GeoAlchemy's type 'Geometry'
            #gdf = gdf.drop('geometry', 1, inplace=True)
            # gdf = gdf.drop(columns=['geometry'], axis=1)
            # table_name = f.split('.')[0]
            # gdf.to_sql(table_name, engine, if_exists='append', index=False,
            #                          dtype={'geom': Geometry('POINT', srid=4326)})