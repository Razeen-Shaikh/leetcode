/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    let n = nums.length;
    let seen = new Array(n + 1).fill(false);
    let duplicate = -1;

    for (let num of nums) {
        if (seen[num]) {
            duplicate = num;
        }
        seen[num] = true;
    }

    let missing = -1;
    for (let i = 1; i <= n; i++) {
        if (!seen[i]) {
            missing = i;
            break;
        }
    }

    return [duplicate, missing];
};