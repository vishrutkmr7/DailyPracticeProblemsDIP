"""
You are given two lists of integers and an integer representing a process id to kill.
One of the lists represents a list of process ids and the other represents a list of each of the processes’
corresponding (by index) parent ids. When a process is killed, all of its children should also be killed.
Return a list of all the process ids that are killed as a result of killing the requested process.

Ex: Given the following…

pid =  [2, 4, 3, 7]
ppid = [0, 2, 2, 3]
kill = 3
the tree of processes can be represented as follows:
           2
         /   \
        4     3
             /
            7
return [3, 7] as killing process 3 will also require killing its child (i.e. process 7).
"""


class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        @solution: hashMap + dfs
        @runtime:  400ms
        @timeComplexity: O(n)
        """
        res = []
        hashMap = {}
        for i in enumerate(ppid):
            group = hashMap.setdefault(ppid[i[0]], [])
            group.append(pid[i[0]])
        self.dfs(hashMap, kill, res)
        return res

    def dfs(self, hashMap, node, res):
        res.append(node)
        if node in hashMap:
            for child in hashMap.get(node):
                self.dfs(hashMap, child, res)


# Test Cases
s = Solution()
print(s.killProcess([2, 4, 3, 7], [0, 2, 2, 3], 3))  # returns [3, 7]
