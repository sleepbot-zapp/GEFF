class Category:
    def __init__(self, data) -> None:
        self._data = data
        self.searchterm = self._data.get('searchterm')
        self.path = self._data.get('path')
        self.image = self._data.get('image')
        self.name = self._data.get('name')

    def __repr__(self) -> str:
        return f"Category({', '.join([f'{i}: {self.__dict__[i]}' for i in self.__dict__ if not i.startswith('_')])})"