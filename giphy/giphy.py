from __future__ import annotations
import httpx
from .parser import Gif
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class GIF:
    BaseUrl = "https://api.giphy.com/v1/gifs/"
    UrlTrending = "https://api.giphy.com/v1/trending/searches"
    UrlTag = "https://api.giphy.com/v1/tags/related/"
    UrlChannel = "https://api.giphy.com/v1/channels/search"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def trending(
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
        data = httpx.get(f"{self.BaseUrl}trending", params=params).json()["data"]
        return [Gif(data[i]) for i in range(len(data))]

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
        data = httpx.get(f"{self.BaseUrl}search", params=params).json()["data"]
        return [Gif(data[i]) for i in range(len(data))]

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
        return Gif(httpx.get(f"{self.BaseUrl}random", params=params).json()["data"])

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
        return Gif(httpx.get(f"{self.BaseUrl}random", params=params).json()["data"])

    # UNTESTED
    def get_random_id(
        self,
        *,
        tag: Optional[str] = None,
        rating: Optional[str] = None,
    ):
        params = {
            "api_key": self.api_key,
            "tag": tag,
            "rating": rating,
        }
        return httpx.get(f"{self.BaseUrl}random", params=params).json()

    def fetch(
        self, id: int, *, random_id: Optional[str] = None, rating: Optional[str] = None
    ):
        params = {
            "api_key": self.api_key,
            "gif_id": id,
            "random_id": random_id,
            "rating": rating,
        }

        return httpx.get(self.BaseUrl + id, params=params).json()

    def fetch_many(
        self,
        ids: list[int],
        *,
        random_id: Optional[str] = None,
        rating: Optional[str] = None,
    ):
        params = {"api_key": self.api_key, "random_id": random_id, "rating": rating}
        _ids = ""
        for id in ids:
            if ids[-1] == id:
                _ids += id
                break
            _ids += id + ", "

        params["ids"] = _ids
        return httpx.get(
            self.BaseUrl[:-1], params=params
        ).json()  # Put index slice: Might need to change the base_url without '/' at the ending.

    def fetch_searches(
        self,
    ):  # Might need to move this method elsewhere for now this staying here!
        params = {"api_key": self.api_key}
        return httpx.get(self.UrlTrending, params=params).json()

    def fetch_relate_search(self, term: str):
        params = {"api_key": self.api_key, "term": term}

        return httpx.get(self.UrlTag + term, params=params).json()

    def fetch_channel(
        self, q: str, *, limit: Optional[int] = None, offset: Optional[int] = None
    ):
        params = {"api_key": self.api_key, "limit": limit, "offset": offset}

        return httpx.get(self.UrlChannel, params=params).json()

    def fetch_tag_autocomplete(
        self, q: str, *, limit: Optional[int] = None, offset: Optional[int] = None
    ):
        params = {"api_key": self.api_key, "limit": limit, "offset": offset}

        return httpx.get(self.BaseUrl + "search/tags", params=params).json()

    def fetch_categories(self):
        params = {"api_key": self.api_key}

        return httpx.get(self.BaseUrl + "categories", params=params)


class Sticker:
    BaseUrl = "https://api.giphy.com/v1/stickers/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def trending(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
    ):
        params = {
            "api_key": self.api_key,
            "limit": limit,
            "offset": offset,
            "rating": rating,
        }
        return httpx.get(f"{self.BaseUrl}trending", params=params).json()

    def search(
        self,
        q: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        rating: Optional[str] = None,
    ):
        params = {
            "api_key": self.api_key,
            "q": q,
            "limit": limit,
            "offset": offset,
            "rating": rating,
        }
        return httpx.get(f"{self.BaseUrl}search", params=params).json()

    def translate(
        self,
        s: str,
        *,
        weirdness=1,
    ):
        params = {
            "api_key": self.api_key,
            "s": s,
            "weirdness": weirdness,
        }
        return httpx.get(f"{self.BaseUrl}translate", params=params).json()


class Emoji:
    BaseUrl = "https://api.giphy.com/v2/emoji"

    def __init__(self, api_key: str):
        self.api_key = self.api_key

    # UNTESTED
    def get(self, *, limit: Optional[int] = None, offset: Optional[int] = None):
        params = {"api_key": self.api_key, "limit": limit, "offset": offset}

        return httpx.get(self.BaseUrl, params=params).json()

    def get_variations(self, *, gif_id: Optional[int]):
        params = {"api_key": self.api_key}
        return httpx.get(f"{self.BaseUrl}/{gif_id}/variations", params=params).json()


"""
TODO:                        Objects:
RandomID: X                  Implements all Giphy objects!
Emoji: X
Emoji Variation: X
GIF(s) by id: X X

Upload:

Categories: X
Autocomplete: X
Channel Search: X
Search Suggestion: X
Trending Search: X
"""
