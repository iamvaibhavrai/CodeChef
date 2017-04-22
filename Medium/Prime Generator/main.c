#include <stdio.h>
#include <math.h>
 
int main() {
	int t,i,x,y;
	scanf("%d",&t);
	while(t--) {
		scanf("%d %d",&x,&y);
		if(x<3) {
			printf("2\n");
			x = 3;
		}
		if(x % 2 == 0)
			x++;
		for(i=x; i<=y; i+=2) {
			float z;
			z = floor(sqrt(i));
			int j,flag = 1;
			for(j=3; j<=z; j+=2) {
				if(i%j == 0) {
					flag = 0;
					break;
				}
			}
			if(flag)
				printf("%d\n",i);
		}
	}
	return 0;
}