#include <iostream>
using namespace std;

int main() {
    int T, n,i,j,k,counter;
    unsigned long time;
	cin>>T;
	unsigned long *A,*B;
	for(k=0;k<T;k++) {
        counter = 0;
        cin>>n;
        A=new unsigned long[n];
        B=new unsigned long[n];
        for(i=0;i<n;i++)
            cin>>A[i];
        for(i=0;i<n;i++)
            cin>>B[i];
        for(j=0;j<n;j++) {
            if(j==0)
                time=A[j];
            else
                time=A[j]-A[j-1];
            if(time>=B[j])
                counter++;
        }
        cout<<counter<<endl;
    }
	return 0;
}
