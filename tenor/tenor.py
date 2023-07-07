from __future__ import annotations
import httpx
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class GIF:
    BaseUrl = "https://tenor.googleapis.com/v2/"

    def __init__(self, api_key: str):
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
    ):
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
        return httpx.get(f"{self.BaseUrl}search", params=params).json()

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
    ):
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
        return httpx.get(f"{self.BaseUrl}featured", params=params).json()

    def categories(
        self,
        *,
        client_key: Optional[str] = None,
        _type: Optional[str] = "featured",
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        contentfilter: Optional[str] = "off",
    ):
        params = {
            "key": self.api_key,
            "client_key": client_key,
            "type": _type,
            "country": country,
            "locale": locale,
            "contentfilter": contentfilter,
        }
        return httpx.get(f"{self.BaseUrl}categories", params=params).json()

    def search_suggestions(
        self,
        q: str = None,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
    ):
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
        }
        return httpx.get(f"{self.BaseUrl}search_suggestions", params=params).json()

    def autocomplete(
        self,
        q: str = None,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
    ):
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
        }
        return httpx.get(f"{self.BaseUrl}autocomplete", params=params).json()

    def trending_terms(
        self,
        q: str = None,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
    ):
        params = {
            "key": self.api_key,
            "q": q,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
        }
        return httpx.get(f"{self.BaseUrl}trending_terms", params=params).json()

    def registershare(
        self,
        _id: str = None,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        limit: Optional[int] = 20,
        q: Optional[str] = None,
    ):
        params = {
            "key": self.api_key,
            "id": _id,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "limit": limit,
            "q": q,
        }
        return httpx.get(f"{self.BaseUrl}registershare", params=params).json()

    def posts(
        self,
        ids: str = None,
        *,
        client_key: Optional[str] = None,
        country: Optional[str] = "US",
        locale: Optional[str] = "en_US",
        media_filter: Optional[str] = None,
    ):
        params = {
            "key": self.api_key,
            "ids": ids,
            "client_key": client_key,
            "country": country,
            "locale": locale,
            "media_filter": media_filter,
        }
        return httpx.get(f"{self.BaseUrl}posts", params=params).json()
