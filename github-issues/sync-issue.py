import requests
from requests.auth import HTTPBasicAuth
import json
import argparse

parser = argparse.ArgumentParser(description='Parse GH issue instructions')
parser.add_argument("--repository", help="the GitHub repository where the issue will live", required=True)
parser.add_argument("--batch_change_name", help="the name of the batch_change the issue is created from", required=True)
parser.add_argument("--description", help="the issue description text", required=True)
parser.add_argument("--reopen", dest='reopen', action='store_true', help="reopen closed issues matching the change.")
parser.add_argument(
  "--labels",
  nargs="*",
  type=str,
  default=[],
  help="(optional) a list of labels, space is the separator, eg. --labels label1 label2 label3"
)
parser.add_argument("--gh_username", help="GitHub username", required=True )
parser.add_argument("--gh_token", help="GitHub PAT or machine access token, with push scope", required=True)
parser.set_defaults(reopen=False)
args = parser.parse_args()

repository = args.repository
batch_change_name = args.batch_change_name
description = args.description
reopen = args.reopen
labels = args.labels
GH_USERNAME = args.gh_username
GH_TOKEN = args.gh_token

URL = "https://api.github.com/repos/"

# Cut prefix if exist
if "github.com/" in repository:
    repository=repository[11:]

def check_for_issue(repository, batch_change_name):
    """Check if an issue corresponding to the batch change exists in a repository.
    By convention issues associated with a batch change need to be named 'batch-change/batch_change_name'.
    Returns the id of the issue, or 0 if there is no matching issue.
    Expects repository to be "owner/repo_name".
    """

    session = requests.Session()
    session.auth = (GH_USERNAME, GH_TOKEN)

    repo_url = URL +  repository + "/issues?per_page=100"
    if reopen:
        repo_url += "&state=all"

    res = session.get(repo_url)
    issues=res.json()

    if res.status_code == 401 or res.status_code == 404:
        raise Exception("Not authenticated. Did you set a GH_TOKEN environment variable with your PAT")

    while 'next' in res.links.keys():
        res=session.get(res.links['next']['url'])
        issues.extend(res.json())

    for issue in issues:
        if issue["title"] == "batch-change/"+batch_change_name:
            return issue["number"]
    return 0

def create_issue(repository, batch_change_name, description, labels):
    """Create an issue for the batch change.
    By convention issues associated with a batch change need to be named 'batch-change/batch_change_name'.
    """
    repo_url = URL +  repository + "/issues"
    auth = HTTPBasicAuth(GH_USERNAME, GH_TOKEN)

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = {
        "title": "batch-change/" + batch_change_name,
        "body": description,
        }

    if len(labels) > 0:
        payload["labels"] = labels

    payload = json.dumps(payload)

    response = requests.request(
       "POST",
       repo_url,
       data=payload,
       headers=headers,
       auth=auth
    )
    issue_number = json.loads(response.content.decode('utf-8'))["number"]
    print("https://github.com/"+repository+"/issues/"+str(issue_number))

def update_issue(repository, issue_id, description, label = []):
    """ Update an issue with a new description, and optionally label
    """
    repo_url = URL +  repository + "/issues/" + str(issue_id)
    auth = HTTPBasicAuth(GH_USERNAME, GH_TOKEN)

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = {
        "body": description,
        "state": "open"
        }

    if len(labels) > 0:
        payload["labels"] = labels

    payload = json.dumps(payload)

    response = requests.request(
       "PATCH",
       repo_url,
       data=payload,
       headers=headers,
       auth=auth
    )

    issue_number = json.loads(response.content.decode('utf-8'))["number"]
    print("https://github.com/"+repository+"/issues/"+str(issue_number))

if __name__ == "__main__":
    issue_id = check_for_issue(repository, batch_change_name)
    if issue_id == 0:
        create_issue(repository, batch_change_name, description, labels)
    else:
        update_issue(repository, issue_id, description, labels)
