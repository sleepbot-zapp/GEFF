from __future__ import annotations
import httpx
from .parsers import Gif, Channel, Term, Category, Sticker as sticker, Emoji as emoji
from typing import TYPE_CHECKING
from json import dumps
from .errors import GiphyAPIError
if TYPE_CHECKING:
    from typing import Optional


class GIF:
    BaseUrl = 'https://api.giphy.com/v1/'
    Gif = "https://api.giphy.com/v1/gifs/"
    UrlTrending = "https://api.giphy.com/v1/trending/searches"
    UrlTag = "https://api.giphy.com/v1/tags/related/"
    UrlChannel = "https://api.giphy.com/v1/channels/search"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def fetch_trending(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
        random_id: Optional[str] = None,
        bundle: Optional["str"] = None,
    ) -> list[Gif]:
        params = {
            "api_key": self.api_key,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "random_id": random_id,
            "bundle": bundle,
        }
        data = httpx.get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return [Gif(data[i]) for i in range(len(data))]
        raise GiphyAPIError(data)

    def search(
        self,
        q: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
        lang: Optional[str] = None,
        random_id: Optional[str] = None,
        bundle: Optional["str"] = None,
    ) -> list[Gif]:
        params = {
            "api_key": self.api_key,
            "q": q,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "lang": lang,
            "random_id": random_id,
            "bundle": bundle,
        }
        data = httpx.get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return [Gif(data[i]) for i in range(len(data))]
        raise GiphyAPIError(data)

    def translate(
        self,
        s: str,
        *,
        random_id: Optional[str] = None,
        weirdness: int = 1,
    ) -> Gif:
        params = {
            "api_key": self.api_key,
            "s": s,
            "random_id": random_id,
            "weirdness": weirdness,
        }
        data = httpx.get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return Gif(data)
        raise GiphyAPIError(data)
            

    def random(
        self,
        *,
        tags: Optional[str] = None,
        rating: Optional[str] = None,
        random_id: Optional[str] = None,
    ) -> Gif:
        params = {
            "api_key": self.api_key,
            "tag": tags,
            "rating": rating,
            "random_id": random_id,
        }
        data = httpx.get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return Gif(data)
        raise GiphyAPIError(data)


    def get_random_id(
        self
    ) -> str:
        params = {
            "api_key": self.api_key,
        }
        return httpx.get(f"{self.BaseUrl}randomid", params=params).json()['data']['random_id']

    def fetch(
        self, id: int, *, random_id: Optional[str] = None, rating: Optional[str] = None
    ) -> Gif:
        params = {
            "api_key": self.api_key,
            "gif_id": id,
            "random_id": random_id,
            "rating": rating,
        }
        data = httpx.get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return Gif(data)
        raise GiphyAPIError(data)

    def fetch_many(
        self,
        ids: list[int],
        *,
        random_id: Optional[str] = None,
        rating: Optional[str] = None,
    ) -> list[Gif]:
        params = {"api_key": self.api_key, "random_id": random_id, "rating": rating}
        _ids = ""
        for id in ids:
            if ids[-1] == id:
                _ids += str(id)
                break
            _ids += str(id) + ", "

        params["ids"] = _ids
        return [Gif(data) for data in httpx.get(
            self.Gif[:-1], params=params
        ).json()["data"]]

    def fetch_searches(
        self,
    ) -> list[str]:
        params = {"api_key": self.api_key}
        return httpx.get(self.UrlTrending, params=params).json()["data"]

    def fetch_relate_search(self, term: str): 
        params = {"api_key": self.api_key, "term": term}
        return httpx.get(self.UrlTag + term, params=params).json()["data"]["name"]

    def fetch_channels(
        self, q: str, *, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> list[Optional[Channel]]:
        params = {
            "api_key": self.api_key, 
            "q": q,
            "limit": limit, 
            "offset": offset
        }
        res = httpx.get(self.UrlChannel, params=params).json()["data"]
        if not res:
            return []
        return [Channel(data) for data in res]

    def fetch_tag_autocomplete(
        self, q: str, *, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> list[Term]:
        params = {"api_key": self.api_key, "q": q, "limit": limit, "offset": offset}
        return [Term(data) for data in httpx.get(self.Gif + "search/tags", params=params).json()["data"]]

    def fetch_categories(self) -> list[Category]: 
        params = {"api_key": self.api_key}
        return  [Category(data) for data in httpx.get(self.Gif + "categories", params=params).json()["data"]]


    def upload(
            self,
            username: str,
            source_image_url: str,
            *,
            file: Optional[str] = None,
            tags: Optional[str] = None,
            source_post_url: Optional[str] = None,
        ) -> dict[str, str]:
            values ={
                "api_key": self.api_key,
                "username": username,
                "source_image_url": source_image_url,
                "file": file if file else "",
                "tags": tags if tags else "",
                "source_post_url": source_post_url if source_post_url else ""
            }
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            d = dumps(values).encode("utf-8")
            data = httpx.post("https://upload.giphy.com/v1/gifs", data=d, headers=headers).json() # type: ignore
            try:
                return {"id": data['data']['id'], 'url':f"https://media.giphy.com/media/{data['data']['id']}/giphy.gif"}
            except:
                raise GiphyAPIError(data)

class Sticker:
    BaseUrl = "https://api.giphy.com/v1/stickers/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def fetch_trending(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
    ) -> list[sticker]:
        params = {
            "api_key": self.api_key,
            "limit": limit,
            "offset": offset,
            "rating": rating,
        }
        data = httpx.get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return [sticker(data[i]) for i in range(len(data))]
        raise GiphyAPIError(data)

    def search(
        self,
        q: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
    ) -> list[sticker]:
        params = {
            "api_key": self.api_key,
            "q": q,
            "limit": limit,
            "offset": offset,
            "rating": rating,
        }
        data = httpx.get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return [sticker(data[i]) for i in range(len(data))]
        raise GiphyAPIError(data)

    def translate(
        self,
        s: str,
        *,
        weirdness=1,
    ) -> sticker:
        params = {
            "api_key": self.api_key,
            "s": s,
            "weirdness": weirdness,
        }
        data = httpx.get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return sticker(data)
        raise GiphyAPIError(data)


    def random(
        self,
        tags: Optional[str] = None,
        *,
        rating: Optional[str] = None,
        random_id: Optional[str] = None,
    ) -> sticker:
        params = {
            "api_key": self.api_key,
            "tag": tags,
            "rating": rating,
            "random_id": random_id,
        }
        data = httpx.get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return sticker(data)
        raise GiphyAPIError(data)


class Emoji:
    BaseUrl = "https://api.giphy.com/v2/emoji"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def fetch(self, *, limit: Optional[int] = None, offset: Optional[int] = None) -> list[emoji]:
        params = {"api_key": self.api_key, "limit": limit, "offset": offset}
        data = httpx.get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return [emoji(data[i]) for i in range(len(data))]
        raise GiphyAPIError(data)

    def get_variations(self, *, gif_id: Optional[int]) -> emoji|None:
        params = {"api_key": self.api_key}
        data = httpx.get(self.BaseUrl+f"/{gif_id}/variations", params=params).json()
        if data['data']:
            data = data['data']
            return emoji(data)
        raise GiphyAPIError(data)
        
