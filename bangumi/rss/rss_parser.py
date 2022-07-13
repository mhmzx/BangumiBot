import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

import bs4
import requests

from bangumi.entitiy import WaitDownloadItem

logger = logging.getLogger(__name__)

class RSSParser(ABC):

    def request_rss(self, url: str) -> bs4.BeautifulSoup:
        try:
            ret = requests.get(url)
        except Exception:
            return None
        if ret.status_code != 200:
            return None
        return bs4.BeautifulSoup(ret.text, "xml")

    @abstractmethod
    def is_matched(self, url: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def parse(self, content) -> List[WaitDownloadItem]:
        raise NotImplementedError()
