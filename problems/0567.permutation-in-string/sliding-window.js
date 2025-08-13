/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const checkInclusion = function (s1, s2) {
  if (s1.length > s2.length) return false;

  const count1 = new Array(26).fill(0);
  const count2 = new Array(26).fill(0);
  const aCode = "a".charCodeAt(0);

  for (let i = 0; i < s1.length; i++) {
    count1[s1.charCodeAt(i) - aCode]++;
    count2[s2.charCodeAt(i) - aCode]++;
  }

  for (let i = s1.length; i < s2.length; i++) {
    if (arraysEqual(count1, count2)) return true;

    count2[s2.charCodeAt(i) - aCode]++;
    count2[s2.charCodeAt(i - s1.length) - aCode]--;
  }

  return arraysEqual(count1, count2);
};

const arraysEqual = (a, b) => {
  for (let i = 0; i < 26; i++) {
    if (a[i] !== b[i]) return false;
  }

  return true;
};
