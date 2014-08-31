library("e1071")

dataSpliter <- function(dset) {
    ids <- c('train', 'test')
    out <- split(dset, sample(rep(ids, nrow(dset)/2)))
    return(out)
}

seaflow <- read.csv(file='seaflow_21min.csv', head=TRUE, sep=',')
summary(seaflow)
## Removing the data coming from the file id 208.
seaflowFix <- subset(seaflow, file_id != 208)
groups <- dataSpliter(seaflowFix)
## Creating a new SVM model.
seaflowFol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
svmmodel <- svm(seaflowFol, data=groups$'train')
## Accuracy on the training dataset.
trainPred <- predict(svmmodel, groups$'train', type="class")
trainAcc <- sum(trainPred == groups$'train'$pop) / length(trainPred)
print(c("Accuracy of SVM on the training dataset", trainAcc))
## Accuracy on the test dataset.
testPred <- predict(svmmodel, groups$'test', type="class")
testAcc <- sum(testPred == groups$'test'$pop) / length(testPred)
print(c("Accuracy of SVM on the test dataset", testAcc))
