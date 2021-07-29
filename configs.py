from decouple import config

class Var:
    API_ID = config("API_ID", None)
    API_HASH = config("API_HASH", None)