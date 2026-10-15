# Working preferences for this portfolio

- Ammar does not want Codex to run tracking automation. Keep its hourly schedule disabled. The source of truth is GitHub issue #1, My learning checklist. GitHub Actions runs `scripts/update_checklist.py` after checkbox edits. Read `docs/AUTOMATIC_TRACKING.md`. Preserve manual notes, source snapshots, actual dates, and supervisor review. A tick records reported topic completion, not supervisor approval.
- Write student-facing portfolio pages in Ammar's first-person voice ("I" and "my"). Use ASD-STE100 principles: short sentences, direct verbs, one clear action per step, and consistent terms. Keep source snapshots and attribution intact. Do not claim formal ASD-STE100 compliance without a full standard check.
- Use GitHub CLI (`gh`) and Git for GitHub work; prefer them over browser interaction.
- The student uses Anaconda and Jupyter Notebook. Make that the primary documented workflow.
- Prefer uv for package installation. Keep a clearly documented pip alternative for other users.
- Keep environments separate from Anaconda's base environment when installing new dependencies. Do not change the student's existing environments just to edit documentation.
- Preserve prior completed work and source attribution. Record source repository/commit and any portability edits when importing notebooks.
- Preserve historical notebook results in their original repositories. Public imported copies have cleared outputs; supporting assets stay ignored locally and are fetched with the GitHub CLI helper. Do not invent study dates, original contributions, module completion or supervisor approval.
- The student explicitly authorized merging the five portfolio updates on 2026-10-15. Do not ask again for those merges or routine fixes within the same authorized repository-organization task.
