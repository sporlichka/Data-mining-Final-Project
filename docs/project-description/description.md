 

Data Mining. Final Project

Project goal: Design and evaluate a complete data mining solution for a meaningful real-world problem. Students must demonstrate sound data preparation, exploration, feature work, model selection, evaluation, interpretation, and communication. The final result must be reproducible and must explain not only which model performed best, but why the result is credible and useful.

General Requirements
-	Group project: maximum 3 students.
-	Select an open-source dataset from Kaggle, UCI, government portals, or another reliable source.
-	Recommended dataset size: at least 15 features and 40,000 records. 
-	Select one main project type: classification, regression, clustering, time-series analysis, or text mining.
-	Submit the code, presentation, dataset link, and short project report.
-	Every student must explain their contribution during the defense.

Part 1 Project Proposal and Data Analysis

1.	Problem Definition
-	Describe the problem and its importance.
-	Define the project objectives.
-	Write 2–4 research questions or hypotheses.
-	Explain why the selected dataset is appropriate.

2.	Dataset Description
Include:
-	Dataset source and link
-	Number of records and features
-	Target variable, if applicable
-	Feature types
-	Missing values and class distribution

3.	Data Preprocessing
Perform and explain:
-	Duplicate removal
-	Missing-value treatment
-	Outlier analysis
-	Categorical encoding
-	Scaling or normalization
-	Variable transformation
-	Aggregation or sampling, if necessary
All preprocessing decisions must be justified.

4.	Exploratory Data Analysis
Include:
-	Summary statistics
-	Feature distributions
-	Correlation analysis
-	At least five meaningful visualizations
-	At least five important conclusions from the analysis
-	ANOVA or another statistical test when appropriate

5.	Feature Engineering
-	Create at least two new meaningful features.
-	Apply feature selection.
-	Use PCA when appropriate.
-	Explain which features were retained or removed.

Part 2 Modeling and Evaluation

Select the section that matches the project.

A.	Classification or Regression
-	Create a simple baseline model.
-	Apply at least four models.
-	Classification examples: logistic regression, KNN, decision tree, SVM, bagging, or boosting.
-	Regression examples: linear regression, KNN regressor, decision tree regressor, SVR, or ensemble regression.
-	Address class imbalance when necessary.

B.	Clustering
-	Apply K-means or K-means++.
-	Determine an appropriate number of clusters.
-	Compare K-means with at least one other clustering method.
-	Use suitable measures such as silhouette score, inertia, Davies–Bouldin score, or Calinski–Harabasz score.
-	Describe and interpret the final clusters.

C.	Time-Series Analysis
-	Explore trend and seasonality.
-	Create lag or rolling features.
-	Use chronological splitting.
-	Create a baseline forecast.
-	Compare at least three forecasting models.

D.	Text Mining and NLP
-	Clean and preprocess the text.
-	Use Bag-of-Words or TF-IDF.
-	Apply cosine similarity when appropriate.
-	Compare at least three classification or clustering models.
-	Analyze incorrectly classified or poorly grouped texts.

6.	Model Evaluation
-	Use train-validation-test split or cross-validation.
-	Tune important hyperparameters.
-	Compare all models using suitable metrics.
-	Check for overfitting.
-	Select and justify the final model.
-	Use the test set only for final evaluation.

7.	Possible metrics include:
-	Classification: precision, recall, F1-score, ROC-AUC, PR-AUC, and confusion matrix
-	Regression: MAE, RMSE, and R²
-	Clustering: silhouette score, inertia, Davies–Bouldin score
-	Time series: MAE, RMSE, and MAPE when appropriate

8.	Results and Conclusions
-	Present the final model and its results.
-	Interpret the most important features or clusters.
-	Discuss successful and incorrect predictions.
-	Answer the research questions.
-	Describe project limitations.
-	Suggest at least three future improvements.

9.	Final Deliverables
-	Presentation: 10–15 slides
-	Project report: approximately 5–8 pages
-	Jupyter Notebook or Python scripts
-	Dataset link
-	README: project title, team, problem, dataset link, setup instructions, file structure, and exact run order.
-	Team contribution statement
