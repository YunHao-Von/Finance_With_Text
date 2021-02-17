import pandas as pd
from sklearn import tree
import graphviz
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import make_scorer, fbeta_score, accuracy_score
data=pd.read_csv("data.csv")
x_data=data[['MACD','slowj','score','n_vol','n_amount']]
y_data=data[['Go']]
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=0)
parameter_tree = {
    'max_depth': range(1, 10),
    'min_samples_leaf':[1,2,3,4,5]
}
clf = tree.DecisionTreeClassifier()
scorer = make_scorer(accuracy_score)
kfold=3
grid = GridSearchCV(clf, parameter_tree, scorer, cv=kfold)
grid = grid.fit(X_train, y_train)
print ("best score: {}".format(grid.best_score_))
print('Best parameters{}'.format(grid.best_params_))
clf=tree.DecisionTreeClassifier(max_depth=3,min_samples_leaf=1)
clf.fit(X_train,y_train)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render(r'jiliang')