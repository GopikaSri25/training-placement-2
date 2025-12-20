class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {

   	int [] count1 = new int[101];
    	int [] count2 = new int[101];
    	int [] count3 = new int[101];
    	for (int i = 0; i < nums1.length; i++) {
			
    		if(count1[nums1[i]]==0) {
    			count1[nums1[i]]++;	
    		}
		}
    	for (int i = 0; i < nums2.length; i++) {
			
    		if(count2[nums2[i]]==0) {
    			count2[nums2[i]]++;	
    		}
		}
    	for (int i = 0; i < nums3.length; i++) {
			
    		if(count3[nums3[i]]==0) {
    			count3[nums3[i]]++;	
    		}
		}
    	
    	List<Integer> result = new LinkedList<>();
    	for(int i=1;i<101;i++) {
    		
    		if(count1[i]+count2[i]+count3[i]>1) {
    			result.add(i);
    		}
    	}
    	return result;    		
            
    }
}
