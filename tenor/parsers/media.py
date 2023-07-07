class Media:
    def __init__(self, name, data) -> None:
        self._data = data
        self.type = name
        self.url = self._data.get('url')
        self.dims = self._data.get('dims')
        self.duration = self._data.get('duration')
        self.size = self._data.get('size')

    def __repr__(self) -> str:
        return f"Media({', '.join([f'{i}: {self.__dict__[i]}' for i in self.__dict__ if not i.startswith('_')])})"