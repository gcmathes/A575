#!/bin/tcsh 

foreach file (*$1)
    mv $file $file.old
end
