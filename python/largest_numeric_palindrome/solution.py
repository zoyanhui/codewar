def chooseMaxPalindrome(value):
    nums = [int(x) for x in str(value)]
    nums.sort(reverse = True)
    i = 0
    highvalue = 0
    lowvalue = 0
    lowvaluebase = 1
    maxsingle = None
    highzeros = True
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            if nums[i] != 0:
                highzeros = False
            if not highzeros:
                highvalue = highvalue * 10 + nums[i]
                lowvalue += nums[i] * lowvaluebase
                lowvaluebase *= 10
            i += 2
        else:
            if maxsingle is None:
                maxsingle = nums[i]
            i += 1
    if i == len(nums) -1:
        maxsingle = nums[-1] if nums[-1] > maxsingle else maxsingle
    if maxsingle is None:
        return lowvaluebase * highvalue + lowvalue
    return lowvaluebase * maxsingle + lowvaluebase * 10 * highvalue + lowvalue

def numeric_palindrome(*args):
    maxval = 0
    for product in complete_combine_products(1, 0, 0, args):
        palindome_product = chooseMaxPalindrome(product)
        if palindome_product > maxval:
            maxval = palindome_product
    return maxval

def complete_combine_products(curproduct, curidx, curnums, ll):
    if curidx == len(ll):
        return
    next = curproduct * ll[curidx] 
    if curnums >=1:
        yield next
    for x in complete_combine_products(curproduct, curidx + 1, curnums, ll):
        yield x
    for x in complete_combine_products(next, curidx + 1, curnums + 1, ll):
        yield x


def complete_permutation(prefix, curidx, ll, retlist):
    if curidx == len(ll):
        retlist.append(prefix)
        return
    for i in range(curidx, len(ll)):
        ll[i], ll[curidx] = ll[curidx], ll[i]
        complete_permutation(prefix + [ll[curidx]], curidx + 1, ll, retlist)    
        ll[i], ll[curidx] = ll[curidx], ll[i]

def complete_combine(prefix, curidx, ll, retlist):    
    if curidx == len(ll):
        return
    retlist.append(prefix + [ll[curidx]]) 
    complete_combine(prefix, curidx + 1, ll, retlist)    
    complete_combine(prefix + [ll[curidx]], curidx + 1, ll, retlist)


if __name__ == '__main__':    
    print numeric_palindrome(57,62,23)==82128


