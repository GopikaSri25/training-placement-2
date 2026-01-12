class Solution {
    class DLLNode{
        int val;
        DLLNode next = null;
        public DLLNode(){}

        public DLLNode(int num){
            this.val = num;
        }
    }

    public int minimumPairRemoval(int[] nums) {
        boolean isDesc=false;
        for(int i=0; i < nums.length-1; i++){
            if(nums[i] > nums[i+1]){
                isDesc = true;
                break;
            }
        }
        if(!isDesc) return 0;

        int pair = 0;
        DLLNode head = new DLLNode(nums[0]), pointer = head;
        for(int i=1; i < nums.length; i++){
            pointer.next = new DLLNode(nums[i]);
            pointer = pointer.next;
        }
        
        while(isDesc){
            pointer = head;
            isDesc = false;
            DLLNode first = null, second = null;
            int minValue = Integer.MAX_VALUE;
            while(pointer.next!=null){
                if(pointer.val + pointer.next.val < minValue){
                    minValue = pointer.val + pointer.next.val;
                    first = pointer; second = pointer.next;
                }
                if(pointer.next==null) break;
                pointer = pointer.next;
            }
            first.val = first.val + second.val;
            first.next = second.next;

            pointer = head;
            while(pointer!=null){
                if(pointer.next!=null && pointer.val > pointer.next.val){
                    isDesc = true;
                    break;
                }
                pointer = pointer.next;
            }
            pair++;
        }
        return pair;
    }
}
