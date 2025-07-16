/**
 * @param {number} n
 * @return {number[]}
 */
const lexicalOrder = function (n) {
  const result = [];
  let curr = 1;

  for (let i = 0; i < n; i++) {
    result.push(curr);
    if (curr * 10 <= n) {
      curr *= 10;
    } else {
      while (curr % 10 === 9 || curr + 1 > n) {
        curr = Math.floor(curr / 10);
      }
      curr++;
    }
  }

  return result;
};
