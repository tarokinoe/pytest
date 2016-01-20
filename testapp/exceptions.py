class TestAppError(Exception):
    def __str__(self):
        return 'Error in test application'


class OpenGameAlreadyExists(TestAppError):
    def __str__(self):
        return 'Player already has open game.'
