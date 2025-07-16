/**
 * @param {number} n
 * @return {number[]}
 */
const lexicalOrder = function (n) {
  const result = [];

  const dfs = (current) => {
    if (current > n) {
      return;
    }

    result.push(current);
    for (let i = 0; i < 10; i++) {
      const next = current * 10 + i;
      if (next > n) {
        return;
      }
      dfs(next);
    }
  };

  for (let i = 1; i <= 9; i++) {
    dfs(i);
  }

  return result;
};
