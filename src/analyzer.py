import pandas as pd
from textblob import TextBlob
from typing import List, Dict, Tuple
from collections import Counter

class Analyzer:
    def __init__(self):
        pass
    
    def analyze_sentiment(self, text: str) -> float:
        """
        Analyze sentiment of a text using TextBlob
        Args:
            text: Text to analyze
        Returns:
            Sentiment score (-1 to 1)
        """
        return TextBlob(text).sentiment.polarity
    
    def get_top_posters(self, tweets: List[Dict]) -> List[Tuple[str, int]]:
        """
        Get top posters from tweet data
        Args:
            tweets: List of tweet dictionaries
        Returns:
            List of tuples (user_id, count)
        """
        author_counts = Counter(tweet['author_id'] for tweet in tweets)
        return author_counts.most_common(10)
    
    def get_engagement_stats(self, tweets: List[Dict]) -> Dict:
        """
        Calculate engagement statistics
        Args:
            tweets: List of tweet dictionaries
        Returns:
            Dictionary with engagement metrics
        """
        total_likes = sum(tweet['public_metrics']['like_count'] for tweet in tweets)
        total_retweets = sum(tweet['public_metrics']['retweet_count'] for tweet in tweets)
        total_replies = sum(tweet['public_metrics']['reply_count'] for tweet in tweets)
        
        return {
            'total_tweets': len(tweets),
            'total_likes': total_likes,
            'total_retweets': total_retweets,
            'total_replies': total_replies,
            'avg_likes': total_likes / len(tweets) if tweets else 0,
            'avg_retweets': total_retweets / len(tweets) if tweets else 0,
            'avg_replies': total_replies / len(tweets) if tweets else 0
        }
    
    def analyze_tweets(self, tweets: List[Dict]) -> Dict:
        """
        Perform comprehensive analysis on tweets
        Args:
            tweets: List of tweet dictionaries
        Returns:
            Dictionary containing analysis results
        """
        if not tweets:
            return {}
        
        # Calculate sentiment scores
        sentiment_scores = [self.analyze_sentiment(tweet['text']) for tweet in tweets]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        
        # Get engagement stats
        engagement_stats = self.get_engagement_stats(tweets)
        
        # Get top posters
        top_posters = self.get_top_posters(tweets)
        
        return {
            'sentiment_analysis': {
                'average_sentiment': avg_sentiment,
                'positive_tweets': len([s for s in sentiment_scores if s > 0]),
                'negative_tweets': len([s for s in sentiment_scores if s < 0]),
                'neutral_tweets': len([s for s in sentiment_scores if s == 0])
            },
            'engagement': engagement_stats,
            'top_posters': top_posters
        } 