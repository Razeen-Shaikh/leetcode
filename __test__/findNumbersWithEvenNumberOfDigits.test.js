const findNumbers = require("../problems/1295.find-numbers-with-even-number-of-digits/findNumbersWithEvenNumberOfDigits");

// Test case: Empty array
test("Empty array should return 0", () => {
  expect(findNumbers([])).toBe(0);
});

// Test case: Array with no numbers with even number of digits
test("Array with no numbers with even number of digits should return 0", () => {
  expect(findNumbers([1, 3, 5, 7])).toBe(0);
});

// Test case: Array with one number with even number of digits
test("Array with one number with even number of digits should return 1", () => {
  expect(findNumbers([12])).toBe(1);
});

// Test case: Array with multiple numbers with even number of digits
test("Array with multiple numbers with even number of digits should return the correct count", () => {
  expect(findNumbers([12, 345, 6789, 987654, 0])).toBe(3);
});
