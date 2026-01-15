class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        max_c = max(count.values())
        ans = (n+1) * (max_c-1)
        for c in count.values():
            if c == max_c:
                ans += 1
        return max(ans, len(tasks))

        
