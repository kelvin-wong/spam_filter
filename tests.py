import unittest
from unittest_data_provider import data_provider
from filters import *
import main


def bad_languages():
    return (
        ('fuck',),
        ('shit',),
        ('ass',),
    )


def proper_languages():
    return (
        ('test',),
        ('Lorem ipsum dolor sit amet, consectetur adipiscing elit.',),
    )


class BadLanguageFilterTestCase(unittest.TestCase):
    def setUp(self):
        self.bad_language_filter = BadLanguageFilter()

    @data_provider(bad_languages)
    def test_filter_with_bad_languages(self, text):
        result = self.bad_language_filter.filter(text)
        self.assertGreater(result, 5)

    @data_provider(proper_languages)
    def test_filter_with_proper_languages(self, text):
        result = self.bad_language_filter.filter(text)
        self.assertLess(result, 5)


class LengthCheckerFilterTestCase(unittest.TestCase):
    def setUp(self):
        self.length_checker_filter = LengthCheckerFilter(10)

    def test_filter_with_short_text(self):
        result = self.length_checker_filter.filter('too short')
        self.assertEqual(result, 10)

    def test_filter_with_long_text(self):
        result = self.length_checker_filter.filter('long enough to pass')
        self.assertEqual(result, 0)


class KeywordStuffingFilterTestCase(unittest.TestCase):
    def setUp(self):
        self.keyword_stuffing_filter = KeywordStuffingFilter()

    def test_filter_with_stuffed_text(self):
        result = self.keyword_stuffing_filter.filter('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                     'Pellentesque dictum in diam eu tristique. Mauris vel leo nec ex '
                                                     'efficitur sodales at vitae nisi. Nulla facilisi. Integer '
                                                     'consectetur vitae velit in vehicula. In fringilla justo a '
                                                     'vehicula tempor. Vestibulum ante ipsum primis in faucibus orci '
                                                     'luctus et ultrices posuere cubilia Curae; Suspendisse vitae '
                                                     'tempus nisl. Quisque sit amet aliquet libero. Integer eu '
                                                     'elementum ligula. Nam feugiat dolor at diam tempus, '
                                                     'at auctor quam tempor. Duis sed volutpat libero, nec dignissim '
                                                     'justo. Nam nec eros ultricies, ultricies ex vel, '
                                                     'accumsan libero. Aenean eleifend sed metus a lobortis. Etiam eu '
                                                     'pellentesque dolor. Curabitur sit amet congue nulla. Fusce '
                                                     'tincidunt aliquam placerat. Phasellus consequat faucibus ex. '
                                                     'Cras vel mauris vitae nibh semper finibus. Praesent dictum '
                                                     'vestibulum turpis, non aliquam nisl. Donec lorem turpis, '
                                                     'pellentesque id vehicula sit amet, efficitur vitae libero. '
                                                     'Mauris at sapien nisl. Orci varius natoque penatibus et magnis '
                                                     'dis parturient montes, nascetur ridiculus mus. Keyword Keyword '
                                                     'Keyword Keyword Keyword Keyword Keyword Keyword Keyword Keyword '
                                                     'Keyword Keyword Keyword Keyword Keyword Keyword Keyword Keyword '
                                                     'Keyword Keyword Keyword Keyword Keyword Keyword Keyword '
                                                     'Maecenas tempus maximus odio id facilisis. Nulla sit amet '
                                                     'efficitur magna. Ut quam nibh, malesuada eget facilisis at, '
                                                     'porttitor ut sapien. Duis vitae mattis nunc. Lorem ipsum dolor '
                                                     'sit amet, consectetur adipiscing elit. Orci varius natoque '
                                                     'penatibus et magnis dis parturient montes, nascetur ridiculus '
                                                     'mus. Keyword stuffing Keyword '
                                                     'stuffing Keyword stuffing Keyword stuffing Keyword stuffing '
                                                     'Keyword stuffing Keyword stuffing Keyword stuffing Keyword '
                                                     'stuffing Keyword stuffing Keyword stuffing Keyword stuffing '
                                                     'Keyword stuffing Keyword stuffing Keyword stuffing Keyword '
                                                     'stuffing Keyword stuffing Keyword stuffing Keyword stuffing '
                                                     'Keyword stuffing Keyword stuffing Keyword stuffing Keyword '
                                                     'stuffing Keyword stuffing Keyword stuffing Keyword stuffing '
                                                     'Keyword stuffing Keyword stuffing Keyword stuffing Keyword '
                                                     'stuffing Keyword stuffing Keyword stuffing Keyword stuffing '
                                                     'Keyword stuffing Keyword stuffing Keyword stuffing Keyword '
                                                     'stuffing')
        self.assertGreater(result, 5)

    def test_filter_with_normal_text(self):
        result = self.keyword_stuffing_filter.filter('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                     'Pellentesque dictum in diam eu tristique. Mauris vel leo nec ex '
                                                     'efficitur sodales at vitae nisi. Nulla facilisi. Integer '
                                                     'consectetur vitae velit in vehicula. In fringilla justo a '
                                                     'vehicula tempor. Vestibulum ante ipsum primis in faucibus orci '
                                                     'luctus et ultrices posuere cubilia Curae; Suspendisse vitae '
                                                     'tempus nisl. Quisque sit amet aliquet libero. Integer eu '
                                                     'elementum ligula. Nam feugiat dolor at diam tempus, '
                                                     'at auctor quam tempor. Duis sed volutpat libero, nec dignissim '
                                                     'justo. Nam nec eros ultricies, ultricies ex vel, '
                                                     'accumsan libero. Aenean eleifend sed metus a lobortis. Etiam eu '
                                                     'pellentesque dolor. Curabitur sit amet congue nulla. Fusce '
                                                     'tincidunt aliquam placerat. Phasellus consequat faucibus ex. '
                                                     'Cras vel mauris vitae nibh semper finibus. Praesent dictum '
                                                     'vestibulum turpis, non aliquam nisl. Donec lorem turpis, '
                                                     'pellentesque id vehicula sit amet, efficitur vitae libero. ')
        self.assertLess(result, 5)


