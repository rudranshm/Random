#include<stdio.h>
#include"coeffs.h"
int main(){
    char* str="uni.dat";
    double m=mean(str);
    double v=var(str);
    printf("The mean is %lf aand the variance is %lf",m,v);
    //The mean is 0.500031 aand the variance is 0.083247
}