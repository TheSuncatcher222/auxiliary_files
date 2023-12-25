import app_logger

logger = app_logger.get_logger(__name__)

class Error(Exception):
    """Базовый класс для исключений."""
    pass


class TokenValidationError(Error):
    """Исключение для ошибки валидации токена"""
    def __init__(self, token):
        self.token = token
        super().__init__(
            f'Токен {self.token} не валидный'
        )
    
    # def __str__(self):
    #     return 'invalid token'
