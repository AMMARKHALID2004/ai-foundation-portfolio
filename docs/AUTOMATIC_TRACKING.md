# How I use my GitHub checklist

**[Open my learning checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1).**

I use the checkboxes in this GitHub issue to record completed topics. GitHub Actions updates my portfolio after I change the issue. This runs on GitHub. I do not need Codex, an AI service, or a running local computer.

## When I finish a topic

1. I open my checklist while signed in to GitHub.
2. I tick the completed topic.
3. I wait for the [checklist workflow](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/actions/workflows/learning-checklist.yml) to finish.
4. I open [my progress tracker](PROGRESS.md) or [my learning log](LEARNING_LOG.md).

My checklist includes all 134 verified CampusX playlist videos. I reported videos 1–31 complete on 2026-10-15. I keep the earlier library and independent-task ticks. My study dates remain unknown. My video ticks do not tick independent exercises.

## What updates after a tick

- My checked-topic counts in PROGRESS.md and the module README.
- A record under the matching module's `learning/` folder.
- A link to my source file, if I include one in the checkbox text.
- Experiment and reflection forms for the new record.
- The module index and my learning log.

My tick means that I report the topic complete. It does not confirm supervisor review or completion of all course requirements. I add measured results and my own reflection to the new record. The workflow preserves those notes.

If I untick a topic, the counts decrease. Its record changes to **Not checked**. Its existing notes remain available. If I remove a topic from the issue, its record changes to **Removed from checklist**.

## My CampusX lessons

I use [my lesson index](../machine-learning/README.md) to find the next video. I tick its existing checkbox in the issue. I keep its video number, label, link, and section key intact. Actions updates the main playlist index and its section table. It creates a learning record in that section's `learning/` folder.

I save my own notebooks in the section's `notebooks/` folder. I use a name such as `video-032-binning-and-binarization.ipynb`. I add personal notes in `notes/` and results in `results/`. Related earlier notebooks stay in `completed-work/`; the section table links them.

The original guide topics remain in the issue's collapsed section. I keep those task statuses separate. I do not check an independent exercise just because I completed its lesson.

## Add a new topic

I edit the issue description. For extra work, I add a unique topic under the matching module heading. For example, under `ml-features`:

```markdown
- [ ] My feature selection practice
```

I can also link my notebook:

```markdown
- [ ] [My feature selection practice](https://github.com/AMMARKHALID2004/Machine-Learning/blob/main/feature-selection.ipynb)
```

The link above is a format example. I replace it with my actual file link. I save the issue description and tick the item after I complete the work. I keep each topic name unique within its module. I keep the module keys at the start of the headings.

| Key | My work |
| --- | --- |
| `ml-*` | My 12 playlist sections; I keep the exact keys shown in the issue |
| `refresh` | Python, NumPy, Pandas, plotting, and EDA |
| `pipeline` | Preprocessing and Pipeline practice |
| `course1` | Linear/logistic regression and supervised ML |
| `course2` | Advanced ML and model comparison |
| `unsupervised` | Optional clustering and related work |
| `pytorch` | PyTorch Basics |
| `videos` | PyTorch video practice |
| `deep-learning` | My MLP and CNN implementations |
| `evaluation` | Optional evaluation study |

## Where I put my notebooks

I save new playlist code in the matching ML section's `notebooks/` folder. I can also keep it in an existing learning repository and link it in the checklist. The workflow creates the learning record in the correct module. It does not move or run my notebook, copy datasets, or guess what I learned from file activity.

GitHub Actions saves its updates on GitHub. To get them in my local Anaconda workspace, I run `git pull --ff-only` from the repository root. I commit my own local edits before I pull.

## If an update fails

I open the workflow link above and read the failed run. After I fix the issue, I select **Re-run jobs**. I can also select **Run workflow** on `main` to rebuild from the current issue. The workflow always reads the latest issue description. It does not force-push over other changes.

The repository copy in [tracking/CHECKLIST.md](../tracking/CHECKLIST.md) is an automatic mirror. I edit the GitHub issue to change my ticks. My earlier local tools and [Jupyter entry form](../Track_my_learning.ipynb) remain optional. They run only when I start them. The former Codex hourly schedule is disabled.
