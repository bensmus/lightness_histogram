Makes a pdf histogram that describes how often a certain pixel lightness occurs in an image. For 8 bit photos like "wheatly.jpg", the max lightness is 255. Similar histograms appear in photo editing applications.

To test the histogram on Linux you need to run 
```none
Rscript main.R wheatly.jpg
```
in a folder that has `main.R`, `get_lightness.py`, and `wheatly.jpg`. 

Note: This assumes you have both a Python and an R interpreter installed.

An Rplots.pdf file will be generated, which contains the histogram.
