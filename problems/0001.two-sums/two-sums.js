/**
 * Given an array of integers `nums` and an integer `target`,
 * return indices of the two numbers such that they add up to `target`.
 * You may assume that each input would have **_exactly one solution_**,
 * and you may not use the same element twice.
 * @param {number[]} numbs
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbs, target) {
  let indices = [];
  numbs.forEach((num, index) => {
    for (let i = 0; i < numbs.length; i++) {
      if (!(i === index)) {
        if (num + numbs[i] === target) {
          indices = [i, index];
        }
      }
    }
  });
  return indices;
};
