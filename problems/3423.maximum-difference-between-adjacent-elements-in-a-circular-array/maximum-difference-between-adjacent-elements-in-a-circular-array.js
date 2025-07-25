/**
 * @param {number[]} nums
 * @return {number}
 */
let maxAdjacentDistance = function(nums) {
    let maxDiff = 0;
    const n = nums.length;

    for (let i = 0; i < n; i++) {
        const nextIndex = (i + 1) % n;
        const diff = Math.abs(nums[i] - nums[nextIndex]);
        maxDiff = Math.max(maxDiff, diff);
    }

    return maxDiff;
};