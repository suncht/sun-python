#-*- coding: utf-8 -*-
import sys
import os
import time
from sklearn import metrics
import numpy as np
import pickle as pickle


#朴素贝叶斯分类
def naive_bayes_classifier(train_x, train_y):
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB(alpha=0.01)
    model.fit(train_x, train_y)
    return model

#KNN邻近分类
def knn_classifier(train_x, train_y):
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    model.fit(train_x, train_y)
    return model
#Logistic回归分类
def logistic_regression_classifier(train_x, train_y):
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty='l2')
    model.fit(train_x, train_y)
    return model

#随机森林分类
def random_forest_classifier(train_x, train_y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=8)
    model.fit(train_x, train_y)
    return model
#决策树分类
def decision_tree_classifier(train_x, train_y):
    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    model.fit(train_x, train_y)
    return model

# Boosting决策树分类
def gradient_boosting_classifier(train_x, train_y):
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=200)
    model.fit(train_x, train_y)
    return model

# 支持向量机
def svm_classifier(train_x, train_y):
    from sklearn.svm import SVC
    model = SVC(kernel='rbf', probability=True)
    model.fit(train_x, train_y)
    return model

# 使用交叉验证的支持向量机
def svm_cross_validation(train_x, train_y):
    from sklearn.grid_search import GridSearchCV
    from sklearn.svm import SVC
    model = SVC(kernel='rbf', probability=True)
    param_grid = {'C': [1e-3, 1e-2, 1e-1, 1, 10, 100, 1000], 'gamma': [0.001, 0.0001]}
    grid_search = GridSearchCV(model, param_grid, n_jobs = 1, verbose=1)
    grid_search.fit(train_x, train_y)
    best_parameters = grid_search.best_estimator_.get_params()
    for para, val in best_parameters.items():
        print(para, val)
    model = SVC(kernel='rbf', C=best_parameters['C'], gamma=best_parameters['gamma'], probability=True)
    model.fit(train_x, train_y)
    return model

def read_data(data_file):
    import gzip
    f = gzip.open(data_file, "rb")
    train, val, test = pickle.load(f, encoding='latin1')
    f.close()
    train_x = train[0]
    train_y = train[1]
    test_x = test[0]
    test_y = test[1]
    return train_x, train_y, test_x, test_y

if __name__ == '__main__':
    data_file = "Datas/mnist.pkl.gz"
    thresh = 0.5
    model_save_file = None
    model_save = {}
    test_classifiers = ['NB', 'KNN', 'LR', 'RF', 'DT', 'SVM', 'GBDT']
    classifiers = {'NB':naive_bayes_classifier,
        'KNN':knn_classifier,
        'LR':logistic_regression_classifier,
        'RF':random_forest_classifier,
        'DT':decision_tree_classifier,
        'SVM':svm_classifier,
        'SVMCV':svm_cross_validation,
        'GBDT':gradient_boosting_classifier
    }
    print('读取训练数据和测试数据...')
    train_x, train_y, test_x, test_y = read_data(data_file)
    num_train, num_feat = train_x.shape
    num_test, num_feat = test_x.shape
    is_binary_class = (len(np.unique(train_y)) == 2)
    print('******************** Data Info *********************')
    print('训练数据: %d, 测试数据: %d, 特征数量: %d' % (num_train, num_test, num_feat))

    for classifier in test_classifiers:
        print('******************* %s ********************' % classifier)
        start_time = time.time()
        model = classifiers[classifier](train_x, train_y)
        print('训练耗时 %fs!' % (time.time() - start_time))
        predict = model.predict(test_x)
        if model_save_file != None:
            model_save[classifier] = model
        if True:
            # precision = metrics.precision_score(test_y, predict)
            # recall = metrics.recall_score(test_y, predict)
            # print('precision: %.2f%%, recall: %.2f%%' % (100 * precision, 100 * recall))
            accuracy = metrics.accuracy_score(test_y, predict)
            print('准确度: %.2f%%' % (100 * accuracy))
        if model_save_file != None:
            pickle.dump(model_save, open(model_save_file, 'wb'))


#******************* NB ********************
#training took 0.287000s!
#accuracy: 83.69%
#******************* KNN ********************
#training took 31.991000s!
#accuracy: 96.64%
#******************* LR ********************
#training took 101.282000s!
#accuracy: 91.99%
#******************* RF ********************
#raining took 5.442000s!
#accuracy: 93.78%
#******************* DT ********************
#training took 28.326000s!
#accuracy: 87.23%
#******************* SVM ********************
#training took 3152.369000s!
#accuracy: 94.35%
#******************* GBDT ********************
#training took 7623.761000s!
#accuracy: 96.18%
