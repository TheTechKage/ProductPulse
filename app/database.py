from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self,db_url,min_connections=2, max_connections=5, **kwargs) -> None:
        self.db_url=db_url
        self.max_connections=max_connections
        self.min_connections=min_connections
        self.db_engine=None,
        self.connection_params=kwargs
        self.session=None
        self.initialize_engine()
        
    def initialize_engine(self):
        try:
            if self.db_engine==None: 
                self.db_engine=create_engine(pool_size=self.min_connections,max_overflow=self.max_connections,**self.connection_params)
            if self.db_engine:
                print("Successfully created postgress connection.")
                self.session=sessionmaker(bind=self.db_engine)
        except Exception as e:
            print(f"Error initializing db connection: {e}")
            raise