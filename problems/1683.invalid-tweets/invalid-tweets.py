import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweets_df = tweets.loc[tweets['content'].str.len() > 15,['tweet_id']].copy()
    return invalid_tweets_df