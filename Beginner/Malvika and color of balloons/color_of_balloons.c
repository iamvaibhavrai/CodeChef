#include<stdio.h>
#include<conio.h>

int main() {
  int t;
  scanf("%d",&t);
  while(t--){
    char *s;
    scanf("%s",&s);
    int i,amber=0,brass=0;
    for (i = 0; i < strlen(s); i++) {
      if(s[i] == 'a') amber++;
      else brass++;
    }
    if(amber<brass) printf("%d\n",amber);
    else printf("%d\n",brass);
  }
  return 0;
}
