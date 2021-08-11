rm(list=ls())
install.packages("pracma")

#Andres Giraldo
#Camilo Garcia
#David Ramirez

library(pracma)
options(digits = 15)

f1<- function(x) { 1/(1-x) }
taylor_f1<- taylor(f1,0,5)

x1<- seq(-1.0, 1.0, length.out = 50)
x1
y1<- f1(x1)
y1

yr_taylor<- polyval(taylor_f1, x1)
yr_taylor
plot(x1, y1, type = "l", 
     main = "1/(1-x) Taylor",
     col = "lightblue", lwd = 1)
par(new=TRUE)
plot(x1, yr_taylor, type = "l",
     main = '1/(1-x) Taylor', 
     col = "red", lwd = 2)