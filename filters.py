from profanity_check import predict_prob
import zlib
import math

__all__ = ('BadLanguageFilter', 'KeywordStuffingFilter', 'LengthCheckerFilter')


class BaseFilter:
    def __init__(self):
        pass

    def filter(self, text):
        raise NotImplementedError


class BadLanguageFilter(BaseFilter):
    def filter(self, text):
        return predict_prob([text])[0] * 10


class KeywordStuffingFilter(BaseFilter):
    """
    Reference:
    https://stackoverflow.com/questions/16961274/how-to-detect-keyword-stuffing#17524090
    """
    def filter(self, text):
        compressed_text = zlib.compress(text.encode(), 9)
        ratio = len(text) / len(compressed_text)

        if len(compressed_text) > len(text) or ratio <= 2:
            return 0

        return min(10, int(math.ceil(ratio - 2) * 5))


class LengthCheckerFilter(BaseFilter):
    def __init__(self, min_length):
        super().__init__()
        self.min_length = min_length

    def filter(self, text):
        return 0 if len(text) > self.min_length else 10
