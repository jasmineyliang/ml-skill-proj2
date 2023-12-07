# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1heVNfkBMzDcsUZSK7IojEW4BVA7zj3iw
"""

import sklearn
import sklearn.svm

def svm_with_diff_c(train_label, train_data, test_label, test_data):
  c=[0.01,0.1,1,2,3,5]
  scorelist=[]
  no_support = []
  for i in range(len(c)):
    linear_svc = sklearn.svm.SVC(C = c[i])
    linear_svc.fit(train_data, train_label, sample_weight=None)
    score = linear_svc.score(test_data, test_label, sample_weight=None)
    support = linear_svc.n_support_
    scorelist.append(score)
    no_support.append(support)
  scorelist = np.array(scorelist)
  no_support = np.array(no_support)
  print(scorelist)
  print(no_support)

def svm_with_diff_kernel(train_label, train_data, test_label, test_data):
  k = ['linear','poly', 'rbf', 'sigmoid']
  scorelist =[]
  no_support = []
  for i in range (len(k)):
    linear_svc = sklearn.svm.SVC(kernel = k[i])
    linear_svc.fit(train_data, train_label, sample_weight=None)
    score = linear_svc.score(test_data, test_label, sample_weight=None)
    support = linear_svc.n_support_
    scorelist.append(score)
    no_support.append(support)
  
  scorelist = np.array(scorelist)
  no_support = np.array(no_support)

  print(scorelist)
  print(no_support)