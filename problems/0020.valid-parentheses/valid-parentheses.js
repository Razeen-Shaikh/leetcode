/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function(s) {
    const stack = [];
    const bracketMap = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let char of s) {
        if (Object.values(bracketMap).includes(char)) {
            stack.push(char);
        } else if (Object.keys(bracketMap).includes(char) && stack.pop() !== bracketMap[char]) {
                     return false;
               }

    }

    return stack.length === 0;
};
