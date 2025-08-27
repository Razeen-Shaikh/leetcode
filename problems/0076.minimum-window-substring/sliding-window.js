/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  if (!s || !t || s.length < t.length) return "";

  const need = new Map();
  for (let char of t) {
    need.set(char, (need.get(char) || 0) + 1);
  }

  let left = 0,
    right = 0;
  let required = need.size;
  let formed = 0;
  const windowCounts = new Map();
  let minLen = Infinity,
    minStart = 0;

  while (right < s.length) {
    let char = s[right];
    windowCounts.set(char, (windowCounts.get(char) || 0) + 1);

    if (need.has(char) && windowCounts.get(char) === need.get(char)) {
      formed++;
    }

    while (left <= right && formed === required) {
      if (right - left + 1 < minLen) {
        minLen = right - left + 1;
        minStart = left;
      }

      let leftChar = s[left];
      windowCounts.set(leftChar, windowCounts.get(leftChar) - 1);

      if (
        need.has(leftChar) &&
        windowCounts.get(leftChar) < need.get(leftChar)
      ) {
        formed--;
      }

      left++;
    }

    right++;
  }

  return minLen === Infinity ? "" : s.substring(minStart, minStart + minLen);
};
