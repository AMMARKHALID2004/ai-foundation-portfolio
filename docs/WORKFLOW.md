# How I use this portfolio

I now use [automatic tracking](AUTOMATIC_TRACKING.md) for routine file detection and learning records. I add lessons without code in [my Jupyter tracking notebook](../Track_my_learning.ipynb). The steps below explain how I prepare evidence and record full module completion.

I use this page each time I finish a lesson, exercise, or module. I use short sentences and direct instructions in my notes. I follow the writing principles of [ASD-STE100](https://www.asd-ste100.org/about_STE.html).

## 1. Find the correct folder

I check [the roadmap](ROADMAP.md) and [the next-steps page](NEXT_STEPS.md). I put new work in the matching folder under `modules/` or `practice/`. I keep earlier source copies in `completed-work/` with their source notes.

If I finish work in another GitHub repository, I link its exact file or commit in [PROGRESS.md](PROGRESS.md). I can also add my own explanation or extension in the matching module folder. I identify tutorial code and other authors' work.

## 2. Save evidence I can explain

I save my notebook in `notebooks/` or my program in `src/` inside the module. I write a short README or use [the module template](../templates/module-evidence.md). I record:

- What I did myself and which sources I used.
- The data source, licence or permission, and the data version.
- The Python packages, kernel, run command, and random seed.
- The data split, metric, measured result, and one figure when useful.
- One error or limit, what I learned, and my next action.

I restart the Jupyter kernel and run the notebook from the first cell. I check that all required cells work. I inspect the notebook before I publish it. I remove credentials, private data, and large or restricted datasets. I link a dataset source when I cannot publish the file.

## 3. Change the progress tracker

I find the correct row in [PROGRESS.md](PROGRESS.md). I add a link to my evidence. I use the actual study dates if I know them. I leave the dates as `Unknown` if I do not know them.

I use **In progress** while I work. I use **Evidence added** when the work and its run instructions are ready for review. I use **Complete — reviewed** only after my supervisor reviews that work. I put the real review date and feedback in the supervision log. A course video or a copied tutorial does not complete an original implementation requirement.

I also update the module README. I check only the tasks I completed. If I finish a required output, I update the **Minimum outputs** table in PROGRESS.md.

## 4. Save the change on GitHub

I check the changed files before I commit:

```bash
git status --short
git diff --check
gh auth status
git add practice/sklearn-pipelines/exercise.ipynb practice/sklearn-pipelines/README.md docs/PROGRESS.md
git commit -m "Record Pipeline exercise"
git push origin main
```

The `git add` paths are an example for the Pipeline exercise. I replace them with the files I changed. I add my code, result note, and reflection when they are ready. I check `git status --short` again after the push. I use GitHub CLI for repository and pull request work.

## Example: I finish the Pipeline exercise

I complete [exercise.ipynb](../practice/sklearn-pipelines/exercise.ipynb) in Jupyter Notebook. I add my own model, run steps, metric, figure, and reflection. I check the notebook from a fresh kernel. I update the Pipeline row in PROGRESS.md from **Not started** to **Evidence added**. I link the notebook and record the actual finish date if I know it.

I do not mark Course 1 or the three-model comparison complete from this exercise alone. If I later compare three models with a sound test plan, I link that evidence in Module 3. I record the result only after I measure it.

## What I do next

After ColumnTransformer, I do the Pipeline exercise. I then check Course 1 concepts and write my own linear and logistic regression. Next, I study Course 2 and compare at least three models. I move to PyTorch Basics, the beginner videos, and my own MLP/CNN training loops. Course 3 and the separate evaluation study are optional.

After the PyTorch foundation, I select one specialization with my supervisor. I use a separate repository for the selected track and another repository for the capstone. [The roadmap](ROADMAP.md) shows the full order.
