class Solution {
    public int largestInteger(int number) {
        List<Integer> oddNumbers = new ArrayList<Integer>();
		List<Integer> evenNumbers = new ArrayList<Integer>();

		for (char c : String.valueOf(number).toCharArray()) {
			if ((c - '0') % 2 == 0) {
				evenNumbers.add(c - '0');
			} else {
				oddNumbers.add(c - '0');
			}
		}

		Collections.sort(oddNumbers, Collections.reverseOrder());
		Collections.sort(evenNumbers, Collections.reverseOrder());

		StringBuffer maxNumber = new StringBuffer();
		int evenIndex = 0;
		int oddIndex = 0;
		for (char c : String.valueOf(number).toCharArray()) {
			if ((c - '0') % 2 == 0 && evenIndex < evenNumbers.size()) {
				maxNumber.append(evenNumbers.get(evenIndex++));
			} else {
				maxNumber.append(oddNumbers.get(oddIndex++));
			}
		}

		return Integer.parseInt(maxNumber.toString());
    }
}
