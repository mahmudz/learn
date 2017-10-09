#include<stdio.h>

int main()
{
    int ano,mes,dia, N;

    N = 30;

    ano = N / 365;
    mes = N % 365 / 30;
    dia = N % 365 % 30;

    printf("%d ano(s)\n",ano);
    printf("%d mes(es)\n",mes);
    printf("%d dia(s)\n",dia);

    return 0;




}