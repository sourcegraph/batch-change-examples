# Running jscodeshift in Batch Changes

This batch change is an example of running [jscodeshift](https://github.com/facebook/jscodeshift) in Batch Changes. This toy example simply replaces `console.log` statements by `console.warn` statements.

## How to

The [Transform module](https://github.com/facebook/jscodeshift#transform-module) in `warn-to-log.ts` defines what changes will be executed through the AST-to-AST transform tool.
