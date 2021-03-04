from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            item_type, color, name = item
            if ruleKey == 'type' and ruleValue == item_type:
                count += 1

            elif ruleKey == 'color' and ruleValue == color:
                count += 1

            elif ruleKey == 'name' and ruleValue == name:
                count += 1
        return count
