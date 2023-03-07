# Creating Jira tickets from batch changes

This batch change is an example of how to create tickets alongside changes in batch changes.
It will:

- Find repositories with `fmt.Sprintf`
- Open changesets to replace them with `strconv.Itoa`
- For each open changeset, create a Jira ticket mentioning the files that have been modified

It demonstrates how to use [steps.outputs](https://docs.sourcegraph.com/batch_changes/references/batch_spec_yaml_reference#steps-outputs) and [batch spec templating](https://docs.sourcegraph.com/batch_changes/references/batch_spec_templating).

## How to use
- Modify the `jira_project`, `jira_username`, `jira_sitename` flags with your own in `jira.batch.yml`
- Create a [JIRA API token](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/) and set it as the `JIRA_TOKEN` environment variable.

```bash
JIRA_TOKEN=mysecrettoken
src batch apply -f jira.batch.yaml
```

## Limitations
* Batch changes has a declarative syntax for code changes: if the state of the codebase has not changed between two runs, there will be no additional changesets created.
* It's up to the user to make sure that the steps the batch change runs are declarative.
* In this simple example, tickets are not "declarative": every time that the batch change runs, and changesets are created or updated, a new ticket will be created (instead of tickets being updated).
Hello World
