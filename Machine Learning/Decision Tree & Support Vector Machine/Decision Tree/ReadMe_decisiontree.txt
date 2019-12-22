Code structure:
The file 'decision_tree.py' contains the code for the decision tree model. The model is trained on training data contained in the file MushroomTrain.csv 
and is tested for accuracy on the file MushroomTest.csv
The tree is given nodes based on 'Entropy. The lower the entropy the better it is because it has lesser loss. This model calcutaes the entropies at 
different levels and selects the best node possible. This process is repeated for the entire tree.

How to run the code:
Go to the command line and change to the directory where the decision_tree.py is located and type 'python decision_tree.py' and then you'll get the output
showing the following:
a. The expected result and the actual result for both training data and test data
b. The accuracy of the training data and test data
