import os,sys
from thyroid.logger import logging
from thyroid.exception import ThyroidException

if __name__ =="__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)
    
