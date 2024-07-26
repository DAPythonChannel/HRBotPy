import os, logging, datetime

class HRLogging():

    def __init__(self):
        '''При инициализации конфигурирует '''
        logging.basicConfig(filename=self.get_file(),filemode="a",
                             format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")


    def get_file(self) -> str:
        '''Создает лог-файл с датой если он не существует и возвращает полный путь к нему'''
        date = datetime.datetime.now().date()
        file_name = os.path.join(os.path.dirname(__file__),f"{date}_py_log.log")
        if os.path.exists(file_name):
            return file_name
        else: 
            open(file_name, 'w').close()
            return file_name
            
    def push_log_warning(self, text: str, level: str) -> None:
        '''Сохраняет информацию в лог с категорией warning'''
        logging.warning(text)

    def push_log_error(self, text:str) -> None:
        '''Сохраняет информацию в лог с категорией error'''
        logging.error(text)

    def push_log_critical(self, text:str) -> None:
        '''Сохраняет информацию в лог с категорией critical'''
        logging.critical(text)