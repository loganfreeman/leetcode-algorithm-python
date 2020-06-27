    def fourSum( self,nums, target):
        def threeSum(nums,target):
            def twosum(target,num,nums,final):
                i=0
                j=len(nums)-1
                target0=target-num
                while i !=j:
                    if nums[i]+nums[j]<target0:
                        i+=1
                    elif nums[i]+nums[j]>target0:
                        j-=1
                    else:
                        a=[num,nums[i],nums[j]]
                        i+=1
                        while nums[i]==nums[i-1]and i!=j:
                            i+=1
                        final.append(a)
                return final
            result = []
            for i in range(len(nums)-2):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                else:
                    newnums=nums[i+1:]
                    result=twosum(target,nums[i],newnums,result)
            return result
        if len(nums) < 4:
            return []
        nums.sort()
        i = 0
        result = []
        for i in range(len(nums) - 3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            subsum1 = nums[i]
            subsum2 = target - subsum1
            newlist = nums[i+1:]
            thresult = threeSum(newlist, subsum2)
            if len(thresult) > 0:
                for list in thresult:
                    list.append(subsum1)
                    result.append(list)
        return result