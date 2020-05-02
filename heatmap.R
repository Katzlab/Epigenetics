#### This script creates a presence/absence matrix with two colors, based on an input table as txt file 
library(ggplot2)
library(gplots)
library(reshape2)
library(plyr)
library(dplyr)
library(RColorBrewer)

# read a table
k1 = read.table('/Users/katzlab_agnes/Desktop/smart_species.txt',header = TRUE)

# put table into matrix
k2 <- as.matrix(k1)

# make the heatmap using k2
heatmap.2(k2, dendrogram='none', Rowv=FALSE, 
          Colv=FALSE, 
          col=c("#FFFFFF","#542788"),trace = "none", key = FALSE, lhei=c(0.1, 10), lwid=c(0.1,10))