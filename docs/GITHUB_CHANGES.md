# GitHub integration

GitHub read access worked for `AMMARKHALID2004`, but creating a review branch and tree returned **403: Resource not accessible by integration**. No GitHub changes or pull requests were successfully created.

The available connector exposes existing-repository edits, branches and pull requests, but its current access rejected writes. It does not expose new-repository creation. The preferred standalone `ai-foundation-portfolio` repository is initialized locally. A transitional `fyp-foundation/` mirror is prepared for the Machine-Learning review branch once upload access works.

The account's terminal GitHub login was also invalid when checked. The connector's installation listing returned no installations. GitHub connection/installation access or a fresh terminal login needs attention before upload. Do not use a token from source files or commit credentials to work around this.

## Prepared changes

| Repository | Local preparation | GitHub status |
| --- | --- | --- |
| Machine-Learning | Foundation mirror, README, dependencies, ignore rules and corrected ColumnTransformer notebook | Upload blocked; no PR |
| Numpy | Topic README, starter dependencies and ignore rules | Upload blocked; no PR |
| Pandas | Topic README, starter dependencies and ignore rules | Upload blocked; no PR |
| Matplotlib | Topic README, starter dependencies and ignore rules | Upload blocked; no PR |
| Seaborn | Topic README, starter dependencies and ignore rules | Upload blocked; no PR |

Existing-repo additions are preserved under the workspace's `github-proposals/` directory. They retain current notebook locations and tracked checkpoints. The ColumnTransformer correction changes the notebook itself and clears stale outputs; it does not claim student completion.
