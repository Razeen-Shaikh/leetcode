/**
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive = function (nums) {
  const numSet = new Set(nums);
  let maxLength = 0;

  for (let num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let length = 1;

      while (numSet.has(currentNum + 1)) {
        currentNum++;
        length++;
      }

      maxLength = Math.max(maxLength, length);
    }
  }

  return maxLength;
};
