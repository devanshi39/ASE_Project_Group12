## Problem Statement
The problem statement is to develop a multi-objective semi-supervised explanation system that can extract useful succinct summaries from a given dataset while working within a limited budget of accessing the values of any one example. The system should be able to select good examples from the dataset based on the extracted summary.

The system should be tested on 10 different datasets with multiple goals using various methods, including sway1 and sway2, and xpln1 and xpln2. The performance measures should rank the data using the Zitzler predicate and normalize those ranks to 1..100. The system should guess the top n items of the data within a given budget, evaluate those top n guesses, and collect the distribution of those final evaluations. The summarization methods should aim to minimize the sum of the final evaluations.

The results should be presented by comparing the preferred method to at least one prior state-of-the-art method, selecting items at random, and one or more human-level sampling processes. The results should be repeated 20 times with different random number seeds and summarized using median and spread. Non-parametric effect size and significance tests should be performed.

The discussion should include a clear commentary on what worked best, acknowledge any unusual results, and provide suggestions for future work. Threats to validity should be discussed, and any bigger picture insights not present in the rest of the text should be included.
