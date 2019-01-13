# coding = utf-8
__author__ = "Yufeng Yang"

"""
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

 

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 

"""


# Time: O(n^2)
# Space: O(n)
def pancakeSort(A):
    """
    :param A: List[int]
    :return: List[int]

    Explanation:
        Like selection sort, from end to start, we find the maximum and do corresponding flips
    """

    N = len(A)
    ans = []
    if N <= 1:
        return ans
    if N == 2:
        if A[0] > A[1]:
            ans.append(2)
        return ans

    for i in range(N - 1, 0, -1):
        max_index = i
        for j in range(i - 1, -1, -1):
            if A[j] > A[max_index]:
                max_index = j

        if max_index != i:
            A = A[:max_index + 1][::-1] + A[max_index + 1:]
            A = A[:i + 1][::-1] + A[i + 1:]
            ans.extend([max_index + 1, i + 1])

    return ans


# Recursive solution
def pancakeSort2(A):
    """
    :param A: List[int]
    :return: List[int]
    """

    N = len(A)
    ans = []
    if N <= 1:
        return ans
    if N == 2:
        if A[0] > A[1]:
            ans.append(2)
        return ans

    max_index = N - 1
    for i in range(0, N - 1):
        if A[max_index] < A[i]:
            max_index = i

    A = A[:max_index + 1][::-1] + A[max_index + 1:]
    A.reverse()
    return [max_index + 1, N] + pancakeSort2(A[:N-1])


if __name__ == "__main__":
    t1 = [3, 2, 4, 1]
    print(pancakeSort(t1))
    print(pancakeSort2(t1))