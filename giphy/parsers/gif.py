from .image import Image
from .user import User



class Gif:
    def __init__(self, data) -> None:
        self._data = data
        self.id = self._data.get("id")
        self.type = self._data.get("type")
        self.slug = self._data.get("slug")
        self.url = self._data.get("url")
        self.bitly_url = self._data.get("bitly_url")
        self.embed_url = self._data.get("embed_url")
        self.source = self._data.get("source")
        self.source_tld = self._data.get("source_tld")
        self.source_url = self._data.get("source_post_url")
        self.alt_text = self._data.get("alt_text")
        self.title = self._data.get("title")
        self.rating = self._data.get("rating")
        self.trending_datetime = self._data.get("trending_datetime")
        self.update_datetime = self._data.get("update_datetime")
        self.create_datetime = self._data.get("create_datetime")
        self.import_datetime = self._data.get("import_datetime")
        self.is_sticker = bool(self._data.get("is_sticker"))
        self.username = self._data.get("username")
        try:
            self.user = User(self._data.get('user'))
        except AttributeError:
            self.user = self.username
        try:
            self.is_emoji = True if self._data.get("variation_count") >= 0 else False
        except TypeError:
            self.is_emoji = False
        if self.is_emoji:
            self.variation_count = self._data.get("variation_count")
    
    @property
    def images(self) -> list[Image]:
        return [Image(self._data.get("images")[i]) for i in self._data.get("images")]

    def __repr__(self) -> str:
        check = isinstance(self.user, User)
        return f"{self.__class__.__name__}(title={self.title}, id={self.id}, {'user' if check else 'username'}={self.user if check else self.username})"

    
class Sticker(Gif):
    ...

class Emoji(Gif):
    ...