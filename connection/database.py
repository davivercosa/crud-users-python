from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# env
from dotenv import load_dotenv
import os 

load_dotenv()

user = os.getenv("dbuser")
password = os.getenv("dbpassword")
host = os.getenv("dbhost")
port = os.getenv("dbport")
database = os.getenv("db")

engine = create_engine(url="mysql+pymysql://{0}:{1}@{2}/{4}".format(user, password, host, port, database))
  
if __name__ == '__main__':
    try:
        with Session(engine) as session:
            x = session.execute("SELECT 1")
            print(x)
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)