/**
 * 383. Ransom Note
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
	if (ransomNote === magazine) return true;
	let ransom = ransomNote.split("").sort();
	let mag = magazine.split("").sort();
	return ransom.every((ran, index) => {
		if (mag.includes(ran)) {
			mag.splice(mag.indexOf(ran), 1);
			return true;
		}
	});
};

// Use Default Props
const ShoppingCart = (props) => {
	return (
		<div>
			<h1>Shopping Cart Component</h1>
		</div>
	)
};
// Change code below this line
ShoppingCart.defaultProps = { items: 0 };
