/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function (nums, k) {
  const freqMap = new Map();
  for (let num of nums) freqMap.set(num, (freqMap.get(num) || 0) + 1);

  const pairs = [...freqMap.entries()];

  const partition = (left, right, pivotIndex) => {
    const pivotFreq = pairs[pivotIndex][1];
    [pairs[pivotIndex], pairs[right]] = [pairs[right], pairs[pivotIndex]];
    let storeIndex = left;

    for (let i = left; i < right; i++) {
      if (pairs[i][1] > pivotFreq) {
        [pairs[storeIndex], pairs[i]] = [pairs[i], pairs[storeIndex]];
        storeIndex++;
      }
    }

    [pairs[right], pairs[storeIndex]] = [pairs[storeIndex], pairs[right]];
    return storeIndex;
  };

  let left = 0,
    right = pairs.length - 1;
  while (left <= right) {
    let pivotIndex = Math.floor(Math.random() * (right - left + 1)) + left;
    const index = partition(left, right, pivotIndex);
    if (index === k - 1) {
      break;
    } else if (index < k - 1) {
      left = index + 1;
    } else {
      right = index - 1;
    }
  }

  return pairs.slice(0, k).map((pair) => pair[0]);
};
