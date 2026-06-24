/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
  let result = [];

  for (let inum of nums) {
    let count = 0;
    for (let jnum of nums) {
      if (jnum < inum) {
        count++;
      }
    }
    result.push(count);
  }

  return result;
};
