from x_collector import XCollector
from analyzer import Analyzer
import json

def main():
    # Initialize components
    collector = XCollector()
    analyzer = Analyzer()
    
    # Example search query
    query = "#python OR #programming"
    max_results = 100
    
    # Collect tweets
    print(f"Collecting tweets for query: {query}")
    tweets = collector.search_tweets(query, max_results)
    
    if not tweets:
        print("No tweets found or error occurred during collection")
        return
    
    # Get user information for top posters
    user_ids = [tweet['author_id'] for tweet in tweets]
    users = collector.get_user_info(user_ids)
    
    # Analyze tweets
    print("Analyzing tweets...")
    analysis_results = analyzer.analyze_tweets(tweets)
    
    # Print results
    print("\nAnalysis Results:")
    print(json.dumps(analysis_results, indent=2))
    
    # Print top posters with their usernames
    print("\nTop Posters:")
    for user_id, count in analysis_results['top_posters']:
        user = next((u for u in users if u['id'] == user_id), None)
        username = user['username'] if user else "Unknown"
        print(f"@{username}: {count} tweets")

if __name__ == "__main__":
    main() 