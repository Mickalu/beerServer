class Response_API:
    def __init__(self, status:bool = False, data:dict = {}) -> None:
        self.status = status
        self.data = data
