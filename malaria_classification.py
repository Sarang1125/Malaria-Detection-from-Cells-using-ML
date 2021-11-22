import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
import joblib
import matplotlib.pyplot as plt
from matplotlib import style

##print(" Loading Dataset")
##Step1: Loading the Dataset 

dataframe = pd.read_csv("csv/dataset.csv")
print(dataframe.head())

#Step2: Splitting the Dataset into training and test data.
x = dataframe.drop(["Label"],axis=1)
y = dataframe["Label"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)


##Step4: Building a model using random forrest classifier
model = RandomForestClassifier(n_estimators=100,max_depth=5)
model.fit(x_train,y_train)
joblib.dump(model,"rf_malaria_100_5")



##Step5: Make predictions and get the classification report
##		 The output will be a floating result which will be the efficiency or the accuracy.

predictions = model.predict(x_test)

print(metrics.classification_report(predictions,y_test))
print(model.score(x_test,y_test))
regression_line = [ (m*x)+b for x in xs]

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()













