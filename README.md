# Tweet_popularity
Prediction of the popularity of a tweet about food recipes 

## Disclaimer
We will use the following features to train the models:
  - tf-idf a tweet (sum of the scoring of each n-gram)
  - publishing time
  - number of followers of the page that has published the tweet
  - number of hastags
  - number of quotation marks
  - number of exclamation marks
  - length of plain text
  - number of urls
  - number of emojis
  - number of tags

## Credentials
We will use secret tokens and secret api keys (stored in a credentials.txt file).
Get your own if you want to run the find_data.py script

## How to prepare dataset
- ### with find_data.ipynb retrieve tweets from desired pages.
- ### with features_text_extractor.ipynb extract relevant features from raw dataset.
- ### note that ther is a pre-retrieved dataset!

## How to train the models
- ### just run the notebooks/training.ipynb script and see the results
