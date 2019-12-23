In this project, we use Apriori principle to generate the frequent itemsets for a given dataset.
Here, we use a dataset of groceries to generate the frequent itemsets, items and rules.

The Apriori Principle:
If an itemset is frequent, then all of its subsets must also be frequent. Conversely, if an subset is infrequent, then all of its supersets must be infrequent, too.

The key idea of the Apriori Principle is monotonicity. By the anti-monotone property of support, we can perform support-based pruning:
∀X,Y:(X⊂Y)→s(X)≥s(Y)

Steps involved: 
1. Generate frequent itemsets of length k (initially k=1)
2. Repeat until no new frequent itemsets are identified
3. Generate length (k+1) candidate itemsets from length k frequent itemsets (Candidate Itemsets Generation and Pruning)
4. Prune length (k+1) candidate itemsets that contain subsets of length k that are infrequent (Candidate Itemsets Generation and Pruning)
5. Count the support of each candidate (Support Counting)
6. Eliminate length (k+1) candidates that are infrequent
