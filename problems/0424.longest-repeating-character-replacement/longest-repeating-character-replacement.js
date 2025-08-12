/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const characterReplacement = function (s, k) {
  let left = 0;
  let maxCount = 0;
  let freq = new Array(26).fill(0);
  let result = 0;

  for (let right = 0; right < s.length; right++) {
    const index = s.charCodeAt(right) - "A".charCodeAt(0);
    freq[index]++;
    maxCount = Math.max(maxCount, freq[index]);

    while (right - left + 1 - maxCount > k) {
      freq[s.charCodeAt(left) - "A".charCodeAt(0)]--;
      left++;
    }

    result = Math.max(result, right - left + 1);
  }

  return result;
};
