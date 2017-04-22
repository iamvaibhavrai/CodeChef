#include <stdio.h>
#include <conio.h>

int main() {
	int t;
	scanf("%d",&t);
	float q,p,expense;
	while(t--) {
		scanf("%f%f",&q,&p);
		expense = q*p;
		if (q>1000) {
			expense -= expense/10;
		}
		printf("%.6f",expense);
		printf("\n");
	}
	return 0;
}