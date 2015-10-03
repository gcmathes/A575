FUNCTION FAC(i) RESULT (number)

INTEGER(kind=8) :: i, RFAC, number
number = RFAC(i)

END

!So in order to get a recursive function, I found that I needed a function
!to call my function, then define one specifically for recursion.

RECURSIVE FUNCTION RFAC(j) RESULT (nresult)
INTEGER :: j
INTEGER(kind=8) :: nresult, inc, fact
!In order to store the large integers from factorials, I need to define my
!integers with extra space.

IF (j > 0) THEN
   inc = RFAC(j-1)
   fact = j * inc !nresult is being returned every time I run the function,
   nresult = fact !which will continue to decrement j until it reaches 0. 
ELSE
   nresult = 1 !This function, in tandem with FAC, will return the factorial
END IF         !of whatever you put in it. 

END 

!After defining my functions, I start the main program here.

PROGRAM MAIN

IMPLICIT NONE

!The limits and starting variable are easily changeable here.
INTEGER :: n = 1, limit1 = 100, limit2 = 20

INTEGER :: count = 0
INTEGER(kind=8) :: FAC
INTEGER(kind=8) :: fact = 0, total = 0, temp = 0
!Once again, I give more space for my long factorial variables.


PRINT *, "Starting n value : ",n

DO WHILE (n < limit1)
IF (n < limit2) THEN
temp = FAC(n)
total = total + temp  !As long as n is less than the limit2 set above, it
END IF           !will loop through the factorial function and add it to
                 !the total to be output at the end of the program.

n = n * (2) + 1  !After that, double n and add one to it.
count = count + 1

print *, "This loop has run : ",count," times"
print *, "Next value of n : ",n

IF (n > limit1) THEN
print *, "Limit of n has been reached, ending loop"
END IF
!If n is passing the limit, I output a warning to the user. 
ENDDO

print *, "The sum of the factorials is : ", total
!Finally, I output the resulting factorial sum and end the program.
END
