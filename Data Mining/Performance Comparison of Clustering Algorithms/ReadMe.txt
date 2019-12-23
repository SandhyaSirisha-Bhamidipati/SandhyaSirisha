We should know the difference between classification and clustering before we start off with this project.
Classification is used in supervised learning technique where predefined labels are assigned to instances by properties, on the contrary, 
clustering is used in unsupervised learning where similar instances are grouped, based on their features or properties.

In clustering, the similarity between two objects is measured by the similarity function where the distance between those two object is 
measured. Shorter the distance higher the similarity, conversely longer the distance higher the dissimilarity.

So, we choose to comapre two different clustering algorithms- K-Means and Hierarchical Agglomerative clustering algorithm.

K means is an iterative clustering algorithm that aims to find local maxima in each iteration.

Agglomerative implies that it is a "bottom-up" approach., each observation starts in its own cluster, and pairs of clusters are merged as 
one moves up the hierarchy.
Hierarchical clustering, as the name suggests is an algorithm that builds hierarchy of clusters. This algorithm starts with all the data 
points assigned to a cluster of their own. Then two nearest clusters are merged into the same cluster. In the end, this algorithm 
terminates when there is only a single cluster left.

So, here in this project we compare the performance measures from the classification report on the same dataset using botht he algorithms mentioned above.

Finally, after looking at the results we say that K-Means is a better way to cluster that Hierarchical Agglomerative clustering because 
Precision, Recall, F1-score, and Support values are more for K-means.
