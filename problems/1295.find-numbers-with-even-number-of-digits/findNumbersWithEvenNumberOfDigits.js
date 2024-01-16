/**
 * 1295. Find Numbers with Even Number of Digits
 * @param {number[]} nums
 * @return {number}
 */
const findNumbers = function (nums) {
  return nums.filter((num) => num.toString().length % 2 === 0).length;
};

module.exports = findNumbers;
