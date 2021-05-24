def decideReward(points):
    if not(isinstance(points, int)):
        decision = "invalid"
        print("Invalid input! You should provide an integer!")
        return decision
    if points < 0:
        decision = "invalid"
        print("Invalid input! You should provide a non-negative integer!")
        return decision
    if points < 350:
        decision = "no rewards"
    else:
        if points < 950:
            decision = "coffee"
        else:
            if points < 3000:
                decision = "coffee and cake"
            else:
                if points <= 5000:
                    decision = "coffee, cake and sandwich"
                else:
                    decision = "unable to earn > 5000"
    print("The reward is: " + decision)
    return decision