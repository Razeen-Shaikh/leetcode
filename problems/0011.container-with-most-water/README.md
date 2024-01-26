# 11. Container With Most Water

1. **Start with two pointers:** Initially, place two pointers, `left` at the beginning of the array (`0`) and `right` at the end of the array (`len(height) - 1`).

2. **Calculate the current area:** The area of the container is determined by the minimum height between the lines at the two pointers multiplied by the width (distance between the pointers).

   ```py
   current_area = min(height[left], height[right]) * (right - left)
   ```

3. **Update maximum water:** Update the maximum water if the current area is greater than the previous maximum water.

   ```py
   max_water = max(max_water, current_area)
   ```

4. **Move pointers:** Move the pointers towards each other. Decide which pointer to move based on the height of the lines. Since the goal is to maximize the area, move the pointer that is pointing to the shorter line. If you move the pointer pointing to the taller line, the height of the container won't increase, and the width will decrease, resulting in a smaller area.

   ```py
   if height[left] < height[right]:
       left += 1
   else:
       right -= 1
   ```

5. **Repeat:** Continue steps 2-4 until the pointers meet.

The idea behind this approach is to gradually converge the two pointers towards each other while considering the height of the lines. By always moving the pointer pointing to the shorter line, you are increasing the chance of finding a taller line that might result in a larger area. This ensures that the algorithm explores various possibilities and converges to the maximum water-containing configuration. The final result is the maximum water that can be stored by any pair of lines in the array.
