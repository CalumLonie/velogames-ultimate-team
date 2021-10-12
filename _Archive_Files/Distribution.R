distribution = read.csv('Italy_Distribution.txt', header = FALSE)
colnames(distribution)
distribution <- rename(distribution, 'Names' = 'V1')
distribution <- rename(distribution, 'Top 10' = 'V2')
distribution <- rename(distribution, 'Top 25' = 'V3')
distribution <- rename(distribution, 'Top 50' = 'V4')
distribution <- rename(distribution, 'Top 100' = 'V5')
colnames(distribution)
distribution

library(ggplot2)
plot <- ggplot(data = distribution) + geom_bar(aes(y = 'Top 10'))
plot
