#INFINITE PATHS - 100 PTS

### CHALLENGE

cr4wl3r(a basillisk) once got pissed off with feignix(fawkes the feignix) and challenged him to find the flag that was hidden in the mysterious tunnels inside his lair, the chamber of secrets. feignix now flies inside the underground tunnels attempting to find the flag. See if you(Tom) can get to the flag first with some magic tricks. Will you be able to solve this Marvelous Riddle Tom? Go [here](http://hack.bckdr.in/INFINITE-PATHS/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path/path)

### SOLUTION

* The link directs to a page having 50 directories one inside another.
* Upon using the directory traversal attack i.e., the '../' attack, the url which is of the form '..path/path/..path/../', directs us one directory above which gives us the same output, which is nothing.
* Instead of typing '..path/../', when typed '/path../' it directs us into a page which gives a part of the flag.
* Do it 50 times starting from the first directory i.e., 'http://hack.bckdr.in/INFINITE-PATHS/path../' and it will give you a string.
* SHA256 of that string is the flag.
