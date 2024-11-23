import psycopg2
from jproperties import Properties


def get_connection():
    """ Connect to the PostgreSQL database server """
    configs = Properties()
    with open('config.properties', 'rb') as config_file:
        configs.load(config_file)
    conn = None
    
    try:
        # read connection parameters
        conn = psycopg2.connect(
            host=configs.get("DB_HOST").data,
            database=configs.get("DB_SCHEMA").data,
            user=configs.get("DB_User").data,
            password=configs.get("DB_PWD").data,
            port=configs.get("PORT").data)

        # create a cursor
        cursor = conn.cursor()
       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    return cursor,conn







