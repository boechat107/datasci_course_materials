library("ggplot2")
library("rpart")
library("randomForest")
library("e1071")

seaflow <- read.csv(file='seaflow_21min.csv', head=TRUE, sep=',')
summary(seaflow)
## Now a complicated command to split randomly samples from seaflow to form 2 groups.
## 'rep' repeats a sequence for N times
## 'sample' takes one element of a sequence at a time, sampling randomly, until the
## sequence is over. The result is another sequence.
## 'split' splits data into groups. The group assignment is given by a sequence of
## group identifier, one for each sample of the sequence.
ids <- c('train', 'test')
groups <- split(seaflow, sample(rep(ids, nrow(seaflow)/2))) 
## Plotting data to answer question 3.
qplot(seaflow$pe, seaflow$chl_small, color=seaflow$pop, geom="point")
## Simplest classification tree model.
seaflowFol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
ctmodel <- rpart(seaflowFol, method="class", data=groups$'train')
## Plot the tree representation.
plot(ctmodel)
text(ctmodel)
## Accuracy on the training dataset.
trainPred <- predict(ctmodel, groups$'train', type="class")
trainAcc <- sum(trainPred == groups$'train'$pop) / length(trainPred)
print(c("Accuracy on the training dataset", trainAcc))
## Accuracy on the test dataset.
testPred <- predict(ctmodel, groups$'test', type="class")
testAcc <- sum(testPred == groups$'test'$pop) / length(testPred)
print(c("Accuracy on the test dataset", testAcc))
## Confusion matrix.
print("Confusion matrix for the simple tree")
table(pred = testPred, true = groups$'test'$pop)
##
## Random Forest
##
rfmodel <- randomForest(seaflowFol, data=groups$'train')
## Accuracy on the training dataset.
trainPred <- predict(rfmodel, groups$'train', type="class")
trainAcc <- sum(trainPred == groups$'train'$pop) / length(trainPred)
print(c("Accuracy of random forest on the training dataset", trainAcc))
## Accuracy on the test dataset.
testPred <- predict(rfmodel, groups$'test', type="class")
testAcc <- sum(testPred == groups$'test'$pop) / length(testPred)
print(c("Accuracy of random forest on the test dataset", testAcc))
## Confusion matrix.
print("Confusion matrix for Random Forest")
table(pred = testPred, true = groups$'test'$pop)
## Variable importance.
importance(rfmodel)
###
### SVM model
###
svmmodel <- svm(seaflowFol, data=groups$'train')
## Accuracy on the training dataset.
trainPred <- predict(svmmodel, groups$'train', type="class")
trainAcc <- sum(trainPred == groups$'train'$pop) / length(trainPred)
print(c("Accuracy of SVM on the training dataset", trainAcc))
## Accuracy on the test dataset.
testPred <- predict(svmmodel, groups$'test', type="class")
testAcc <- sum(testPred == groups$'test'$pop) / length(testPred)
print(c("Accuracy of SVM on the test dataset", testAcc))
## Confusion matrix.
print("Confusion matrix for SVM")
table(pred = testPred, true = groups$'test'$pop)
