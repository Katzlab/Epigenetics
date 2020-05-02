# This script combines two dataframes. The epigenetic dataframe is a unique file (csv) while for the conserved dataframe there are 100 repetitions. 
# The result is 100 files containing epigenetic and conserved dataframes combined for each of the 100 repetitions of the dataframe conserved. 

epigenetic <- read.table("epi_paralogs.csv", header=F, sep=",")
colnames(epigenetic) <- c("StrEpi", "AlvEpi", "RhiEpi", "PlEpi", "EEEpi", "ExEpi", "AmEpi", "OpEpi")

for(i in 1:100){
	input = paste0("./sampleMatrices/", i, ".csv")
	conserved <- read.table(input, header=F, sep=",")
	str(conserved)
	colnames(conserved) <- c("StrCons", "AlvCons", "RhiCons", "PlCons", "EECons", "ExCons", "AmCons", "OpCons")
	mixDF <- cbind(epigenetic, conserved)
	mixDF <- mixDF[,c("StrEpi", "StrCons","AlvEpi", "AlvCons","RhiEpi", "RhiCons","PlEpi", "PlCons","EEEpi", "EECons","ExEpi", "ExCons","AmEpi", "AmCons","OpEpi", "OpCons")]
	path2out <- paste("./sampleMatrices/",i,"_mixed.csv")
	write.table(mixDF, path2out, sep=",", col.names=F, row.names=F)
	pdf(paste0("./sampleMatrices/", i, ".pdf"))
	boxplot(mixDF, names = c("StrEpi", "StrCons","AlvEpi", "AlvCons","RhiEpi", "RhiCons","PlEpi", "PlCons","EEEpi", "EECons","ExEpi", "ExCons","AmEpi", "AmCons","OpEpi", "OpCons"), col = c("grey","white","grey","white","grey","white","grey","white","grey","white","grey","white","grey","white","grey","white"), las=2)
	dev.off()
}


		

	
	


