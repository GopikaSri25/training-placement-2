class Solution(object):
    def minimumSum(self, nums):
        
        res=[]
        i=0
        j=1
        k=j+1
        if len(nums) == 3: 
            if nums[0] < nums[1] and nums[2] < nums[1]:
                 return sum(nums)
            else:
                return -1
        while(i!=len(nums)-2):
            if(j==len(nums)-1 and i!= len(nums)-2):
                i+=1
                j=i+1
                k=j+1      
            if(k==len(nums)):
                break 
            if nums[i]<nums[j]:        
                    if nums[j]>nums[k]:       
                        res.append(nums[i]+nums[j]+nums[k])
                        k+=1
                        if k==len(nums) and j== len(nums)-2 and i == len(nums)-3:
                            break
                    else:          
                        k+=1
                    if(k==len(nums)):
                        j+=1
                        k=j+1
            else:
                    
                    j+=1
                    k=j+1
    
        if(len(res)==0):
            return -1
        else:
             return min(res)      

        
        
