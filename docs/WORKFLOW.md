# How I add my work

## Choose a folder

I use `numpy/`, `pandas/`, `matplotlib/`, `seaborn/`, or a topic under `machine-learning/`. I save new notebooks in `notebooks/`. I use clear topic names such as `binning-and-binarization.ipynb`. I keep longer explanations in `notes/` and figures or measured summaries in `results/`.

I preserve imported notebooks and their source notes. I identify my own changes or add a separate extension. I keep reference solutions separate from my independent answers.

## Prepare my evidence

I select the FYP AI (Anaconda) kernel. I record my source, data permission, setup, split, metric, and seed when relevant. I add my own explanation, measured results, and limits. I restart the kernel and run my required cells.

I inspect the files before I publish them. I keep private data, credentials, large datasets, and saved models out of my commits. I add a source link when a dataset stays external.

## Save and track my work

From the repository root, I use this example:

```bash
git status --short
git diff --check
git add machine-learning/preprocessing/notebooks/binning-and-binarization.ipynb
git commit -m "Add my binning practice"
git push origin main
```

I replace the example path with my actual files. I then tick the topic in [my checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1). Actions updates my counts and creates a learning record with reflection and experiment forms. I fill those forms with my own observations.

I commit my local edits before I run `git pull --ff-only` to get Actions updates. I record actual study dates and supervisor feedback separately in [PROGRESS.md](PROGRESS.md).

## Add a new topic

I edit the issue description and add a unique checkbox under the matching topic key. For example, under `ml-preprocessing`:

```markdown
- [ ] My feature selection practice
```

I can make the text a Markdown link to my notebook. I leave the key at the start of its heading intact. [Tracking instructions](AUTOMATIC_TRACKING.md) list the keys.
