def fun(s):
	arr = []
	n = len(s)
	dn = 0  # distinct length
	aux = 0
	left=0
	right=0
	flag=0
	res = n
	for i in range(26):
		arr.append(0)
	for i in range(n):
		arr[ord(s[i])-97]+=1
	for i in range(26):
		if arr[i]>0:
			dn+=1
	for i in range(26):
		arr[i] = 0		
	
	while(1):
		while(aux!=dn):
			if(right==n):
				flag=1
				break
			if(arr[ord(s[right])-97]==0):
				aux+=1
			arr[ord(s[right])-97]+=1
			right+=1
		if flag==1:
			break	
		#print(right,left)
		while(left<right):
			arr[ord(s[left])-97]-=1
			if(arr[ord(s[left])-97]==0):
				if(right-left<res):
					res = right - left	
				break
			left+=1
		
		aux-=1	
		left+=1	
	print(res)



		
			


fun("hellolhe");

