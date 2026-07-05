class Solution(object):
    def triangleType(self, nums):
        a=nums[0] + nums[1] 
        b=nums[0] + nums[2] 
        c=nums[1] + nums[2]

        e=nums[2]
        f=nums[1]
        g=nums[0]

        if nums[0]==nums[1] and nums[1]==nums[2]:
            a="equilateral"
            return a

        if nums[0]==nums[1] or nums[0]==nums[2] or nums[1]==nums[2]:
            s="isosceles"
            n="none"
            if nums[0]==nums[1]:
                if a>e:
                    return s
                else:
                    return n

            if nums[0]==nums[2]:
                if b>f:
                    return s
                else:
                    return n
            if nums[1]==nums[2]:
                if c>g:
                    return s
                else:
                    return n
            

        else:
            if a>e and b>f and c>g:
                q="scalene"
                return q
            else:
                l="none"
                return l

            

