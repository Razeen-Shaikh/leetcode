/**
 * 242. Valid Anagram
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }

  let str1 = s.split("").sort().join("").toLowerCase();
  let str2 = t.split("").sort().join("").toLowerCase();

  return str1 === str2;
};
