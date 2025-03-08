class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')
        current_white_count = sum(1 for i in range(k) if blocks[i] == 'W')

        min_operations = current_white_count

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_white_count -= 1
            if blocks[i] == 'W':
                current_white_count += 1
            min_operations = min(min_operations, current_white_count)

        return min_operations