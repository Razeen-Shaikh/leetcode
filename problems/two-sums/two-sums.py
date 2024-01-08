# /**
#  * 1. Two Sum
#  * @param {number[]} numbs
#  * @param {number} target
#  * @return {number[]}
#  */
def twoSum(numbs, target):
    indices = []
    for i in range(len(numbs)):
        for j in range(len(numbs)):
            if(not(i == j)):
                if(numbs[i] + numbs[j] == target):
                    indices = [j, i]
    return indices
