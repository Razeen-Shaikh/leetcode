/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function (s) {
  let alphaNumeric = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();

  let left = 0,
    right = alphaNumeric.length - 1;

  while (left < right) {
    if (alphaNumeric[left] !== alphaNumeric[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
};
