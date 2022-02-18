'''Given an array of integers A, every element appears twice except for one. Find that single one.'''
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
		res=A[0]
		for i in range(1,len(A)):
			res=res^A[i]
		return res
