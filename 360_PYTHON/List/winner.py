votes = [340, 270, 340, 200]
max_vote = max(votes)
winners = [i for i, v in enumerate(votes) if v == max_vote]

if len(winners) > 1:
    print("Tie between:", winners)
else:
    print("Winner:", winners[0])
