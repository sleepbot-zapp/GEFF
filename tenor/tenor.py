from __future__ import annotations
from httpx import get
from typing import TYPE_CHECKING, Tuple
from .parsers import Gif, Category
from .errors import TenorAPIError

if TYPE_CHECKING:
    from typing import Optional


class GIF:
    BaseUrl = "https://tenor.googleapis.com/v2/"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def search(
        self,
        q: str,
        *,
        client_key: Optional[str] = None,
        searchfilter: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        contentfilter: Optional[str] = "off",
        media_filter: Optional[str] = None,
        ar_range: Optional[str] = "all",
        random: Optional[bool] = False,
        limit: Optional[int] = 20,
        pos: Optional[str] = None,
    ) -> Tuple[Gif]:
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "searchfilter": searchfilter,
            "country": country,
            "locale": locale,
            "contentfilter": contentfilter,
            "media_filter": media_filter,
            "ar_range": ar_range,
            "random": random,
            "limit": limit,
            "pos": pos,
        }
        data = get(f"{self.BaseUrl}search", params=params).json()
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(Gif(data[i]) for i in range(len(data)))

    def featured(
        self,
        *,
        client_key: Optional[str] = None,
        searchfilter: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        contentfilter: Optional[str] = "off",
        media_filter: Optional[str] = None,
        ar_range: Optional[str] = "all",
        random: Optional[bool] = False,
        limit: Optional[int] = 20,
        pos: Optional[str] = None,
    ) -> Tuple[Gif]:
        params = {
            "key": self.api_key,
            "client_key": client_key,
            "searchfilter": searchfilter,
            "country": country,
            "locale": locale,
            "contentfilter": contentfilter,
            "media_filter": media_filter,
            "ar_range": ar_range,
            "random": random,
            "limit": limit,
            "pos": pos,
        }
        data = get(f"{self.BaseUrl}featured", params=params).json()
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(Gif(data[i]) for i in range(len(data)))

    def categories(
        self,
        *,
        client_key: Optional[str] = None,
        type: Optional[str] = "featured",
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        contentfilter: Optional[str] = "off",
    ) -> Tuple[Category]:
        params = {
            "key": self.api_key,
            "client_key": client_key,
            "type": type,
            "country": country,
            "locale": locale,
            "contentfilter": contentfilter,
        }
        data = get(f"{self.BaseUrl}categories", params=params).json()["tags"]
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(Category(data[i]) for i in range(len(data)))

    def search_suggestions(
        self,
        q: str,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
    ) -> Tuple[str]:
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
        }
        data = get(f"{self.BaseUrl}search_suggestions", params=params).json()
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(i for i in data)

    def autocomplete(
        self,
        q: str,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
    ) -> Tuple[str]:
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
        }
        data = get(f"{self.BaseUrl}autocomplete", params=params).json()
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(i for i in data)

    def trending_terms(
        self,
        q: str,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
    ) -> Tuple[str]:
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
        }
        data = get(f"{self.BaseUrl}trending_terms", params=params).json()
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(i for i in data)

    def registershare(
        self,
        id: str,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
        q: Optional[str] = None,
    ):
        params = {
            "key": self.api_key,
            "id": id,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
            "q": q,
        }
        return get(f"{self.BaseUrl}registershare", params=params).json()

    def posts(
        self,
        ids: str,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        media_filter: Optional[str] = None,
    ) -> Tuple[str]:
        params = {
            "key": self.api_key,
            "ids": ids,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "media_filter": media_filter,
        }
        data = get(f"{self.BaseUrl}posts", params=params).json()
        try:
            data = data["results"]
        except KeyError:
            raise TenorAPIError(data)
        return tuple(i for i in data)
