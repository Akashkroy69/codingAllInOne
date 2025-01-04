#include<stdio.h>
int main()
{
    int i,n;
    printf("the original array");
    int arr[7]={1,2,3,4,5,6,7};
    int size=sizeof(arr)/sizeof(arr[0]);
    for(i=0;i<size;i++)
    {
        printf(" %d ",arr[i]);
    }
    
    
   // printf("%d",noofelements);//
   printf("\nafter reversal: \n");
  int firstindex=0;
  int lastindex=size;
  int temp;
  while(firstindex<lastindex)
{
    //   
          temp=arr[firstindex];
          arr[lastindex]=arr[firstindex];
          arr[lastindex]=temp;
          firstindex++;
          lastindex--;      
  }
  for(i=0;i<size;i++)
  {
      printf(" %d ",arr[i]);
  }
}