#!/bin/tcsh 

foreach file (*.txt)
    mv $file $file:r.dat
end
