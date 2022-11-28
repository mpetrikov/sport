1 2 3 4 5 6 7 8 9
20 30 40 50

k = 6

i=len(A)//2 # 4
j=k-i # 2

if A[i]>B[j]:
            #Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i],B[j:],i)
        else:
            return self.findKth(A[i:],B[:j],j)
