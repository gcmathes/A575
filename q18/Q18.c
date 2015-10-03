#include <stdio.h> //Standard namespace library

//I made my function a long because it needs the digits to hold the 
//large factorial numbers.
long fac(int i)
{
  long inc=0, fact=0; //I define some local variables that are only needed 
  if (i > 0)      //within my function.
    {
      inc = fac(i-1);
      fact = i * inc; //The function calls itself until the input reaches 0.
      return(fact);   //Once at 0, the function returns one and begins 
    }             //multiplying by each integer in increments of one until
  else            //it reaches the original value. For example, fac(4) will
    {             //perform 1 * 2 * 3 * 4, then return this value to main.
      return 1;
    }
}

int main()
{
  //Declaring variables where my limits and initial conditions are separated
  //for easy changing if needed.
  int n = 1, limit1 = 100, limit2 = 20;


  int count = 0;                     
  //These variables, like my fac(n) function, are going to be large, so I
  //set them as long types to hold all my information. 
  long fact = 0, total = 0, temp = 0;

  printf("Starting n value : %i\n", n);

  //I begin the loop that executes until n increases above a set limit.
  while (n < limit1)
    {
      //If n is less than another limit, I execute my factorial function
      //and add the result to my total, which is output at the end.
      if (n < limit2)
	{
	  temp = fac(n);
	  total += temp;
	}
      //After checking for the factorial, I double n and add one. The count
      //variable is used to track the number of executions for this loop.
      n = (n * 2) + 1;
      count += 1;
      printf("This loop has run : %i times\n", count);
      printf("Next value of n : %i\n", n);

      //I put this statement in to alert the user at what n value the loop ends.
      if (n > limit1)
	{
	  printf("Limit of n has been reached, ending loop\n");
	}
    }
  printf("The sum of the factorials is : %ld\n", total);
}

