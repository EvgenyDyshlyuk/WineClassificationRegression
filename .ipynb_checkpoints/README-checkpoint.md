# This is a personal ML project for Wine Dataset
### (comparison of wine quality: (int) 3 to 8 on 1600 examples using 12 measured features)
### This task is a ranking task. and can be solved for this dataset as a Classification or/and Regression task

## The solution is provided in three notebooks:
## 1. EDA:
  - Data loaded
  - Feature distributions shown
  - Train-test set split understood
  - Data saved for next step

## 2. Classification:
  - Data loaded
  ### HPO
  - Quick visualization of the performance of different classifiers on the dataset using just two features shown
  - Accuracy of 10 classifiers compared before hyperparameter optimization (HPO)
  - HPO conducted using SKOPT Bayes search (random_forest optimizer) for each of the classifiers
  Stratified 5-fold cross-validation used during this step
  - Accuracy of 10 classifiers compared after HPO
  ### Ensemble
  - First level models predictions for train set: train-meta obtained using Kfold CV
  - First level models predictions obtained for test set after using all train data for train: test-meta
  - Second level models predictions obtained for test set using train-meta for second level model HPO:
      RandomForest (shallow) after optimization of HPO using train-meta with the same KFOLD CV (making sure seed is the same as when obtaining train-meta)
   
  ## 3. Regression:
- Same procedure (as in Classification above), with the exception that:
  simple LinearRegression was used as a second level model (no HPO for second level)

### Comments:
- The "output" folder is added to .gitignore because some of the results of the HPO are more than 100 MB, exceeding GitHub limits
- The "output" folder has 4 subfolders: models, data, predictions, submissions