#We have 62 detectors, each 2048 x 4096 pixels. Each pixel will store one 2-byte 
#integer. We have 500 images. So, simply done:

numdec = 62.
pix_x = 2048.
pix_y = 4096.
size = 2.
images = 500.

total = numdec * pix_x * pix_y * 2 * 500

print total
'''
This outputs 5.20093696e+11 bytes, which is 520 GB of data. 
There is no way we would get this into memory alone, and would require the
use of a lot of swap space.

On my desktop, without using the kochab-data partition, I couldn't fit this 
either. Using df -h, I only have about 116 GB of disk space in my /dev/sda 
partitions. I could, however, put it in my data partition which has 790 GB 
of space. 

However, Hyades has 19 TB of space to spare, so I could definitely store this data
on that cluster. 
'''
