# Refactoring Go code withComby

This action definition rewrites Go statements from

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

```json
{
  "scopeQuery": "lang:go fmt.Sprintf",
  "steps": [
    {
      "type": "docker",
      "image": "comby/comby",
      "args": [
        "-in-place",
        "fmt.Sprintf(\"%d\", :[v])",
        "strconv.Itoa(:[v])",
        ".go",
        "-matcher",
        ".go",
        "-d",
        "/work",
        "-exclude-dir",
        ".,vendor"
      ]
    },
    {
      "type": "docker",
      "image": "golang:1.14-alpine",
      "args": ["sh", "-c", "cd /work && gofmt -w ./"]
    }
  ]
}
```

Save as `action.json` and execute

```
src -v actions exec -f action.json -create-patchset
```
