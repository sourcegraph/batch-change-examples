# Batch Changes examples

Example batch specs to get you started with Batch Changes. Contributions welcome!

## Getting started

Take a look at the [Sourcegraph documentation on Batch Changes](https://docs.sourcegraph.com/batch_changes) to learn what batch changes are and how to run them.

## Examples

- [Rewrite Go import paths using Comby](comby-goimports/README.md)
- [Refactor Go code with Comby](comby-go-refactor/README.md)
- [Open Jira tickets alongside changesets](jira-tickets/README.md)
- [Open GitHub tickets alongside changesets (declarative)](github-issues/README.md)
- [Update the Docker Hub username in Circle CI configurations](update-circle-ci-config/update-circle-ci-config.batch.yaml)
- [Update deprecated GraphQL API query](update-api-query/replace-viewer-configuration.yaml)
- [Migrate from Python 2 to 3](python-refactor/README.md)
- [Update package.json for NPM dependencies](npm-package-update/README.md)
- [Rewrite `interface{}` to `any` in Go 1.18 code](go-interface-to-any/interface-to-any.spec.yml)

For a list of static-checker style linting rules for go, also see [comby go-patterns](https://github.com/comby-tools/go-patterns).

## Other examples

Also see how Batch Changes can help respond to a vulnerability with this [example](https://github.com/sourcegraph/log4j-cve-code-search-resources/tree/c70aeb6236f12c22c7c19e9b3fa54b2049213e29/batch-changes)
This is a test again!
