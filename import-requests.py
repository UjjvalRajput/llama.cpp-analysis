import requests

def fetch_issues(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch issues. Status code: {response.status_code}")
        return None

def analyze_issues(issues):
    if issues:
        print(f"Total number of issues: {len(issues)}")
        for issue in issues:
            print(f"Issue #{issue['number']}: {issue['title']}")
            print(f"URL: {issue['html_url']}")
            print(f"State: {issue['state']}")
            print(f"Created at: {issue['created_at']}")
            print(f"User: {issue['user']['login']}")
            print(f"Labels: {issue['labels']}")
    else:
        print("No issues found.")

def main():
    repo_owner = "ggerganov"
    repo_name = "llama.cpp"
    
    print(f"Fetching issues from {repo_owner}/{repo_name}...")
    issues = fetch_issues(repo_owner, repo_name)
    if issues:
        print("Issues fetched successfully.")
        print("Analyzing issues...")
        analyze_issues(issues)
    else:
        print("Failed to fetch issues.")

if __name__ == "__main__":
    main()
