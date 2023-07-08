class GiphyAPIError(Exception):
    def __init__(self, error) -> None:
        self._error = error.get('meta')
        self.status = self._error.get("status")
        self.msg = self._error.get("msg")
        self.response_id = self._error.get("response_id")
        super().__init__(f"error code : {self.status}, message : {self.msg}")
