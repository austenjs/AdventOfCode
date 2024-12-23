with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

containers = sorted(map(int, lines))

def find_number_of_ways(containers, target_vol):
    ans = 0
    N = len(containers)
    def helper(i, total):
        if total == target_vol:
            nonlocal ans
            ans += 1
            return
        elif total > target_vol or i == N:
            return
        
        helper(i + 1, total)
        helper(i + 1, total + containers[i])
    helper(0, 0)
    return ans

print(find_number_of_ways(containers, 150))
