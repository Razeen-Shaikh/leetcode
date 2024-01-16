"""Find the Peaks"""
from ast import List

class FindPeaks:
    """Find the Peaks"""
    def find_peaks(self, mountain: List[int]) -> List[int]:
        """
        Find the indices of the peaks in a mountain list.

        Args:
            mountain (List[int]): The list of mountain heights.

        Returns:
            List[int]: The indices of the peaks in the mountain list.
        """
        indices = [
            i
            for i in range(1, len(mountain)-1)
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]
        ]
        return indices
