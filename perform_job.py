import pandas as pd
import sqlite3
from datetime import datetime
import time


def create_connection():
    return sqlite3.connect('./temp.db')


def read_csv():
    print("starting to read from csv file")
    df = pd.read_csv("./input_data/urban-area-long-term.csv", delimiter=',')
    df = pd.concat([df] * 3)
    return df


def write_csv(df: pd.DataFrame):
    print("starting to write into Table")
    conn = create_connection()
    df.to_sql('urban_data', conn, if_exists='append', index=False)
    conn.close()


def read_n_write_data_to_db():
    df = read_csv()
    write_csv(df)
    print("records written into sql database")


def read_records_from_db():
    conn = create_connection()
    df = pd.read_sql('select * from urban_data', conn)
    conn.close()
    return df


def get_batch_reference():
    str_date = str(datetime.now())
    batch_ref = str_date.split('.')[-1]
    return batch_ref


class SqllittleConnection(object):
    def __init__(self):
        self.conn = None

    def __enter__(self):
        print("inside enter method, initialised the connection")
        self.conn = sqlite3.connect('./temp.db')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit method triggerred, closing connection")
        self.conn.close()


def read_n_write_data_to_db(data_vol):
    df = read_csv()
    df = pd.concat([df] * data_vol)
    df['batch_reference'] = get_batch_reference()
    df['data_vol'] = str(data_vol)
    time.sleep(10)
    with SqllittleConnection() as sql3connector:
        df.to_sql('urban_data', sql3connector.conn, if_exists='append', index=False)
    return "records written into sql database for Data Volume" + str(data_vol)


if __name__ == "__main__":
    read_n_write_data_to_db(10)
    # read_records_from_db()
