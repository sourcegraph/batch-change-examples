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

Using these features here is not necessary; the batch spec is a good practical
example of how one could use them and extend their use.

See `eslint-fix.simple.spec.yaml` for a functionally equivalent batch spec that
only uses a single step. The batch spec using `steps.outputs` and `steps.if` can
serve as a ready-to-use
