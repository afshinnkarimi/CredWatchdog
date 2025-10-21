from dotenv import load_dotenv
import os, requests


gitlab_token = os.getenv("GITLAB_TOKEN")
gitlab_address = os.getenv("GITLAB_ADDRESS")

gitlab_url = f"https://{gitlab_address}/api/v4/personal_access_tokens"

resp = requests.get(gitlab_url, headers={"PRIVATE-TOKEN": gitlab_token})

print(resp.content)