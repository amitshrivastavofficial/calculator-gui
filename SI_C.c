// C Program To Calculate Simple Interest 
#include <stdio.h>
int main(){
    float principal, time, rate, SI;
    
    // Asking for Input
    printf("Enter the principal amount: ");
    scanf("%f", &principal);
    printf("Enter the time period: ");
    scanf("%f", &time);
    printf("Enter the rate of interest: ");
    scanf("%f", &rate);
    
    SI = (principal * time * rate) / 100;
    printf("Simple Interest for Principal Amount %.2f is %.2f", principal, SI);
    return 0;
}
