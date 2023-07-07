class Image:
    def __init__(self, data) -> None:
        self._data = data
        self.url = self._data.get("url")
        self.width = self._data.get("width")
        self.height = self._data.get("height")
        self.mp4 = self._data.get("mp4")
        self.mp4_size = self._data.get("mp4_size")
        self.webp = self._data.get("webp")
        self.webp_size = self._data.get("webp_size")
        self.size = self._data.get("size")
        self.frames = self._data.get("frames")

    def __repr__(self) -> str:
        return f"Image(url={self.url})"
