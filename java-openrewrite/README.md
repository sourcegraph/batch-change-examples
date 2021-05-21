# Running Rewrite recipes over Java code

This batch change uses OpenRewrite's [Rewrite](https://github.com/openrewrite/rewrite) to auto-format Java code.

It does this in three steps:

1. It adds the `org.openrewrite.rewrite` plugin to `build.gradle` files.
2. It adds the `"AutoFormat"` recipe.
3. It executes the rewrite

This follows the [Rewrite Quickstart](https://docs.openrewrite.org/getting-started/getting-started) and also uses the same repository.

That, of course, can be adopted to use any other repository and JDK version (the tutorial requires JDK8, which is why the Docker image used here is `grade:7.0-jdk8`.
