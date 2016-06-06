## LOSSLESS (Steganography) - 100 PTS

### CHALLENGE
d4rth used his dirty methods to hide a secret in a png file. He is cleverly trying to divert your focus from challenge, but the force is strong with you. Now extract the flag from these images, my young padawan.
Created by: Arpit Singla    
http://hack.bckdr.in/LOSSLESS/original.png  
http://hack.bckdr.in/LOSSLESS/encrypted.png

### SOLUTION
* In this challenge, we are provided with two images, `original.png` and `encrypted.png`. And are supposed to find the hidden message.
* Observing the images and seeing the difference using  `compare original.png encrypted.png diff.png` reveals that both the images differ only in the top right corner.
* To enhance the clarity of the difference, we used an online Steganographic Comparator `https://futureboy.us/stegano/compinput.html` giving us an image that looks like `out.png`
* It was only a matter of seconds that we realized these may be binary strings Blue - 1 and Black - 0. Moreover, they were of 7 bits (Vertically). That further provoked the thought of them fitting in ASCII representation. (<128)
* We wrote a quick script to read the binary numbers and got the output `The flag is SHA256{-----------------------------}`.
* ![Original Image](./original.png)
* ![Encrypted Image](./encrypted.png)
* ![Amplified Difference](./out.png)