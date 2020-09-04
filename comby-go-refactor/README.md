# Refactoring Go code with Comby

This campaign rewrites Go statements from

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
  - run: comby -in-place 'fmt.Sprintf("%d", :[v])' 'strconv.Itoa(:[v])' .go -matcher .go -exclude-dir .,vendor
    container: comby/comby
  - run: gofmt -w ./
    container: golang:1.15-alpine

# Describe the changeset (e.g., GitHub pull request) you want for each repository.
changesetTemplate:
  title: Replacing fmt.Sprintf with strconv.Itoa
  body: This campiagn replaces `fmt.Sprintf` with `strconv.Itoa`
  branch: campaign-comby-go-fmt # Push the commit to this branch.
  commit:
    message: Replacing fmt.Sprintf with strconv.Iota
  published: true
```

Save as `campaign-spec.yaml` and execute

```
src campaigns preview -f campaign-spec.yaml -namespace <your-user-or-org-name>
```
