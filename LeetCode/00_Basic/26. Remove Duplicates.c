int removeDuplicates(int* nums, int numsSize) {
    // exception handling
    if (numsSize == 0) return 0;
    // the number of unique values
    // index 0 element is always unique so starts with index 1
    int k = 1;
    // iterating sorted list, find duplicates
    for (int i = 1; i<numsSize; i++) {
        // comparing with previous value
        if (nums[i] != nums[i-1]) { // if current value is different from previous value
            // new unique value is found
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}
