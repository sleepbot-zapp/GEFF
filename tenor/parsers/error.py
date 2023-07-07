class TenorAPIError(Exception):
    def __init__(self, error) -> None:
        self._error = error.get('error')
        self.code = self._error.get('code')
        self.message = self._error.get('message')
        self.status = self._error.get('status')
        self.details = self._error.get('details')
        super().__init__(f"error code : {self.code}, message : {self.message}")