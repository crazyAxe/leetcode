# leetcode
leetcode algorithms problem  

problem:
1.findKminsNumber.py
  desc: find k min numbers in an inordered list.
  time complexisy: nlogk

2.findMedianSortedArrays.py
  #4
  desc: There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
  The overall run time complexity  should be O(log (m+n)).
  time complexisy: O(log(m+n))
  space complexisy : O(m+n)

3.findAnumberOverHalf.py
  desc: find whether it has a number which exists over N/2 times. return the number or None.
  method: when the 2 digits is no tequal, 'delete' them all. the last one may be the candidate.
  time complexity : O(n)
  space complexity: O(1)

4.findNways.py
  desc: there is 15 steps, Tom can reach step over 3 steps at most in one pace. how many ways can he reach the 15 steps?
  method : Dynamic programming. f(n) = f(n-1) + f(n-2) + f(n-3)
  time complexisy : ?

5.LongestPalindromicSubstring.py
  #5
  time complexisy : O(n^2)

6.zigzagCoversion.py
  #6
  time complexity: O(nm)   or  O(n)? -- only visit each item once.
  space complexity: O(n)