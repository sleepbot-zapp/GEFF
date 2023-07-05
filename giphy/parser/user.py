class User:
    def __init__(self, data) -> None:
        self._data = data

    @property
    def avatar_url(self):
        return self._data.get('avatar_url')

    @property
    def banner_url(self):
        return self._data.get('banner_url')

    @property
    def profile_url(self):
        return self._data.get('profile_url') 
    
    @property
    def username(self):
        return self._data.get('username')
    
    @property
    def display_name(self):
        return self._data.get('display_name')