import sys   
from src.logger import logging


def error_message_detail(error,error_details:sys):
    
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python scripts name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )
    
    return error_message


class CustomExcecption(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_detail)


# if __name__=="__main__":    
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by 0 error.")
#         raise CustomExcecption(e,sys)