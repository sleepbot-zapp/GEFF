class Term:
    def __init__(self, data):
        self._data = data
        self.name = data.get("name")
        self.analytics_response_payload = data.get("analytics_response_payload")

    def __repr__(self) -> str:
        return f"Term(name={self.name})"
