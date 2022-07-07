# Updating npm dependencies

This batch change runs `npm-check-updates` and, if outdated changes are found in the `package.json` file, updates the dependencies to the latest version.

---

```
name: npm-update-package.json
description: Use NPM to update dependencies in package.json.

# NPM Update.

on:
  - repositoriesMatchingQuery: patternType:regexp file:package.json 

# In each repository
steps:
  - run: |
      npm install -g npm-check-updates 
      ncu -u
    container: node:16-alpine
# Describe the changeset (e.g., GitHub pull request) you want for each repository.
changesetTemplate:
  title: Update outdated npm modules
  body: Running npm-check-updates
  branch: batch changes/npm-update # Push the commit to this branch.
  commit:
    message: Updating outdated packages in package.json.
  published: false
```
