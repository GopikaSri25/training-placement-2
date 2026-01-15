class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0] * n
        st = []

        for i in logs:
            x = i.split(":")

            if x[1] == 'end':
                curr = 0

                while len(st[-1]) == 1:
                    curr += st.pop()[0]
                y = st.pop()
                res[int(x[0])] += int(x[2]) - int(y[2]) + 1 - curr 
                st.append([int(x[2]) - int(y[2]) + 1])

            else:
                st.append(x)
        return res
