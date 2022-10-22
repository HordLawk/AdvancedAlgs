#include <stdio.h>
#include <string.h>
#include <stdarg.h>

char str1[2000];
char str2[2000];
static int memo[2000][2000];

int min(int num, ...){
    va_list valist;
    va_start(valist, num);
    int minimum = va_arg(valist, int);
    for(int i = 1; i < num; i++){
        int n = va_arg(valist, int);
        if(n < minimum) minimum = n;
    }
    va_end(valist);
    return minimum;
}

int edit(int n, int m){
    if(!n) return m;
    if(!m) return n;
    if(memo[n - 1][m - 1] == -1){
        memo[n - 1][m - 1] = (
            (str1[n - 1] == str2[m - 1])
            ? edit(n - 1, m - 1)
            : (1 + min(3, edit(n, m - 1), edit(n - 1, m), edit(n - 1, m - 1)))
        );
    }
    return memo[n - 1][m - 1];
}

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        scanf(" %s", str1);
        scanf(" %s", str2);
        memset(memo, -1, 2000 * 2000 * sizeof(int));
        printf("%d\n", edit(strlen(str1), strlen(str2)));
    }
    return 0;
}