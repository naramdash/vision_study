# Listing 11.3 snippet.
# Assumes cv2 has been imported and `coins` plus `cnts` are already defined,
# as in counting_coins.py.

cv2.drawContours(coins, cnts, 0, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 1, (0, 255, 0), 2)
cv2.drawContours(coins, cnts, 2, (0, 255, 0), 2)
