# words="Nitin"
# count={}
# for char in words.lower():
#     if char in count:
#         count[char] +=1
#     else:
#         count[char] = 1
# print(count)

def atm_withdrawal(s):
    Available_denominations=[100, 200, 500, 2000]

    if type(s) != int:
        return "Input should be integer"

    if s <= 0:
        return "Input should be a positive integer"

    if s % 100 != 0:
        return "Input should be multiple of 100"

    two_thousand_count = s // 2000
    balance_after_2000 = s - 2000 *  two_thousand_count
    five_hundered_count = balance_after_2000 // 500
    balance_after_500 = balance_after_2000 - 500 * five_hundered_count
    two_hundered_count = balance_after_500 // 200
    balance_after_200 = balance_after_500 - 200 * two_hundered_count
    one_hundered_count = balance_after_200 // 100
    balance_after_100 = balance_after_200 - 100 * one_hundered_count

    return (dict(two_thousand_count=f"{two_thousand_count}", five_hundered_count=f"{five_hundered_count}",
    two_hundered_count=f"{two_hundered_count}", one_hundered_count=f"{one_hundered_count}"))

print(atm_withdrawal(5300))
