#include <stdio.h>
#include <string.h>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    int p[26];
    for(int i = 0; i < 26; i++) scanf(" %d", &p[i]);
    char s1[2000];
    char s2[2000];
    scanf(" %s", s1);
    scanf(" %s", s2);
    static int memo[2001][2001];
    memset(memo, 0, (n + 1) * (m + 1) * sizeof(int));
    for(int i = 1; i < (n + 1); i++){
        for(int j = 1; j < (m + 1); j++){
            if(s1[i - 1] == s2[j - 1]){
                memo[i][j] = memo[i - 1][j - 1] + p[s1[i - 1] - 97];
            }
            else{
                memo[i][j] = (memo[i][j - 1] > memo[i - 1][j]) ? memo[i][j - 1] : memo[i - 1][j];
            }
        }
    }
    printf("%d\n", memo[n][m]);
    return 0;
}