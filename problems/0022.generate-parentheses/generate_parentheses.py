from typing import List

class Solution:
    """
    This class provides a solution for generating all combinations of well-formed parentheses.
    """
    def generate_parenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.
    
        Args:
        - n: int - the number of pairs of parentheses to generate
    
        Returns:
        - List[str] - a list of all the valid combinations of parentheses
        """
        def generate(p, left, right, parens=None):
            parens = [] if parens is None else parens
            if left:
                generate(p + '(', left-1, right)
            if right > left:
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
            return parens

        return generate('', n, n)
