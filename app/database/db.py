from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
import os


class DatabasePool:
    def __init__(self,min_connections=2, max_connections=5, **kwargs) -> None:
        self.max_connections=max_connections
        self.min_connections=min_connections
        self.connection_params=kwargs
        self.initialize_pool()


    def initialize_pool(self):
        try:
            self.pool=pool.ThreadedConnectionPool(self.min_connections,self.max_connections,**self.connection_params)
            if self.pool:
                print("Successfully created postgress connection.")
        except psycopg2.Error as e:
            print(f"Error initializing connection pool: {e}")
            raise

    def get_connection(self):
        if self.pool is None:
            self.initialize_pool()
        try:
            connection =self.pool.getconn()
            
            if connection: 
                print("Connection acquired from db pool")
                return connection
            else: 
                print("Failed to obtain a connection from the db pool.")
                return None
        except psycopg2.Error as e:
            print(f"Error getting connection from pool: {e}")
            return None

    def put_connection(self,connection):
        try:
            self.pool.putconn(connection)
        except psycopg2.Error as e:
            print(f"Error initializing connection pool: {e}")
            raise

    def close_connection(self):
        try:
            if self.pool:
                self.pool.closeall()
                print("All connections in the pool closed.")
            else:
                print("Pool is already closed or not initialized.")
        except psycopg2.Error as e:
            print(f"Error closing all connections: {e}")

