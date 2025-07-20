# Last updated: 7/20/2025, 9:30:35 PM
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # Backtracking
        kids = [0]*k
        n = len(cookies)
        ans = math.inf
        mem = {}

        # 5,4,4,5,4
        # [5, 0], [0, 5]
        # [9, 0], [5, 4],    [4, 5], [0, 9]
        # [13, 0], [9, 4], [9, 4], [5, 8],     [8, 5], [4, 9], [4, 9], [0, 13]

        def bt(i, count):
            nonlocal ans
            #if (i, tuple(kids)) in mem:
            #    return mem[(i, tuple(kids))]
            if i == n:
                mx = max(kids)
                ans = min(ans, mx)
                return mx
            if n-i < k-count:
                return

            #max_assign = math.inf
            for j in range(k):
                kids[j] += cookies[i]
                if kids[j] < ans:
                    #max_assign = min(max_assign, bt(i+1))
                    bt(i+1, count+ (kids[j] == cookies[i]))
                kids[j] -= cookies[i]
            #mem[(i, tuple(kids))] = max_assign
            #return max_assign
        bt(0, 0)
        return ans






        # 5, 5, 4, 4, 4 = min = 11 and max 22
        left, right = max(cookies), sum(cookies)
        ans = 0

        def enough(size):
            kids = 0
            total = 0
            max_total = 0
            for cookie in cookies:
                if total + cookie > size:
                    max_total = max(max_total, total)
                    total = 0
                if total == 0:
                    kids += 1
                total += cookie
            max_total = max(max_total, total)

            return kids, max_total
            

        while left <= right:
            mid = (left + right) // 2

            kids, max_assigned = enough(mid)
            if kids <= k:
                if kids == k:
                    ans = max_assigned
                right = mid - 1
            else:
                left = mid + 1

        return ans






















        
        total = sum(cookies)
        left  = max(cookies)
        right = max(left, (total // k) + (total % 2))

        def canDistribut(limit):
            kid_total = 0
            kids = 1
            max_cookie = 0
            for cookie in cookies:
                if kid_total + cookie > limit:
                    max_cookie = max(max_cookie, kid_total)
                    kid_total = 0
                    kids += 1
                    if kids >= k:
                        return True, max_cookie
                kid_total += cookie
            max_cookie = max(max_cookie, kid_total)
            return kids >= k, max_cookie
        
        ans = 0
        while left <= right:
            #print(left, right)
            mid = (left + right) // 2

            found, max_cookie = canDistribut(mid)
            if found:
                ans = max_cookie
                left = mid + 1
            else:
                right = mid - 1
        return ans