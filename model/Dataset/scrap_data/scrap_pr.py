from config import major_repos
from github_connectors.pull_request import get_recent_merged_pull_requests
from utils import select_unique_pairs, write_to_md

for repo in major_repos:
    recent_pull_requests = get_recent_merged_pull_requests(repo)
    unique_pull_request_pairs = select_unique_pairs(
        recent_pull_requests, recent_pull_requests // 4, recent_pull_requests * 4
    )
    write_to_md(repo, unique_pull_request_pairs)
