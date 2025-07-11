/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function (nums) {
  let frequencyMap = new Map();

  for (let num of nums) {
    if (frequencyMap.has(num)) {
      return true;
    }
    frequencyMap.set(num, 1);
  }
  return false;
};
