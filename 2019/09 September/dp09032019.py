# This problem was recently asked by Twitter:

# You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    # Fill this in.
    pool = []
    for i in lists:
        status = True
        while status:
            pool.append(i.val)
            if i.next == None:
                status = False
            i = i.next

    pool.sort()
    ans = temp = Node(pool[0])
    for j in range(1, len(pool)):
        temp.next = Node(pool[j])
        temp = temp.next

    return ans


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456
