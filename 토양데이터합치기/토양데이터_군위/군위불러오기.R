install.packages("gdata")
library(gdata)

gunwi1 <- read.xls("gunwi1.xls")


install.packages("libxls")

library(readxl)
file = "1gunwi.xlsx"

gunwi1<- read_excel(file)
phlist<- gunwi1[33,]
phlist

View(gunwi1)


install.packages("openxlsx")
library(openxlsx)

file_path <- "/Users/Star1/Desktop/부트캠프_파이썬 _실습/Python_Practice/토양데이터합치기/토양데이터_군위/gunwi1.xlsx"

gunwi1 <- read.xlsx(file)
