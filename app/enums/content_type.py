from enum import Enum

class ContentType(str, Enum):
    NEWS = "news"
    EVENT = "event"
    PROMO = "promo"