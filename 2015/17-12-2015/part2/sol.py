from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

containers = sorted(map(int, lines))

def find_number_of_ways(containers, target_vol):
    ans = defaultdict(int)
    N = len(containers)
    def helper(i, used, total):
        if total == target_vol:
            ans[used] += 1
            return
        elif total > target_vol or i == N:
            return
        
        helper(i + 1, used, total)
        helper(i + 1, used + 1, total + containers[i])
    helper(0, 0, 0)
    return ans

print(find_number_of_ways(containers, 150))
