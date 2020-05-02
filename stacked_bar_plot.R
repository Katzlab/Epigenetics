# This script creates a stacked bar plot with colors and legend and was used to make figure 3 of the epigenetics paper; 
# This script requires a table as txt file as input
# read a table
k1 = read.table('/Users/katzlab_agnes/Desktop/bar_plot.txt',header = TRUE)

# put table into matrix
k2 <- as.matrix(k1)


par(las=2) # make label text perpendicular to axis
par(mar=c(5,10,10,6)) # increase y-axis margin


barplot(k2, #main="Conservation by function", 
        horiz=TRUE, col=c("black", "gray40", "white", "white"),
        legend = rownames(k2), ylim = c(0,20), cex.names=0.8)

