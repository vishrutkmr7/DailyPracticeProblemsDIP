# This problem was recently asked by Google:

# Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    # Function to print the list
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        # Implement this.
        node = head
        finalList = []
        while node != None:
            finalList.append(node.val)
            node = node.next

        finalList.reverse()
        startNode = n = ListNode(finalList[0])
        for i in range(1, len(finalList)):
            n.next = ListNode(finalList[i])
            n = n.next

        return startNode


    # Recursive Solution 
    finalList = []    
    def reverseRecursively(self, head):
        # Implement this.
        if head != None:
            self.finalList.append(head.val)
            if head.next != None:
                self.reverseRecursively(head.next)
        else:
            self.finalList.reverse()
            startNode = n = ListNode(self.finalList[0])
            for i in range(1, len(self.finalList)):
                n.next = ListNode(self.finalList[i])
                n = n.next

            return startNode



# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0

print("List after Iterative reversal: ")
testHead.reverseIteratively(testHead).printList()
# testTail.printList()
# 0 1 2 3 4

# print("List after Recursive reversal: ")
# testHead.reverseRecursively(testHead).printList()
# testTail.printList()
# 0 1 2 3 4