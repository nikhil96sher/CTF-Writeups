# Mr. Robot

## Problem Statement:

```
Disallow it
```

The name of the challenge made it clear that we had to look for the robots.txt file of the website

Going to `https://ctf.ekoparty.org/robots.txt`:


Result was:

```
User-agent: *
Disallow: /static/wIMti7Z27b.txt
```

Opening the file: `https://ctf.ekoparty.org/static/wIMti7Z27b.txt` gave the flag: `EKO{robot_is_following_us}`