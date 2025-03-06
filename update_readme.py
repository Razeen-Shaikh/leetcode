import requests
import json

LEETCODE_USERNAME = "your_leetcode_username"
README_PATH = "README.md"

# Fetch LeetCode solved problems using an API
def fetch_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Update README file
def update_readme(solved, total):
    with open(README_PATH, "r") as file:
        readme_lines = file.readlines()

    new_content = []
    inside_section = False

    for line in readme_lines:
        if "<!-- LEETCODE:START -->" in line:
            inside_section = True
            new_content.append("<!-- LEETCODE:START -->\n")
            new_content.append(f"- **Total Problems Solved:** {solved} / {total}\n")
        elif "<!-- LEETCODE:END -->" in line:
            inside_section = False
            new_content.append("<!-- LEETCODE:END -->\n")
        elif not inside_section:
            new_content.append(line)

    with open(README_PATH, "w") as file:
        file.writelines(new_content)

# Run the update process
leetcode_stats = fetch_leetcode_stats(LEETCODE_USERNAME)

if leetcode_stats:
    total_solved = leetcode_stats.get("totalSolved", 0)
    total_questions = leetcode_stats.get("totalQuestions", 0)
    update_readme(total_solved, total_questions)
    print(f"Updated README: {total_solved} problems solved!")
else:
    print("Failed to fetch LeetCode stats.")
