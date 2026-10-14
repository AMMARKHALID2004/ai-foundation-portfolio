# Personal roadmap

Planning baseline: **2026-10-15 (Asia/Karachi)**. Weekly availability, deadline, prior ML theory and intended FYP topic are not yet confirmed, so this is a sequence rather than a dated promise.

## Credit existing learning

NumPy, Pandas, Matplotlib and Seaborn are reported complete. Scikit-learn preprocessing is complete through ColumnTransformer. Preserve and document those notebooks, do a short independent diagnostic, and close Python/OOP/environment/Git gaps only if the diagnostic reveals them. The whole refresh module remains partially verified until all its objectives have evidence.

## Common foundation, in guide order

| Order | Activity | Supervisor estimate | Evidence gate |
| --- | --- | --- | --- |
| 1 | Targeted Python/data/Git refresh | Guide: 1–2 weeks; shorten for verified skills | Representative existing work, independent extension, clean setup and Git workflow |
| Bridge | Pipeline practice from current ColumnTransformer level | A few focused sessions; personalized addition | Leakage-safe workflow and explanation |
| 2 | ML Specialization Course 1 | 3 weeks | Independent linear/logistic regression, loss/gradient/regularization explanations |
| 3 | ML Specialization Course 2 | 6–8 weeks | Neural-network concepts, bias/variance, trees/forests/boosting and ≥3-model comparison |
| 4 | Course 3, optional | 3 weeks if chosen | Clustering/anomaly/recommender/PCA experiments |
| 5 | PyTorch Learn the Basics | 1–2 weeks | Tensors, data, autograd, optimization and checkpoint round-trip |
| 6 | PyTorch Beginner Series | 1–2 weeks | Independent reproductions and debugging notes |
| 7 | Deep-learning implementation practice | 2 weeks | Student-written MLP/CNN loops, custom data, early stopping and error report |
| 8 | Evaluation foundation, optional module | 1 week if chosen | Leakage, imbalance, metrics and limitations audit |

Study loss functions, derivatives/gradients, matrix shapes and probability as needed alongside ML/PyTorch. This is supporting practice, not an extra compulsory course invented by the guide. Carry responsible evaluation through required outputs even if you omit its optional dedicated module.

The guide's approximately 14–19-week foundation estimate is a planning reference; it is not an estimate of your remaining time. Course completion is unconfirmed and existing implementations may shorten work after review.

## Select one specialization after PyTorch

| Track | Required path | Guide estimate | Future repository |
| --- | --- | --- | --- |
| Computer Vision | CS231n + Hugging Face CV; selected fast.ai is optional | 12–16 weeks | `computer-vision-specialization` |
| LLMs | HF LLM required core (1–7, 9) + selected Full Stack LLM Bootcamp; advanced 10–12, CS336 elective | 12–18 weeks | `llm-specialization` |
| AI Agents | First HF LLM chapters 1–5 and 9; then HF Agents + MCP + selected Microsoft lessons | 10–14 weeks after LLM prerequisites | `ai-agents-specialization` |

No specialization is selected yet. Select based on the intended FYP problem and supervisor approval. Implement multi-agent systems only with a measured advantage over a simpler single-agent approach.

## Finish the capstone

Use a separate `fyp-ai-capstone` repository. Complete the substantial evaluated project (guide: 3–5 weeks within track duration), then polish the repository, report and demo (1–2 weeks). Use [the capstone blueprint](../blueprints/capstone.md) and [submission checklist](SUBMISSION_CHECKLIST.md). Course availability and compute costs must be checked when enrolling or running experiments; the source guide's September 2026 access claims are not reverified here.
