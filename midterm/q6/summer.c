#include <stdio.h>

int main()
{
  int total = 0, i = 1, max = 1000;
  
  while (i <= max)
    {
      total += i;
      i += 1;
    }
  
  printf("Total Sum from 1 to 1000: %d\n",total);

  printf("Or, lets cheat with N(N+1)/2\n");

  total = 0;
  total = max * (max + 1) / 2;
  printf("Total Sum from 1 to 1000 using formula: %d\n",total);
}
