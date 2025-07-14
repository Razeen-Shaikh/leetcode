/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const freq = {};

  for (let char of s) {
    freq[char] = (freq[char] || 0) + 1;
  }

  for (let char of t) {
    if (!freq[char]) {
      return false;
    }
    freq[char]--;
  }

  return true;
};
