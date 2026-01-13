import tweepy
from django.shortcuts import render

# Twitter API Credentials
BEARER_TOKEN = "YOUR_BEARER_TOKEN"

def fetch_tweets(request):
    tweets_data = []
    error = None
    username = None

    if request.method == "POST":
        username = request.POST.get("username").strip().replace("@", "")
        
        # Initialize Tweepy Client (API v2)
        client = tweepy.Client(bearer_token=BEARER_TOKEN)

        try:
            # 1. Get User ID from Username
            user = client.get_user(username=username)
            
            if user.data:
                user_id = user.data.id
                
                # 2. Fetch Recent Tweets
                # max_results must be between 5 and 100
                response = client.get_users_tweets(id=user_id, max_results=10)
                
                if response.data:
                    for tweet in response.data:
                        tweets_data.append(tweet.text)
                else:
                    error = "No recent tweets found for this user."
            else:
                error = "User not found."
                
        except tweepy.TweepyException as e:
            error = f"Twitter API Error: {str(e)}"
        except Exception as e:
            error = f"An unexpected error occurred: {str(e)}"

    return render(request, 'tweets.html', {
        'tweets': tweets_data, 
        'error': error, 
        'username': username
    })