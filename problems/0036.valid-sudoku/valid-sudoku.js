/**
 * @param {character[][]} board
 * @return {boolean}
 */
const isValidSudoku = function (board) {
  let [row] = board;
  let column = row.map((_, column) => board.map((row) => row[column]));
  let sub_boxes = Array(9).fill([]);
  let valid = false;

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      let boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
      sub_boxes[boxIndex] = [...sub_boxes[boxIndex], board[i][j]];
    }
  }

  for (let i = 0; i < board.length; i++) {
    valid =
      !board[i].some(
        (r, index) => r !== "." && board[i].indexOf(r) !== index
      ) &&
      !column[i].some(
        (col, index) => col !== "." && column[i].indexOf(col) !== index
      ) &&
      !sub_boxes[i].some(
        (sub, index) => sub !== "." && sub_boxes[i].indexOf(sub) !== index
      );
    if (!valid) return false;
  }

  return valid;
};
