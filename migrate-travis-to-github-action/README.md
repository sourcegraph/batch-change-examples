# Migrate from Travis CI to GitHub Actions

> NOTE: Sourcegraph Campaigns require the [Sourcegraph CLI](https://github.com/sourcegraph/src-cli) be [installed](https://github.com/sourcegraph/src-cli#installation) and [configured](https://github.com/sourcegraph/src-cli#setup) to point at your [Campaigns enabled](https://docs.sourcegraph.com/user/campaigns) Sourcegraph instance.

This campaign migrates Go projects from Travis CI to GitHub Actions.

What this action does:
1. Delete `.travis.yml` file if exists.
2. Copy over the template `go.yml` from your local machine (on which `src` is being executed) to `.github/workflows/go.yml` (contains jobs for linting and testing) in each repository.

---

```json
{
  "scopeQuery": "repohasfile:.travis.yml lang:go",
  "steps": [
    {
      "type": "command",
      "args": ["rm", "-f", ".travis.yml"]
    },
    {
      "type": "command",
      "args": ["mkdir", "-p", ".github/workflows"]
    },
    {
      "type": "command",
      "args": ["cp", "<path-to-file-on-your-local-machine>/go.yml", ".github/workflows/go.yml"]
    }
  ]
}
```

Save as `action.json` and execute

```
src -v actions exec -f action.json -create-patchset
```