def mocked_empty_urlopen(url):
    import io
    return io.StringIO('[]')


def mocked_safe_urlopen(url):
    import io
    return io.StringIO('[{"projectId":"8182fad6-06df-4af4-9fad-311578efb835","projectName":"Test title",'
                       '"projectDescription":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque '
                       'dictum in diam eu tristique. Mauris vel leo nec ex efficitur sodales at vitae nisi. Nulla '
                       'facilisi. Integer consectetur vitae velit in vehicula.",'
                       '"categoryId":"b0666dcb-1713-4573-b8ae-f0f802628104","categoryName":"Test Category",'
                       '"createdAt":"2019-10-01T1313:45:30"}]')


def mocked_bad_urlopen(url):
    import io
    return io.StringIO('[{"projectId":"8182fad6-06df-4af4-9fad-311578efb835","projectName":"Test title",'
                       '"projectDescription":"Keyword ass Keyword ass Keyword ass Keyword ass Keyword ass Keyword ass'
                       'Keyword ass Keyword ass", '
                       '"categoryId":"b0666dcb-1713-4573-b8ae-f0f802628104","categoryName":"Test Category",'
                       '"createdAt":"2019-10-01T1313:45:30"}]')


class MainTestCase(unittest.TestCase):
    def test_main_with_empty_data(self):
        main.urllib.request.urlopen = mocked_empty_urlopen
        result = main.main('irrelevant')
        self.assertLess(result, 5)

    def test_main_with_safe_data(self):
        main.urllib.request.urlopen = mocked_safe_urlopen
        result = main.main('irrelevant')
        self.assertLess(result, 5)

    def test_main_with_bad_data(self):
        main.urllib.request.urlopen = mocked_bad_urlopen
        result = main.main('irrelevant')
        self.assertGreater(result, 5)


if __name__ == '__main__':
    unittest.main()
