from __future__ import annotations
from httpx import get, post
from .parsers import Gif, Channel, Term, Category, Sticker as sticker, Emoji as emoji
from typing import TYPE_CHECKING, Tuple, List
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

    def fetch_trendinget(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
        random_id: Optional[str] = None,
        bundle: Optional["str"] = None,
    ) -> Tuple[Gif]:
        params = {
            "api_key": self.api_key,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "random_id": random_id,
            "bundle": bundle,
        }
        data = get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return tuple(Gif(data[i]) for i in range(len(data)))
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
    ) -> Tuple[Gif]:
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
        data = get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return tuple(Gif(data[i]) for i in range(len(data)))
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
        data = get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return Gif(data)
        raise GiphyAPIError(data)
            

    def random(
        self,
        *,
        tag: Optional[str] = None,
        rating: Optional[str] = None,
        random_id: Optional[str] = None,
    ) -> Gif:
        params = {
            "api_key": self.api_key,
            "tag": tag,
            "rating": rating,
            "random_id": random_id,
        }
        data = get(f"{self.Gif}trending", params=params).json()
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
        return get(f"{self.BaseUrl}randomid", params=params).json()['data']['random_id']

    def fetch(
        self, id: int, *, random_id: Optional[str] = None, rating: Optional[str] = None
    ) -> Gif:
        params = {
            "api_key": self.api_key,
            "gif_id": id,
            "random_id": random_id,
            "rating": rating,
        }
        data = get(f"{self.Gif}trending", params=params).json()
        if data['data']:
            data = data['data']
            return Gif(data)
        raise GiphyAPIError(data)

    def fetch_many(
        self,
        ids: str|List[str],
        *,
        random_id: Optional[str] = None,
        rating: Optional[str] = None,
    ) -> Tuple[Gif]:
        if isinstance(ids, list):
            ids = ", ".join([i for i in ids])
        params = {"api_key": self.api_key, 'ids':ids, "random_id": random_id, "rating": rating}
        data = get(f"{self.Gif}", params=params).json()
        if data['data']:
            data = data['data']
            return tuple(Gif(data[i]) for i in range(len(data)))
        raise GiphyAPIError(data)

    def fetch_searches(
        self,
    ) -> Tuple[str]:
        params = {"api_key": self.api_key}
        data = get(self.UrlTrending, params=params).json()
        if data['data']:
            return tuple(data["data"])
        raise GiphyAPIError(data)

    def fetch_related_search(self, term: str) -> Tuple[str]: 
        params = {"api_key": self.api_key, "term": term}
        data = get(self.UrlTag + term, params=params).json()
        if data['data']:
            return tuple(data["data"]["name"])
        raise GiphyAPIError(data)

    def fetch_channels(
        self, q: str, *, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Tuple[Channel]:
        params = {
            "api_key": self.api_key, 
            "q": q,
            "limit": limit, 
            "offset": offset
        }
        data = get(self.UrlChannel, params=params).json()
        if data['data']:
            return tuple(Channel(i) for i in data['data'])
        raise GiphyAPIError(data)

    def fetch_tag_autocomplete(
        self, q: str, *, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Tuple[Term]:
        params = {"api_key": self.api_key, "q": q, "limit": limit, "offset": offset}
        data = get(self.Gif + "search/tags", params=params).json()
        if data['data']:
            return tuple(Term(i) for i in data['data'])
        raise GiphyAPIError(data)

    def fetch_categories(self) -> Tuple[Category]: 
        params = {"api_key": self.api_key}
        data = get(self.Gif + "categories", params=params).json()
        if data['data']:
            return tuple(Category(i) for i in data['data'])
        raise GiphyAPIError(data)


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
            data = post("https://upload.giphy.com/v1/gifs", data=d, headers=headers).json() # type: ignore
            try:
                return {"id": data['data']['id'], 'url':f"https://media.giphy.com/media/{data['data']['id']}/giphy.gif"}
            except:
                raise GiphyAPIError(data)

class Sticker:
    BaseUrl = "https://api.giphy.com/v1/stickers/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def fetch_trendinget(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
    ) -> Tuple[sticker]:
        params = {
            "api_key": self.api_key,
            "limit": limit,
            "offset": offset,
            "rating": rating,
        }
        data = get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return tuple(sticker(data[i]) for i in range(len(data)))
        raise GiphyAPIError(data)

    def search(
        self,
        q: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
    ) -> Tuple[sticker]:
        params = {
            "api_key": self.api_key,
            "q": q,
            "limit": limit,
            "offset": offset,
            "rating": rating,
        }
        data = get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return tuple(sticker(data[i]) for i in range(len(data)))
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
        data = get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return sticker(data)
        raise GiphyAPIError(data)


    def random(
        self,
        tag: Optional[str] = None,
        *,
        rating: Optional[str] = None,
        random_id: Optional[str] = None,
    ) -> sticker:
        params = {
            "api_key": self.api_key,
            "tag": tag,
            "rating": rating,
            "random_id": random_id,
        }
        data = get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return sticker(data)
        raise GiphyAPIError(data)


class Emoji:
    BaseUrl = "https://api.giphy.com/v2/emoji"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def fetch(self, *, limit: Optional[int] = None, offset: Optional[int] = None) -> Tuple[emoji]:
        params = {"api_key": self.api_key, "limit": limit, "offset": offset}
        data = get(f"{self.BaseUrl}trending", params=params).json()
        if data['data']:
            data = data['data']
            return tuple(emoji(data[i]) for i in range(len(data)))
        raise GiphyAPIError(data)

    def get_variations(self, *, gif_id: Optional[int]) -> emoji:
        params = {"api_key": self.api_key}
        data = get(self.BaseUrl+f"/{gif_id}/variations", params=params).json()
        if data['data']:
            data = data['data']
            return emoji(data)
        raise GiphyAPIError(data)
        