## Kaggle's Titanic Competition

From [Kaggle website](https://www.kaggle.com/c/titanic):

> This is the legendary Titanic ML competition – the best, first challenge for you to dive into ML competitions and familiarize yourself with how the Kaggle platform works.
> 
>The competition is simple: use machine learning to create a model that predicts which passengers survived the Titanic shipwreck.

### Goal
Given a *train.csv* file, fit a model that maximizes prediction accuracy over a *test.csv* unlabeled dataset

### Phase 1: Data Loading & Feature Engineering
In the first phase, we concentrate on analyze the dataset to understand when provided data is good enough to be processed. The very first step after loading csv is to look at missing values

	> Train Dataset - Counting missing values over 891 examples
    Pclass        0
    Name          0
    Sex           0
    Age         177
    SibSp         0
    Parch         0
    Ticket        0
    Fare          0
    Cabin       687
    Embarked      2
	dtype: int64
	> Ground Truth - Are there missing values?
	no
	> Test Dataset - Counting missing values over 418 examples
	PassengerId      0
	Pclass           0
	Name             0
	Sex              0
	Age             86
	SibSp            0
	Parch            0
	Ticket           0
	Fare             1
	Cabin          327
	Embarked         0

Turns out that:
* A significant amount of examples in the training set has missing values. We don't want to get rid of these rows
* Both Train and Test dataset have few values of "Cabin" variable. This is a good point to decide to remove this feature
* We have an outcome for each example. This makes me very happy :blush:
* In training dataset, ~10% of samples have missing "Age" value. Furthermore, looking at distribution (see docs/Figure_1.png) and sample dispersion, turns out that it's not appropriate to replace so many values with mean/median

In this step, I won't pick Age as feature, but I'll come back on it later and here is why: When a ship sinks, I suppose that everyone will put a big effort to save children. Old people have less probability to survive. Thus, if I'm right, age will carry significant knowledge

### Phase 2: Exploratory Analysis

The first question I need to answer is: "How many people survived? Who are the the survivors/dead?"

    > Survivors and Dead count
    Survived= 38.0% , Dead=62.0% (sum is 100.0) Out of 891 examples

There are more dead than survivors. I'll investigate on dead people data to understand why they are dead

The first assumption that I'll take a very sad assumption: poor people are more likely to die. Let's check it out using passenger class