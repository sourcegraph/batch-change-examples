# Creating and updating GitHub issues along with batch changes
This batch change is an example of how to create tickets alongside changesets.
It will:

- Find repositories with `fmt.Sprintf`
- Open changesets to replace them with `strconv.Itoa`
- For each open changeset, create a GH issue mentioning the files that have been modified

When reapplying the spec, it will
- first check for existing issues matching the changes and update them if they exist
- otherwise create new issues

It demonstrates how to use [steps.outputs](https://docs.sourcegraph.com/campaigns/references/campaign_spec_yaml_reference#steps-outputs) and [campaigns spec templating](https://docs.sourcegraph.com/campaigns/references/campaign_spec_templating).


**Note**: by convention, all the issues tracked by this script must be named `batch-change/<batch-change-name>`. In this example `batch-change/refactor-go-gh-issue`

## How to
- Modify the `gh_username` flag with your own in `gh-issues.batch.yml`
- Create a [GitHub Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) and set it as the `GH_TOKEN` environment variable.

```bash
export GH_TOKEN=mysecrettoken
src campaign apply -f gh.issues.batch.yml
```

## Limitations
* For each changeset, the script will load all the issues in the repository affected by the changeset. That is inefficient, and a way better solution would be to maintain an index of all batch changes associated issues.
* This does not work in a monorepo as it assumes that there is only one issue matching a given batch change in any given repository.
