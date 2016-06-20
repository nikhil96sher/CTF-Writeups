keys = [1,2,3,4,5,6,7,8,9,0,'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

decode = ['2933070^67','3232427352382723^3475','33^8923','1752173996578580830630^3617','47^1205','1334324742249840763104115177915406053196992583180688299430^5620']

key = 11266
for crypted in decode:
	quotient = int(crypted.split('^')[0],10)
	remainder = int(crypted.split('^')[1],10)
	value = quotient*key + remainder
	s = []
	ans = {}
	j = 0
	while j<62:
		ct = 0
		while(value%primes[j] == 0):
			value/=primes[j]
			ct+=1
		if(ct!=0):
			s.append(ct)
			ans[ct] = keys[j]
		j+=1
	res = ""
	for j in ans:
		res = res + str(ans[j])
	print res