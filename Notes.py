#How to create a chance that a player injures themselves on Gameday
#The injury would cause the match to be an automatic loss.
#Generally injuries cause player traits that lower skill X amount. However some injuries can set skill to 0.

#Matchday Chance Indicator:
#   Each match has a horizontal bar that fills with GREEN from the left and RED from the right.
#   There's an animation that showws the two colors colliding and pushing each other.
#   At the halfway point in the match the colors settle. Where they land dictates the odds of each player winning the remainder of the match.
#   If the opponent has 70% odds of winning than the bar will be 30% green from the left and 70% red from the right.
#   After the halfway break, an arrow appears and slides back and forth across the bar. Where it stops determines the winner.
#   The arrow has an even chance of stopping anywhere along the bar. So if 70% of the bar is red than the odds of the arrow landing on red is 70%.
#   Exhaustion - There's a 2nd element to the bar, Exhaustion. As the player's play their endurance/energy meter depletes.
#   When it hits critical levels, the player starts to become exhausted.
#   Exhaustion is represented by the exhausted athlete's far edge of the bar moving inward. As it moves inward the GREEN or RED becomes GRAY.
#   The arrow will only slide back and forth between the non-gray area.
#   So if the player has 50% GREEN but becomes exhausted in the second half and the left 20% of the full bar turns gray, the arrrow can only move between the remaining 30% of the player's Green zone and the 50% of the opponents red zone.
#   So a 50/50 match with 20% exhaustion changes the odds to 30/50 or 37.5/62.5 or 25 point spread.
