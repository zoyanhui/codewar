Description:

Create a function that finds the largest palindromic number made from the product of any amount of numeric arguments.

Example:

numericPalindrome(937,113) === 81518
As 937 * 113 = 105881 and the largest palindromic number that can be arranged from this result is: 81518.

Further example:

numericPalindrome(57,62,23)==82128
Because you try all possible combinations (57*62,57*23,62*23 and 57*62*23) and find that the product 81282 allow to create the largest palindrome (then again: notice that you are must not necessarily use all the digits of a product, as it was by chance in this case).

Note: single digits numbers are still considered (edge) palindromes, so for:

Test.assert_equals(numeric_palindrome(15, 125, 8),8)
You try all possible combinations (15*125,15*8,125*8,15*125*8) and find that 1875 generates the largest palindrome number, namely 8.

Notes and tips

This kata is quite demanding, as you will need to manage all possible combinations to get products, then use all or some of the digits of each product to get the largest palindrome: as you can easily guess, the computing time can easily grow exponentially, so you will need to work on optimization to be able to make it in the alloted time.

Dealing with 1s and 0s when passed as parameters in a smart way could help. A lot.