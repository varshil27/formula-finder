def checker(data,signs,target_indx):
    """Function to check and avoid false positives for formula cells
    Parameters:
        - data (list): List of lists containing the data to be checked.
        - signs (list): List of integers representing the signs of the formula.
        - target_indx (int): Index of the target cell to be checked.
    Returns:
        - valid (bool): Boolean value indicating whether the formula is valid or not.
    Processing Logic:
        - Loops through each column in the data and calculates the sum of the values multiplied by the corresponding sign.
        - Compares the calculated sum to the value in the target cell.
        - If the sum does not match, the formula is considered invalid and the function returns False. Otherwise, it returns True."""
    signs = signs[::-1]
    start_indx = target_indx-len(signs)
    valid = True
    for col in data:
        sum = 0
        for i in range(start_indx,target_indx):
            sum += (signs[i-start_indx] * col[i])
        if sum!=col[target_indx]:
            valid = False
            break
    return valid




def rec(indx,target_indx, req, nums, signs, comb_signs,data,vis):
    """Purpose:
        This function recursively generates all possible combinations of signs for a given set of numbers and a target index.
    Parameters:
        - indx (int): The current index being evaluated.
        - target_indx (int): The target index to be reached.
        - req (int): The current required value to reach the target index.
        - nums (list): The list of numbers to be evaluated.
        - signs (list): The current list of signs being evaluated.
        - comb_signs (list): The final list of all possible combinations of signs.
        - data (list): List of lists containing the data to be checked.
    Returns:
        - comb_signs (list): The final list of all possible combinations of signs.
    Processing Logic:
        - Checks if the current combination of signs is valid.
        - Recursively calls the function for each possible sign at the current index.
        - Appends the current sign to the list of signs being evaluated.
        - Pops the current sign from the list of signs being evaluated."""
    if len(comb_signs)>0 or len(signs)>10:
        return
    if req == 0:
        valid = checker(data,signs,target_indx)
        if valid==True:
            comb_signs.append(signs[:])

    if indx < 0:
        return

    for new_sign in range(-1,2):
        signs.append(new_sign)
        if new_sign == 0:
            rec(indx-1,target_indx, req, nums, signs, comb_signs,data,vis)
        elif new_sign == 1 and vis[indx]==0:
            rec(indx-1,target_indx, req-nums[indx], nums, signs, comb_signs,data,vis)
        elif new_sign == -1 and vis[indx]==0:
            rec(indx-1,target_indx, req+nums[indx], nums, signs, comb_signs,data,vis)
        signs.pop()

def find_formula(data,vis,nums, target,target_indx):
    """Finds formula for a single cell.
    """
    comb_signs = []
    rec(target_indx-1,target_indx, target, nums, [], comb_signs,data,vis)
    comb_signs.append([])
    return comb_signs[0]

def get_all_formulas(data):
    all_formulas = []
    nums = data[0]
    vis = [0]*(len(nums))
    for i in range(len(nums)):
        target = nums[i]

        result = find_formula(data,vis,nums,target,i)
        result = result[::-1]
        formula = []
        for j in range(i-len(result),i):
            vis[j] = 1
            if result[j-(i-len(result))]==0 : continue
            formula.append(result[j-(i-len(result))]*(j+1))

        all_formulas.append(formula)
    return all_formulas