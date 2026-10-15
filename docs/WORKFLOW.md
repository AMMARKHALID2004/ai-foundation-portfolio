# How I use this portfolio

I use [my GitHub checklist](https://github.com/AMMARKHALID2004/ai-foundation-portfolio/issues/1) to record topic completion. GitHub Actions updates my tracker after I tick a box. [Tracking instructions](AUTOMATIC_TRACKING.md) explain how I add topics. The steps below explain how I prepare evidence.

I use this page each time I finish a lesson, exercise, or module. I use short sentences and direct instructions in my notes. I follow the writing principles of [ASD-STE100](https://www.asd-ste100.org/about_STE.html).

## 1. Find the correct folder

I check [the roadmap](ROADMAP.md) and [the next-steps page](NEXT_STEPS.md). For the CampusX playlist, I use the matching section under `machine-learning/`. Each section has `notebooks/`, `notes/`, and `results/`. I start the filename with the playlist number, such as `video-032-binning-and-binarization.ipynb`. I keep earlier source copies in `completed-work/` with their source notes.

If I finish work in another GitHub repository, I link its exact file or commit in [PROGRESS.md](PROGRESS.md). I can also add my own explanation or extension in the matching module folder. I identify tutorial code and other authors' work.

## 2. Save evidence I can explain

I save my notebook in `notebooks/` or my program in `src/` inside the module. I write a short README or use [the module template](../templates/module-evidence.md). I record:

- What I did myself and which sources I used.
- The data source, licence or permission, and the data version.
- The Python packages, kernel, run command, and random seed.
- The data split, metric, measured result, and one figure when useful.
- One error or limit, what I learned, and my next action.

I restart the Jupyter kernel and run the notebook from the first cell. I check that all required cells work. I inspect the notebook before I publish it. I remove credentials, private data, and large or restricted datasets. I link a dataset source when I cannot publish the file.

## 3. Tick my completed topic

I open my GitHub checklist and tick the topic. GitHub Actions adds a module record and updates my topic counts. I do not edit the generated counts by hand. I add my actual study dates and supervisor feedback in [PROGRESS.md](PROGRESS.md) when I have them.

My checklist records topic completion. I keep full module requirements and the **Minimum outputs** table under review. I use **Complete — reviewed** only after my supervisor reviews the work.

## 4. Save the change on GitHub

I check the changed files before I commit:

```bash
git status --short
git diff --check
gh auth status
git add machine-learning/03-feature-engineering/notebooks/video-032-binning-and-binarization.ipynb
git commit -m "Add my video 032 binning practice"
git push origin main
```

The `git add` path is an example for video 032. I replace them with the files I changed. I add my code, result note, and reflection when they are ready. I check `git status --short` again after the push. I use GitHub CLI for repository and pull request work.

## Example: I finish the Pipeline exercise

I complete [exercise.ipynb](../practice/sklearn-pipelines/exercise.ipynb) in Jupyter Notebook. I add my own model, run steps, metric, figure, and reflection. I check the notebook from a fresh kernel. I tick **My independent Pipeline exercise** in my checklist. I link the notebook and record the actual finish date if I know it.

I do not mark Course 1 or the three-model comparison complete from this exercise alone. If I later compare three models with a sound test plan, I link that evidence in Module 3. I record the result only after I measure it.

## What I do next

I continue at video 032: Binning and Binarization. I then follow the verified playlist order in [my ML index](../machine-learning/README.md). I keep my existing Pipeline exercise as independent practice. I use [my next steps](NEXT_STEPS.md) for the exact actions.
