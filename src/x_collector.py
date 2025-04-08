import tweepy
import pandas as pd
from typing import List, Dict
import os
from dotenv import load_dotenv

class XCollector:
    def __init__(self):
        load_dotenv()
        self.client = tweepy.Client(
            bearer_token=os.getenv('X_BEARER_TOKEN'),
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_TOKEN_SECRET')
        )
    
    def search_tweets(self, query: str, max_results: int = 100) -> List[Dict]:
        """
        Search for tweets based on a query
        Args:
            query: Search query (keywords or hashtags)
            max_results: Maximum number of results to return
        Returns:
            List of tweet data dictionaries
        """
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=['created_at', 'public_metrics', 'author_id']
            )
            return [tweet.data for tweet in tweets.data]
        except Exception as e:
            print(f"Error searching tweets: {e}")
            return []
    
    def get_user_info(self, user_ids: List[str]) -> List[Dict]:
        """
        Get user information for a list of user IDs
        Args:
            user_ids: List of user IDs
        Returns:
            List of user data dictionaries
        """
        try:
            users = self.client.get_users(ids=user_ids)
            return [user.data for user in users.data]
        except Exception as e:
            print(f"Error getting user info: {e}")
            return [] 