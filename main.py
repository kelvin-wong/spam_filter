import json
import urllib.request
import sys
from statistics import mean
from filters import *


def main(url):
    json_contents = urllib.request.urlopen(url).read()
    contents = json.loads(json_contents)
    if len(contents) < 1:
        return 0

    filters = [LengthCheckerFilter(100), BadLanguageFilter(), KeywordStuffingFilter(), ]
    results = mean([mean([f.filter(content['projectDescription']) for f in filters]) for content in contents])

    return results


if __name__ == '__main__':
    main(sys.argv[1])
