class Image:
    def __init__(self, data) -> None:
        self._data = data

    @property
    def url(self):
        return self._data.get('url')
    
    @property
    def width(self):
        return self._data.get('width')
    
    @property
    def height(self):
        return self._data.get('height')
    
    @property
    def mp4(self):
        return self._data.get('mp4')
    
    @property
    def mp4_size(self):
        return self._data.get('mp4_size')
    
    @property
    def webp(self):
        return self._data.get('webp')
    
    @property
    def webp_size(self):
        return self._data.get('webp_size')
    
    @property
    def size(self):
        return self._data.get('size')
    
    @property
    def frames(self):
        return self._data.get('frames')