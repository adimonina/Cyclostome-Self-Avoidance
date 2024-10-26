library(Rsamtools)


args <- commandArgs(trailingOnly = TRUE)

# Check if the BAM file path is provided
if (length(args) == 0) {
  stop("No BAM file path provided. Usage: Rscript sam_to_CSV.R /path/to/file.bam")
}

bamFile <- args[1]

#read in entire BAM file
bam <- scanBam(bamFile)


#function for collapsing the list of lists into a single list
#as per the Rsamtools vignette
.unlist <- function (x){
  x1 <- x[[1L]]
  if (is.factor(x1)){
    structure(unlist(x), class = "factor", levels = levels(x1))
  } else {
    do.call(c, x)
  }
}

#store names of BAM fields
bam_field <- names(bam[[1]])

#go through each BAM field and unlist
list <- lapply(bam_field, function(y) .unlist(lapply(bam, "[[", y)))

#store as data frame
bam_df <- do.call("DataFrame", list)
names(bam_df) <- bam_field

write.csv(bam_df[c("rname", "pos" , "qwidth")],"data.csv", row.names=FALSE)
