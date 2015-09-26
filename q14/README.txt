The outputs for both the HTML and LATEX versions are given in this file with
appropriate names. The _all files are designed to run for any number of computers 
you want, as long as you format the command as such:

q14_all <html OR latex> <any number of computer names> > q14_all.<html or latex>

Running this script outputs two files: q14_all.html and q14_all.pdf . The .pdf
is my latex table, which the script automatically converts. 

In order to get my ssh keys working, I already had my keys made with ssh-keygen.
Then, I used ssh-add and input my passphrase to add this to my approved hosts. 
After that, my ssh commands went through to each host (hyades, praesepe, virgo, 
astronomy) without any more input.

