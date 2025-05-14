import requests

# Your LeetCode username
LEETCODE_USERNAME = "srazeen"
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"
README_PATH = "README.md"

def fetch_leetcode_stats(username):
    query = {
        "query": """
        query recentAcSubmissions($username: String!) {
            recentAcSubmissionList(username: $username, limit: 10) {
                title
                titleSlug
            }
            matchedUser(username: $username) {
                submitStats: submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }
            }
        }
        """,
        "variables": {"username": username},
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post("https://leetcode.com/graphql", json=query, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and data["data"].get("matchedUser"):
            return data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
    else:
        print(f"❌ API Request Failed: {response.status_code}, Response: {response.text}")

    return None, None


def generate_badge(solved_count):
    return f"https://img.shields.io/badge/LeetCode_Solved-{solved_count}-orange?style=for-the-badge&logo=leetcode"

def update_readme(stats):
    total_solved = stats[0]["count"]  # Get total solved problems
    badge_url = generate_badge(total_solved)

    with open(README_PATH, "r") as file:
        readme_lines = file.readlines()

    new_content = []
    inside_section = False

    for line in readme_lines:
        if "<!-- LEETCODE:START -->" in line:
            inside_section = True
            new_content.extend(
                (
                    "<!-- LEETCODE:START -->\n",
                    f"![LeetCode Total Solved]({badge_url})\n",
                )
            )
        elif "<!-- LEETCODE:END -->" in line:
            inside_section = False
            new_content.append("<!-- LEETCODE:END -->\n")
        elif not inside_section:
            new_content.append(line)

    with open(README_PATH, "w") as file:
        file.writelines(new_content)

if stats := fetch_leetcode_stats(LEETCODE_USERNAME):
    update_readme(stats)
    print("✅ README updated with latest LeetCode stats!")
else:
    print("❌ Failed to fetch LeetCode stats.")
