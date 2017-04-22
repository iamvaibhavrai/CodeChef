#include <stdio.h>
#include <conio.h>

int main() {
	int test_cases,no_of_expenditures,salary,expenditure;
	scanf("%d",&test_cases);
	while(test_cases--) {
		int sum = 0;
		scanf("%d%d",&no_of_expenditures,&salary);
		while(no_of_expenditures--) {
			scanf("%d",expenditure);
			sum += expenditure;
		}
		printf("%d", sum);
	}
	return 0;
}