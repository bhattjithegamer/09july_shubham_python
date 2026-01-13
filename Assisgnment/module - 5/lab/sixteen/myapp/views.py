import requests
from django.shortcuts import render

# Replace with your actual GitHub Personal Access Token
GITHUB_TOKEN = "your_github_token_here"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def github_manager(request):
    user_data = None
    repo_result = None
    error = None

    # 1. Fetch User Data (GET Request)
    user_url = "https://api.github.com/user"
    try:
        user_response = requests.get(user_url, headers=HEADERS)
        if user_response.status_code == 200:
            user_data = user_response.json()
        else:
            error = f"Failed to fetch user: {user_response.json().get('message')}"
    except Exception as e:
        error = str(e)

    # 2. Create Repository (POST Request)
    if request.method == "POST":
        repo_name = request.POST.get("repo_name")
        create_url = "https://api.github.com/user/repos"
        payload = {
            "name": repo_name,
            "description": "Created via Django API",
            "private": False
        }
        
        try:
            repo_response = requests.post(create_url, headers=HEADERS, json=payload)
            if repo_response.status_code == 201:
                repo_result = f"Successfully created: {repo_response.json().get('html_url')}"
            else:
                error = f"Failed to create repo: {repo_response.json().get('message')}"
        except Exception as e:
            error = str(e)

    context = {
        'user': user_data,
        'repo_result': repo_result,
        'error': error
    }
    return render(request, 'github.html', context)