# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import argparse

parser = argparse.ArgumentParser(description='Parse jira ticket attributes')
parser.add_argument("--summary", help="summary of the issue to be created", default="")
parser.add_argument("--description", help="description of the issue to be created", default="")
parser.add_argument("--campaign_name", help="description of the issue to be created", default="")
parser.add_argument("--jira_sitename", help="Name of your site. Can be found in the site URL https://<mysite>.atlassian.net/", required=True)
parser.add_argument("--jira_username", help="Jira email address", required=True)
parser.add_argument("--jira_token", help="Jira API token. ", required=True)
parser.add_argument("--jira_project", help="The project key where issues will be created. Eg. 'MP' ", required=True)
args = parser.parse_args()

url = "https://" + args.jira_sitename + ".atlassian.net/rest/api/3/issue/"

auth = HTTPBasicAuth(args.jira_username, args.jira_token)

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = {
  "update": {},
  "fields": {
    "summary": args.summary,
    "issuetype": {
      "id": "10000"
    },
    "project": {
      "id": "10000"
    },
    "customfield_10011": "go_refactor",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "text": args.description,
              "type": "text"
            }
          ]
        }
      ]
    },
    "labels": [
      "sourcegraph-campaigns",
    ],
  }
}


if len(args.campaign_name) > 0:
    payload['fields']['labels'].append(args.campaign_name)

payload = json.dumps(payload)




response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

try:
    issue = json.loads(response.text)["key"]
    link = "https://"+args.jira_sitename+".atlassian.net/secure/RapidBoard.jspa?rapidView=1&modal=detail&projectKey="+args.jira_project+"&selectedIssue="+issue
    print(link)
except:
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
