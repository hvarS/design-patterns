import logging 

class MailService:

    def __init__(self) -> None:
        pass

    def __connect(self):
        logging.info('<---- Connecting to the MAIL server --->')
    
    def __authenticate(self):
        logging.info('<---- Authenticating connection to the MAIL server --->')
    
    def __disconnect(self):
        logging.info('<---- Disconnecting to the MAIL server --->')

    def sendEmail(self):
        self.__connect()
        self.__authenticate()
        self.__disconnect()
    
     
    

    