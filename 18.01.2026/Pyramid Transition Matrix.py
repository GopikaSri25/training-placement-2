class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        dic = defaultdict(list)
        for a in allowed:
            dic[a[:2]].append(a[2])
        memo = {}

        def make_next_bottoms(l):
            prev_ans =[""]
            next_ans =[]
            for sub_l in l:
                for c in sub_l:
                    for p_a in prev_ans:
                        next_ans.append(p_a+c)
                prev_ans = next_ans[:]
                next_ans = []
            return prev_ans
        def helper(l):
            len_l = len(l)
            if len_l==1:
                return True
            if l in memo:
                return memo[l]

            next_char_list = []
            next_bottoms=[]
            for i in range(1,len_l):
                pair = l[i-1]+l[i]
                if pair in dic:
                    next_char_list.append(dic[pair])
                else:
                    memo[l] = False
                    return False
            
            next_bottoms = make_next_bottoms(next_char_list)
            for next_bottom in next_bottoms:
                if helper(next_bottom):
                    memo[next_bottom] = True
                    return True

            memo[l] = False
            return False

        return helper(bottom)
