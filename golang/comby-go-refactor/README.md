# Refactoring Go code with Comby

This batch change rewrites Go statements from

```go
fmt.Sprintf("%d", number)
```

to

```go
strconv.Itoa(number)
```

since they are equivalent.

And then runs `gofmt` over the repository.

---

```yaml
name: comby-go-fmt
description: Run `comby` and `go fmt`

# Find all repositories that contain a README.md file.
on:
  - repositoriesMatchingQuery: lang:go fmt.Sprintf("%d", :[v]) patterntype:structural

steps:
  - run: comby -in-place 'fmt.Sprintf("%d", :[v])' 'strconv.Itoa(:[v])' ${{ join repository.search_result_paths " " }}
    container: comby/comby
  - run: goimports -w ${{ join previous_step.modified_files " " }}
    container: unibeautify/goimports

# Describe the changeset (e.g., GitHub pull request) you want for each repository.
changesetTemplate:
  title: Replacing fmt.Sprintf with strconv.Itoa
  body: This campiagn replaces `fmt.Sprintf` with `strconv.Itoa`
  branch: batch-changes/comby-go-fmt # Push the commit to this branch.
  commit:
    message: Replacing fmt.Sprintf with strconv.Iota
  published: true
```

Save as `batch-batch.yaml` and execute

```
src batch preview -f batch-batch.yaml -namespace <your-user-or-org-name>
```
Hello World
