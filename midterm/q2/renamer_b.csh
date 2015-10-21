#!/bin/tcsh 

foreach file (*.txt)
    mv $file $file.old
end
