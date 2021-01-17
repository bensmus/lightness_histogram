library(reticulate)

args = commandArgs(trailingOnly = TRUE)
img = args[1]
source_python("get_lightness.py")
Lightness = get_lightness_func(img)


hist(Lightness, right = FALSE, freq = FALSE, breaks = 10) 
