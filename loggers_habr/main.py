import package1
import app_logger
import app_exceptions

logger = app_logger.get_logger(__name__)


def main():
    logger.debug('Запуск программы')
    package1.process(msg='сообщение')
    logger.warning('Это warning')
    logger.info('Программа завершила работу')

if __name__ == '__main__':
    # main()
    # b = 1 / 0
    b = 1
    raise app_exceptions.TokenValidationError(b)
