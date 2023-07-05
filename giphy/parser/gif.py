from .image import Image
from .user import User


class Gif:
    def __init__(self, data) -> None:
        self._data = data
    
    @property
    def id(self):
        return self._data.get('id')
    
    @property
    def type(self):
        return self._data.get('type') 
       
    @property
    def slug(self):
        return self._data.get('slug')

    @property
    def url(self):
        return self._data.get('url')
    
    @property
    def bitly_url(self):
        return self._data.get('bitly_url')
    
    @property
    def embed_url(self):
        return self._data.get('embed_url')
    
    @property
    def source(self):
        return self._data.get('source')

    @property
    def source_tld(self):
        return self._data.get('source_tld')

    @property
    def source_url(self):
        return self._data.get('source_post_url')
    
    @property
    def alt_text(self):
        return self._data.get('alt_text')
    
    @property
    def title(self):
        return self._data.get('title')
    
    @property
    def rating(self):
        return self._data.get('rating')
    
    @property
    def trending_datetime(self):
        return self._data.get('trending_datetime')
    
    @property
    def update_datetime(self):
        return self._data.get('update_datetime')
    
    @property
    def create_datetime(self):
        return self._data.get('create_datetime')
    
    @property
    def import_datetime(self):
        return self._data.get('import_datetime')
    
    @property
    def is_sticker(self):
        return False if not self._data("is_sticker") else True

    @property
    def username(self):
        return self._data.get('username')
    
    @property
    def images(self):
        return [Image(i) for i in self._data.get('images')]
    
    @property
    def user(self):
        return [User(i) for i in self._data.get('user')]
    
    def __repr__(self) -> str:
        return f"Gif(Title: {self.title}, URL: {self.url})"