from datetime import datetime
from .media import Media
from typing import Dict, Any


class Gif:
    def __init__(self, data: Dict[str, Any]) -> None:
        self._data = data
        self.id = self._data.get("id")
        self.title = self._data.get("title")
        self.created = datetime.fromtimestamp(self._data.get("created"))  # type: ignore
        self.tags = self._data.get("tags")
        self.content_description = self._data.get("content_description")
        self.itemurl = self._data.get("itemurl")
        self.url = self._data.get("url")
        self.hasaudio = self._data.get("hasaudio")
        self.media_formats = [
            Media(i, self._data.get("media_formats")[i])  # type: ignore
            for i in self._data.get("media_formats")  # type: ignore
        ]

    def __repr__(self) -> str:
        return f"Response({', '.join([f'{i}: {self.__dict__[i]}' for i in self.__dict__ if not i.startswith('_')])})"
