class Solution(object):
    def getImportance(self, employees, id):
        i_to_e = {}
        e_to_i = {}
        j = 0
        for i in range(len(employees)):
            if id == employees[i].id:
                j = i
            i_to_e[i] = employees[i].id
            e_to_i[employees[i].id] = i
        h = {}
        self.total = 0
        def dfs(index):
            h[index] = 1
            self.total += employees[index].importance
            for n in employees[index].subordinates:
                if e_to_i[n] not in h:
                    dfs(e_to_i[n])
            return self.total        
        return dfs(j)
