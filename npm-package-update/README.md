# Updating npm dependencies

This batch change runs `npm-check-updates` and, if outdated changes are found in the `package.json` file, updates the dependencies to the latest version.

---

```
name: npm-update-package.json
description: Use NPM to update dependencies in package.json.

# NPM Update.

on:
  - repositoriesMatchingQuery: patternType:regexp file:package.json repo:sourcegraph-testing/docker-image-pin$

# In each repository
steps:
  - run: |
      apk add --update nodejs npm 
      npm install -g npm-check-updates 
      ncu -u
    container: alpine:3

# Describe the changeset (e.g., GitHub pull request) you want for each repository.
changesetTemplate:
  title: Update outdated npm modules
  body: Running npm-check-updates
  branch: campaigns/npm-update # Push the commit to this branch.
  commit:
    message: Updating outdated packages in package.json.
  published: false
```
