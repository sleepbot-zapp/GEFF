from .user import User
from .image import Image


class Clip:
    def __init__(self, data):
        self._data = data
        self.id = self._data.get("id")
        self.url = self._data.get("url")
        self.embed_url = self._data.get("embed_url")
        self.duration = self._data.get("duration")
        self.username = self._data.get("username")
        self.source = self._data.get("source")
        self.title = self._data.get("title")
        self.rating = self._data.get("rating")
        self.cta = self._data.get(
            "cta"
        )  # Need parser, full object isnt documented in the docs
        self.images = [Image(_data) for _data in self._data.get("images")]
        self.video = Video(self._data.get("video"))
        self.user = User(self._data.get("user"))


class Video:
    def __init__(self, data):
        self._data = data
        self.description = self._data.get("description")
        self.assets = [
            asset for asset in self._data.get("assets")
        ]  # Need parser for assets, object isnt documented in docs (same with CTA)
        self.captions = [
            caption for caption in self._data.get("captions")
        ]  # Need parser for captions, object isnt documented in docs (same with CTA)
        self.native = self._data.get("native")
