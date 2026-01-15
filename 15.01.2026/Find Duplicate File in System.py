class Solution(object):
    def findDuplicate(self, paths):
        same_content_files = {}

        for path in paths:
            files = path.split(" ")

            root_name = ""

            for i, file_name in enumerate(files):
                if i == 0:
                    root_name = file_name
                else:
                    start_p = file_name.find("(") + 1
                    end_p = file_name.find(")") - 1

                    content = file_name[start_p:end_p+1]

                    if content not in same_content_files:
                        same_content_files[content] = []
                    
                    same_content_files[content].append(root_name + "/" + file_name[0:start_p-1])
        
        ans = []

        for file_entry in same_content_files:
            if len(same_content_files[file_entry]) > 1:
                ans.append(same_content_files[file_entry])
        
        return ans
