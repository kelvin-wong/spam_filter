### Introduction
This is a simple program to determine the degree of spam/abuse using the [profanity-check](https://github.com/vzhou842/profanity-check) library.

### Installation
```
git clone git@github.com:kelvin-wong/spam_filter.git
cd spam_filter

# create python virtual env
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

### Usage
```
python3 main.py <api_url>
```

### Test
```
python3 tests.py
```

### Improvements
Currently, the compression rate of the content is used as a key metric to detect keyword stuffing. To get a more accurate result, some statistical metrics of the content should be considered as the keys such as the frequency of the word and standard deviation of the word. By using those statistical metrics, it can tell how the word repeat and spam over the content. To be more sophisticated, some NLP techniques may be used to find out all the words which are related and in a similar meaning.