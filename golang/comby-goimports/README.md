# Rewriting Go imports with Comby

This batch change rewrites Go import paths for the `log15` package from `gopkg.in/inconshreveable/log15.v2` to `github.com/inconshreveable/log15` using [Comby](https://comby.dev/):

It can handle single-package import statements like these

```go
import "gopkg.in/inconshreveable/log15.v2"
```

and multi-package import statements like these:

```go
import (
	"io"

	"github.com/pkg/errors"
	"gopkg.in/inconshreveable/log15.v2"
)
```

---

```yaml
name: rewrite-log15-import
description: This batch change rewrites Go import paths for the `log15` package from `gopkg.in/inconshreveable/log15.v2` to `github.com/inconshreveable/log15` using [Comby](https://comby.dev/)

# Find all repositories that contain the import we want to change.
on:
  - repositoriesMatchingQuery: lang:go gopkg.in/inconshreveable/log15.v2

# In each repository
steps:
  # we first replace the import when it's part of a multi-package import statement
  - run: comby -in-place 'import (:[before]"gopkg.in/inconshreveable/log15.v2":[after])' 'import (:[before]"github.com/inconshreveable/log15":[after])' .go -matcher .go -exclude-dir .,vendor
    container: comby/comby
  # ... and when it's a single import line.
  - run: comby -in-place 'import "gopkg.in/inconshreveable/log15.v2"' 'import "github.com/inconshreveable/log15"' .go -matcher .go -exclude-dir .,vendor
    container: comby/comby

# Describe the changeset (e.g., GitHub pull request) you want for each repository.
changesetTemplate:
  title: Fix import path for log15 package
  body: Rewrites Go import paths for the `log15` package from `gopkg.in/inconshreveable/log15.v2` to `github.com/inconshreveable/log15` using [Comby](https://comby.dev/)
  branch: batch-changes/comby-go-fmt # Push the commit to this branch.
  commit:
    message: Fix import path for log15 package
  published: false
```

Save as `batch-batch.yaml` and execute

```
src batch preview -f batch-batch.yaml -namespace <your-user-or-org-name>
```
Hello World
