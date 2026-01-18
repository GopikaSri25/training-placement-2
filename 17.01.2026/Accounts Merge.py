class Solution(object):
    def accountsMerge(self, accounts):
        def dfs(email_list, email):
            if email in visited:
                return
            else:
                visited.add(email)
                email_list.append(email)
                for nb in nb_lookup[email]:
                    dfs(email_list, nb)

        nb_lookup = collections.defaultdict(set)
        visited = set()

        for idx, ele in enumerate(accounts):
            email = ele[1]
            for j in range(2, len(ele), 1):
                nb_lookup[email].add(ele[j])
                nb_lookup[ele[j]].add(email)

        res = []
        for idx, ele in enumerate(accounts):
            name = ele[0]
            email = ele[-1]
            if email not in visited:
                email_list = []
                dfs(email_list, email)
                email_list.sort()
                email_list.insert(0, name)
                res.append(email_list)

        return res

        






        





        
