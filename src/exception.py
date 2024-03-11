#file for exception handling
import sys   # this library has all the details related to a particular error
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() 
    #in this the last variable will give you in which file error has occurred and in which line number the error has occurred
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
       
    return error_message 
    
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message     
       
       
'''    #To check whether exception is working fine u can add this and check, if the log file recieves the message provided below then it is working fine   
if __name__=="__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero") # if an exception comes this is the message that goona be shown in the log file
        raise CustomException(e,sys)
          
'''  