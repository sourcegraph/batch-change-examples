# Rewriting Go imports with Comby

> NOTE: Sourcegraph Campaigns requires the [Sourcegraph CLI](https://github.com/sourcegraph/src-cli) be [installed](https://github.com/sourcegraph/src-cli#installation) and [configured](https://github.com/sourcegraph/src-cli#setup) to point at your [Campaigns enabled](https://docs.sourcegraph.com/user/campaigns) Sourcegraph instance.

This action definition rewrites Go import paths for the `log15` package from `gopkg.in/inconshreveable/log15.v2` to `github.com/inconshreveable/log15` using [Comby](https://comby.dev/):

```json
{
  "scopeQuery": "lang:go gopkg.in\/inconshreveable\/log15.v2",
  "steps": [
    {
      "type": "docker",
      "image": "comby/comby",
      "args": [
        "-in-place",
        "import (:[before]\"gopkg.in/inconshreveable/log15.v2\":[after])",
        "import (:[before]\"github.com/inconshreveable/log15\":[after])",
        ".go",
        "-matcher",
        ".go",
        "-d",
        "/work",
        "-exclude-dir",
        ".,vendor"
      ]
    }
  ]
}
```

Save as `action.json` and execute:

```
src -v actions exec -f action.json -create-patchset
```
