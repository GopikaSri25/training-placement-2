class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        k_sum = nums_sum // k
        max_num = max(nums)
        if max_num > k_sum :
            return False
        
        parts = [0] * k
        part_nums = [] * k
        for i in range(k):
            part_nums.append([])
        count = [0]

        nums.sort()

        invalid = set()
        visited = [False] * len(nums)

        def checkSolution(cur_part_i):
            if cur_part_i == len(parts):
                yield True
            
            unvisited_i = getLastUnvisited()
            visited[unvisited_i] = True
            parts[cur_part_i] += nums[unvisited_i]
            part_nums[cur_part_i].append(nums[unvisited_i])
            
            for current_part in addNumToPart(nums, cur_part_i, 0):
                for is_solved in checkSolution(cur_part_i + 1):
                        if is_solved:
                            yield True
                            return

            visited[unvisited_i] = False
            parts[cur_part_i] -= nums[unvisited_i]
            part_nums[cur_part_i].pop()

        def addNumToPart(nums, cur_part_i, cur_num_i):      
            if parts[cur_part_i] == k_sum:
                yield True       
                return
            
            for num_i in range(cur_num_i, len(nums)):
                if visited[num_i]:
                    continue
                count[0] += 1

                if parts[cur_part_i] + nums[num_i] > k_sum:
                    break
                
                visited[num_i] = True
                parts[cur_part_i] += nums[num_i]
                part_nums[cur_part_i].append(nums[num_i])
                for variant in addNumToPart(nums, cur_part_i, num_i + 1):
                    yield variant
                part_nums[cur_part_i].pop()
                parts[cur_part_i] -= nums[num_i]
                visited[num_i] = False
            return
        
        def getLastUnvisited():
            for i in range(len(visited)-1,-1,-1):
                if visited[i] == False:
                    return i
        
        for res in checkSolution(0):
            if res:
                return True
        
        return False
