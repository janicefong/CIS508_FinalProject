<h2>CIS508 Machine Learning in Business Final Project </h2>

<b>Problem Definition: </b> An increasing number of account holders have been failing to meet their minimum payment requirements, leading to a rise in defaults. <br/>
<b>Goal:</b> Construct a predictive model to accurately forecast the likelihood of an account defaulting in the next month.  <br/>
<b>Data: </b>https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients

<b>Supervised Model used:</b> Decision Tree, Logistic Regression, Random Forest, AdaBoost Classifier,Gradient Booster, BaggingClassifier

<b>Presentation slides:</b> https://github.com/janicefong/CIS508_FinalProject/blob/main/Team%202%20-%20Final%20Presentation.pptx

<h3>Installation</h3>
1. Download app.py from file <br/>
2. Run this code in terminal !streamlit run app.py

<h3>Result</h3>
![image](https://github.com/user-attachments/assets/3082c203-36af-410d-b512-ab91f9da73cf)

We choose Random Forest model as our best bet because it has a highest recall and F1-score compare to the rest. <br/>
The reason why we are looking at the recall and F-1 score is due to imbalance data.
