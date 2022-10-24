This spec is an example of manipulating files with Batch Changes. It adds a license file along each README.md found in any repository.

Two different methods are demonstrated to add the file content:

1. `add-file.batch.yaml` embeds the file content in the batch spec itself using the [`steps.files`](https://docs.sourcegraph.com/batch_changes/references/batch_spec_yaml_reference#steps-files) element. `steps.files` has been supported since Sourcegraph 3.22.
2. `mount-file.batch.yaml` mounts the file content from the host filesystem using [`steps.mount`](https://docs.sourcegraph.com/batch_changes/references/batch_spec_yaml_reference#steps-mount). This has been supported since Sourcegraph 3.41 using `src batch preview` and `src batch apply`, and since Sourcegraph 4.1 when executing batch specs [on the server using `src batch remote`](https://docs.sourcegraph.com/batch_changes/how-tos/server_side_file_mounts).

Both specs also use [template variables](https://docs.sourcegraph.com/batch_changes/references/batch_spec_templating#template-variables) to generate the list of paths the license file should be added at.

### Whither `steps.files` or `steps.mount`?

`steps.files` is more useful when:

1. You need to support Sourcegraph versions before `steps.mount` was added, or
1. The file content is small and self-contained, and therefore isn't a hassle to embed within a batch spec, or
1. The file content needs to be dynamically generated using [template variables](https://docs.sourcegraph.com/batch_changes/references/batch_spec_templating#template-variables).

`steps.mount` is more useful when:

1. The file content is static, or
1. The file content is too large to embed in a YAML spec, or
1. The file is binary that cannot be represented within YAML.
