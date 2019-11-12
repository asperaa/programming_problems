"""Buy sell cooldown for stock with cooldown
 State Machine Explaination. 
I give you a "like" because it does help to understand more than s0,s1,s2, especially you mention "CAN sell", "CAN buy." However, I disagree with your explanation, and I would like to mention it because your explanation can cause misunderstanding of what state actually present and I think it is important because state-action is the core of the state machine algorithm.

my clarification:
[1] a bit about state machine: state machine captures the current states and their relationships between previous states and current state through action.
So, the state should be understood as the consequence of our previous actions, and what action we can do at current state.

s0:
[Consequence] State not immediate after selling; Doesn't have any stock;
[Action can take] Buy a new stock / Continue to take a rest

s1:
[Consequence] State with stock in hand;
[Action can take] Sell a stock / Continue to take a rest

s2:
[Consequence] State immediate after selling; Doesn't have any stock (since just sell one to enter this state)
[Action can take] Enters next state by taking a rest (since s2 is only for state immediate after selling, we cannot stay here.)

"""

def buy_sell(prices):
    length = len(prices)
    if length <= 1:
        return 0
    state_a = [0]*length
    state_b = [0]*length
    state_c = [0]*length

    state_a[0] = 0
    state_b[0] = -prices[0]
    state_c[0] = float('-inf')

    for i in range(1, length):
        state_a[i] = max(state_a[i-1], state_c[i-1])
        state_b[i] = max(state_b[i-1], state_a[i-1]-prices[i])
        state_c[i] = state_b[i-1] + prices[i]
    return max(state_a[-1], state_c[-1])


if __name__ == "__main__":
    # prices = [1, 2, 3, 0, 2]
    prices = [0, 1, 2, 5, 9, 11, 1, 3]
    print(buy_sell(prices))
