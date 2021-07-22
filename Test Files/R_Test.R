distribution = read.csv('Test_Distribution.txt', header = FALSE)
distribution
library(dplyr)
distribution <- rename(distribution, 'Names' = 'V1')
distribution <- rename(distribution, 'Top 10' = 'V2')
distribution <- rename(distribution, 'Top 25' = 'V3')
distribution <- rename(distribution, 'Top 50' = 'V4')
distribution <- rename(distribution, 'Top 100' = 'V5')
colnames(distribution)

library(ggplot2)
results <- ggplot(distribution) + 
  geom_bar(aes(x = `Top 10`, colour = 'red')) +
  geom_bar(aes(x = `Top 25`, colour = 'green'))
results
