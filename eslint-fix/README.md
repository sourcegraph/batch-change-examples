# Run `eslint --fix` in repositories with an eslint configuration

This batch change finds repositories that have either an `.eslint`, an
`.eslintrc.js` or an `eslintrc.json` file at their root.

It then uses
[`steps.outputs`](https://docs.sourcegraph.com/batch_changes/references/batch_spec_yaml_reference#steps-outputs)
to dynamically construct an output in YAML format.

Then, in the other two steps, it uses
[`steps.if`](https://docs.sourcegraph.com/batch_changes/references/batch_spec_yaml_reference#steps-if)
combined with [batch spec
templating](https://docs.sourcegraph.com/batch_changes/references/batch_spec_templating)
to conditionally install and run `eslint --fix` either with NPM or with Yarn.
