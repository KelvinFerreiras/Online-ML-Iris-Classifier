# Online ML Iris Classifier

https://iris-classifier.000webhostapp.com/

##Description

This webapp classifies Iris plants into subtypes using a decision tree trained with IBM Watson Machine Learning. 

Requests are sent through a HTTP Web Action to a python Cloud Function (Apache OpenWisk), which processes the inputs, obtain a output class using a live IBM Watson Machine Learning model and retuns the results in JSON format.

The ML model was trained using both discrete and numerical data from R.A Fisher's Iris Plants Database. The model takes infomation of the size of the plant's sepals and petals as input. Then, it returns a string with the class of the plant.

##Discrete Input Format

Four possible values:
	S for small
	MS for medium small
	ML for medium large
	L for large

##Numerical Input Format

Numerical values in decimal(float/double) format
	Ex:
		3.5
		3.0
		3

##Output

Possible string values
	Iris-setosa
	Iris-versicolor
	Iris-virginica

##Link

https://iris-classifier.000webhostapp.com/


