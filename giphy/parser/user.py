class User:
    def __init__(self, data) -> None:
        self._data = data
        self.avatar_url = self._data['avatar_url']#.get('avatar_url')
        self.banner_url = self._data.get('banner_url')
        self.profile_url = self._data.get('profile_url') 
        self.username = self._data.get('username')
        self.display_name = self._data.get('display_name')

    def __repr__(self) -> str:
        return f"User({', '.join([f'{i}: {self.__dict__[i]}' for i in self.__dict__ if not i.startswith('_')])})"