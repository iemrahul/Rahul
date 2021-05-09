def reverse(l1):
    l1_t =0
    while (l1 > 0):
        a = l1 % 10
        l1_t = l1_t * 10 + a
        l1 = l1 // 10
    return l1_t


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.val)


#import re
l1 = input()

# l1 = re.split(',',l1)
# l2 = input()
# l2 = re.split(',',l2)
# l1[0] = l1[0][1]
# l1[-1] = l1[-1][0]
# l1 =int("".join(l1))
# l2[0] = l2[0][1]
# l2[-1] = l2[-1][0]
# l2 =int("".join(l2))
# l1=reverse(l1)
# l2=reverse(l2)
# l3=str(reverse(l1+l2))
# temp =['[']
# for i in range(len(l3)):
#     if i == len(l3)-1:
#         temp.append(l3[i])
#         temp.append(']')
#         continue
#     temp.append(l3[i])
#     temp.append(',')
# print(''.join(temp))

