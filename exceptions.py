class TooManyStarsException(Exception):
    "You can't have more then 2 * (1 for competence, 2 for maestria)"
    def __init__(self,  message="too many stars in conf file"):
        self.message = message
        super().__init__(self.message)
    pass