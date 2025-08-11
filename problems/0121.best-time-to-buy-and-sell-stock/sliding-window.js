/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function (prices) {
  let left = 0,
    right = 1;
  let max_profit = 0;

  while (right < prices.length) {
    if (prices[right] > prices[left]) {
      let profit = prices[right] - prices[left];
      max_profit = Math.max(max_profit, profit);
    } else {
      left = right;
    }

    right++;
  }

  return max_profit;
};
