
import pandas as pd
from sklearn import svm
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV,train_test_split,StratifiedKFold
from sklearn.decomposition import PCA

def cutData(X):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=.2)
    return x_train, x_test, y_train, y_test

def grid(x_train, x_test, y_train, y_test):
    kfold = StratifiedKFold(n_splits=4)
    grid = GridSearchCV(SVC(), param_grid={"C": [1, 2, 3, 4], "gamma": [1, 0.1, 0.5, 0.01]}, cv=kfold)
    grid.fit(x_train, y_train)
    score = grid.score(x_test, y_test)
    print("最佳参数： %s 精确度： %0.3f" % (grid.best_params_, grid.best_score_))
    print('测试精度: %f' % score)
    pd.DataFrame(grid.cv_results_).T


if __name__ == '__main__':

    df = pd.read_csv('data/wordVecs.csv')
    y = df.iloc[:, 1]
    x = df.iloc[:, 2:]

    x_pca = PCA(n_components=10).fit_transform(x)

    X = StandardScaler().fit_transform(x_pca)

    x_train, x_test, y_train, y_test=cutData(X)
    grid(x_train, x_test, y_train, y_test)
