import httpx

class GIF:
    BaseUrl = "https://api.giphy.com/v1/gifs/"
    def __init__(self, api_key: str):
        self.api_key = api_key

    def trending(self,  *, limit: int, offset: int, rating: str,):
        params = {"api_key": self.api_key, "limit": limit, "offset": offset, "rating": rating}
        return httpx.get(f"{self.BaseUrl}trending", params=params).json()
    
    def search(self,  q: str, *, limit: int, offset: int, rating: str,):
        params = {"api_key": self.api_key, "q": q, "limit": limit, "offset": offset, "rating": rating}
        return httpx.get(f"{self.BaseUrl}search", params=params).json()
    
    def translate(self, s: str, *, weirdness = 1,):
        params = {"api_key": self.api_key, "s": s, "weirdness": weirdness,}
        return httpx.get(f"{self.BaseUrl}translate", params=params).json()
    
    def random(self, *, tag: str = None, rating: str = None,):
        params = {"api_key": self.api_key, "tag": tag, "rating": rating,}
        return httpx.get(f"{self.BaseUrl}random", params=params).json()


class Sticker:
    BaseUrl = "https://api.giphy.com/v1/stickers/"
    def __init__(self, api_key: str):
        self.api_key = api_key

    def trending(self,  *, limit: int = 1, offset: int = 0, rating: str = None,):
        params = {"api_key": self.api_key, "limit": limit, "offset": offset, "rating": rating}
        return httpx.get(f"{self.BaseUrl}trending", params=params).json()
    
    def search(self,  q: str, *, limit: int = 1, offset: int = 0, rating: str = None,):
        params = {"api_key": self.api_key, "q": q, "limit": limit, "offset": offset, "rating": rating}
        return httpx.get(f"{self.BaseUrl}search", params=params).json()
    
    def translate(self, s: str, *, weirdness = 1,):
        params = {"api_key": self.api_key, "s": s, "weirdness": weirdness,}
        return httpx.get(f"{self.BaseUrl}translate", params=params).json()
    
    def random(self, *, tag: str = None, rating: str = None,):
        params = {"api_key": self.api_key, "tag": tag, "rating": rating,}
        return httpx.get(f"{self.BaseUrl}random", params=params).json()
    