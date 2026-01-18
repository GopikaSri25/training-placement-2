class Solution(object):
    def removeComments(self, source):
        incomment = False
        needjoin = False
        ans = []
        for line in source:
            tempstring = ""
            x = 0
            while x < len(line):
                if line[x] == "/":
                    if not incomment:
                        if x == len(line)-1:
                            tempstring += line[x]
                            break
                        if line[x+1] == "/":
                            break
                        if line[x+1] == "*":
                            incomment = True
                            x += 1
                        else:
                            tempstring += line[x]
                elif line[x] == "*":
                    if not incomment:
                        tempstring += line[x]
                    elif x < len(line)-1 and line[x+1] == "/":
                        incomment = False
                        x += 1
                elif not incomment:
                    tempstring += line[x]

                x += 1

            if len(tempstring) > 0:
                print(tempstring)
                if needjoin:
                    ans[-1] = ans[-1] + tempstring
                    needjoin = False
                else:
                    ans.append(tempstring)
                if incomment:
                    needjoin = True
            elif needjoin and not incomment:
                needjoin = False
        
        return ans

        
