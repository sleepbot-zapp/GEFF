from .gif import Gif
from .user import User


# How abt we make the repr much shorter? it's likevery long bro we just need the slug thats all?
class Channel:
    def __init__(self, data):
        self._data = data

        self.id = self._data.get("id")
        self.url = self._data.get("url")
        self.display_name = self._data.get("display_name")
        self.parent = self._data.get("parent")
        self.slug = self._data.get("slug")
        self.type = self._data.get("type")
        self.content_type = self._data.get("content_type")
        self.id = self._data.get("id")
        self.user = User(self._data.get("user"))
        self.banner_image = self._data.get("banner_image")
        self.short_display_name = self._data.get("short_display_name")
        self.description = self._data.get("description")
        self.meta_data_description = self._data.get("meta_data_description")
        self.has_children = self._data.get("has_children")
        self.is_visible = self._data.get("is_visible")
        self.is_private = self._data.get("is_private")
        self.is_visible = self._data.get("is_live")
        self.featured_gif = Gif(self._data.get("featured_gif"))
        self.tags = self._data.get(
            "tags"
        )  # [ChannelTag(tag) for tag in channel["tags"]]
        self.live_since_datetime = self._data.get("live_since_datetime")
        self.live_until_datetime = self._data.get("live_until_datetime")
        self.ancestors = self._data.get(
            "ancestors"
        )  # [Channel(_data) for _data in self._data.get("ancestors")]
        self.syncable_tags = self._data.get(
            "syncable_tags"
        )  # [ChannelTag(tag) for tag in channel["syncable_tags"]]

    def __repr__(self) -> str:
        return f"Channel(url={self.url}, id={self.id}, user={self.user})"
