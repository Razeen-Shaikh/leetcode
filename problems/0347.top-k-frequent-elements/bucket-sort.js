/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function (nums, k) {
  const freqMap = new Map();
  for (let num of nums) freqMap.set(num, (freqMap.get(num) || 0) + 1);

  const bucket = Array(nums.length + 1)
    .fill(null)
    .map(() => []);
  for (let [num, freq] of freqMap.entries()) bucket[freq].push(num);

  const result = [];
  for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
    for (let num of bucket[i]) result.push(num);
  }

  return result.slice(0, k);
};
