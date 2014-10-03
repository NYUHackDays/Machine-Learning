import numpy as np
import sklearn
from sklearn.tree import *
from sklearn.datasets import *
 
iris = load_iris()
 
X = iris.data
y = iris.target
 
ds = zip(X, y)
np.random.shuffle(ds)
 
X = [a for a,b in ds]
y = [b for a,b in ds]
 
Xtrain = X[:125]
Xtest = X[125:]
 
ytrain = y[:125]
ytest = y[125:]
 
clr = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None, random_state=None, min_density=None, compute_importances=None, max_leaf_nodes=None)
 
def compute_tree():
 clr.fit(Xtrain, ytrain)
 print clr.score(Xtest, ytest)
 #with open('dtree.dot', 'w') as f:
  #explort_graphviz(clr, f, ['Septal length', 'Septal width', 'Petal length', 'Petal width'])
