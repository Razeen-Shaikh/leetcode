/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function (nums, k) {
  const map = new Map();

  for (let num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  }

  const sorted = [...map.entries()].sort((a, b) => b[1] - a[1]);

  return sorted.slice(0, k).map((pair) => pair[0]);
};
