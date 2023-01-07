import collections
from typing import Optional, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#내풀이
class Solution:
    # 내풀이
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        if not head:
            return True

        while head is not None:
            lst.append(head.val)
            head = head.next

        if lst[::] == lst[::-1]:
            return True
        else:
            return False

    #데크를 이용한 최적화
    def isPalindrome_with_deq(self, head: Optional[ListNode]) -> bool:
        # 데크는 이중 연결리스트 구조로 양쪽 방향 모두 추출하는데 시간복잡도가 O(1)에 해당한다
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True
    def isPalindrome_with_runner(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
           fast = fast.next.next
           rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


