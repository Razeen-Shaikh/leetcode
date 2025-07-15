/**
 * Given an array of integers `nums` and an integer `target`,
 * return indices of the two numbers such that they add up to `target`.
 * You may assume that each input would have **_exactly one solution_**,
 * and you may not use the same element twice.
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let indices = [];

  for (let num of nums) {
    for (let i = 0; i < nums.length; i++) {
      if (!(i === index)) {
        if (num + nums[i] === target) {
          indices = [i, index];
        }
      }
    }
  }

  return indices;
};
