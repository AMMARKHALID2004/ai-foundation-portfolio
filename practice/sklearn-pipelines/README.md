# My ColumnTransformer to Pipeline practice

This folder gives me a teaching example and a notebook exercise. The example is supplied code. I do not count it as my own Course 1 implementation or model comparison.

I run the example from the repository root:

```bash
python practice/sklearn-pipelines/example.py
```

The example makes synthetic classification data. It splits the data before it fits preprocessing. It puts a `ColumnTransformer` and logistic regression in one `Pipeline`. It uses five-fold cross-validation on the training data. It then evaluates a separate test set. The printed scores show how the example works on synthetic data.

I complete [exercise.ipynb](exercise.ipynb) with my own code. I start with a simple baseline. I state my metric before I compare models. I use validation data or cross-validation while I develop the model. I use the test data after I make my model choices.

When I finish, I record my code, settings, validation scores, one useful figure, and final test result. I explain one error or limit. I add a reflection and link the work in [my tracker](../../docs/PROGRESS.md). [My workflow](../../docs/WORKFLOW.md) shows how to save it. If I later compare three models with a sound evaluation plan, I can link that work to Module 3 for review.

The example uses locally generated data and seed 42. I record my Python and package versions for my own run. References: [scikit-learn composition](https://scikit-learn.org/stable/modules/compose.html) and [leakage pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).
