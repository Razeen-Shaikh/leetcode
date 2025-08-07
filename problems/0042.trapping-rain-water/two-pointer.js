/**
 * @param {number[]} height
 * @return {number}
 */
const trap = function (height) {
  let left = 0,
    right = height.length - 1;
  let maxLeft = 0,
    maxRight = 0;
  let water = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= maxLeft) {
        maxLeft = height[left];
      } else {
        water += maxLeft - height[left];
      }
      left++;
    } else {
      if (height[right] >= maxRight) {
        maxRight = height[right];
      } else {
        water += maxRight - height[right];
      }
      right--;
    }
  }

  return water;
};
