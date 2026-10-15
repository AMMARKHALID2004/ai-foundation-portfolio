# My automatic topic tracker

**[Open my checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1).**

I use GitHub issue checkboxes and GitHub Actions. The workflow runs on GitHub when I edit the issue. I do not need a running local computer. The former Codex schedule stays disabled.

## When I finish a topic

1. I save and push my notebook or source in the matching folder.
2. I tick the topic in my issue.
3. I wait for [the workflow](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/actions/workflows/learning-checklist.yml).
4. I open [my progress](PROGRESS.md) or [my learning log](LEARNING_LOG.md).

Actions updates my topic counts, the topic README, and its `learning/` index. It creates experiment and reflection forms for a newly checked topic. It does not run my notebook or infer a measured result.

If I untick a topic, its count decreases and its record says **Not checked**. Its notes remain. Removing a topic retains its record with **Removed from checklist**. My actual dates and supervisor review remain separate.

## My topic keys

| Key | Folder |
| --- | --- |
| `numpy` | `numpy` |
| `pandas` | `pandas` |
| `matplotlib` | `matplotlib` |
| `seaborn` | `seaborn` |
| `ml-foundations` | `machine-learning/foundations` |
| `ml-data` | `machine-learning/data-collection` |
| `ml-cleaning` | `machine-learning/data-cleaning` |
| `ml-eda` | `machine-learning/exploratory-data-analysis` |
| `ml-preprocessing` | `machine-learning/preprocessing` |
| `ml-pca` | `machine-learning/dimensionality-reduction` |
| `ml-regression` | `machine-learning/regression` |
| `ml-classification` | `machine-learning/classification` |
| `ml-trees` | `machine-learning/decision-trees` |
| `ml-ensembles` | `machine-learning/ensembles` |
| `ml-clustering` | `machine-learning/clustering` |
| `ml-model-selection` | `machine-learning/model-selection` |
| `ml-projects` | `machine-learning/projects` |

I can add a unique topic under a matching heading. I can use a notebook link as its label. I keep the key intact. I use topic names for my work.

The repository copy in [tracking/CHECKLIST.md](../tracking/CHECKLIST.md) is a generated mirror. I change ticks in the GitHub issue. I commit my local work before I pull the automatic updates.

If a run fails, I read its log and select **Re-run jobs** after I fix the cause. I can also choose **Run workflow** on `main`. The workflow reads the current issue and does not force-push over other work.

My [optional Jupyter form](../Track_my_learning.ipynb) creates local records only when I run it. It does not set checklist ticks.
