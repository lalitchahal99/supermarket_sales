from fake_store_txn import FakeDataBuilder
import random, os
from sqlalchemy import create_engine, insert, Table, Column, String, DECIMAL, CHAR, SmallInteger, BigInteger
from sqlalchemy.orm import declarative_base

import logging
import logging.handlers
import os
import configparser
from datetime import datetime

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf-8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)
logger.info(f"-----------| {datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} |-----------")
logger.info(f"Loading start...")

def main(*args):
    table, engine = args[0][0], args[0][-1]
    f = (
        FakeDataBuilder()
        .addCity()
        .addCustomerType()
        .addGender()
        .addProductLine()
        .addUnitPrice()
        .addProductQuantity()
        .addTaxProduct()
        .addTotalCost()
        .addDateTime()
        .addPaymentMode()
        .FetchTxn()
    )
    stmt = insert(table).values(
        product_line = f.Product_Line,
        city = f.City,
        customer_type = f.Customer_Type,
        gender = f.Gender,
        payment_mode = f.Payment_Mode,
        dt = f.DT,
        unit_price = f.Unit_Price,
        quantity = f.Quantity,
        tax = f.Tax,
        total = f.Total 
    )
    with engine.connect() as conn:
        r = conn.execute(stmt)
        conn.commit()
    return None

if __name__ == "__main__":
    try:
        connection_string = os.environ["MYSQL_CONNECTION_STRING"]
        engine = create_engine(connection_string, echo=False)
    except Exception as err:
        logger.info(f"Error setting up connection!")
        logger.info(err)
    else:
        Base = declarative_base()
        sales_table = Table(
            "sales",
            Base.metadata,
            Column('txn_id', BigInteger, primary_key=True),
            Column('product_line', String),
            Column('city', String),
            Column('customer_type', String),
            Column('gender', CHAR),
            Column('payment_mode', String),
            Column('dt', String),
            Column('unit_price', DECIMAL(10,2)),
            Column('quantity', SmallInteger),
            Column('tax', DECIMAL(10,2)),
            Column('total', DECIMAL(10,2)) 
        )
        try:
            cp = configparser.ConfigParser()
            cp.read("properties.conf")
            l, h = int(cp.get('DEFAULT', 'rows_range').split()[0]), int(cp.get('DEFAULT', 'rows_range').split()[-1]) # rows_range is the number of rows to be loaded at a time
            n_rows = random.randint(l, h)
        except Exception as err:
            logger.info(f"Error loading conf file")
        else:
            try:
                # Multi-Threading
                from concurrent.futures import ThreadPoolExecutor
                with ThreadPoolExecutor(max_workers=4) as executor:
                    executor.map(main, [(sales_table, engine) for _ in range(n_rows)], timeout=30)
            except Exception as err:
                logger.info(f"Error while loading data.")
            else:
                logger.info(f"Number of rows loaded -> {n_rows}")
                logger.info(f"Data load finished!")
    finally:
        logger.info('Note : Refer to above logs to know more.')
        logger.info('\n')