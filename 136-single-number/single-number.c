int singleNumber(int* nums, int numsSize) {
    int xor_output = nums[0];
    for(int i = 1; i < numsSize; i++) {
        xor_output ^= nums[i];
    }
    return xor_output;
}