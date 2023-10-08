"""
Find Winner Of Election

Given a list of votes, containing names of candidates in an election,
find which candidate received maximum number of votes.

If two or more candidate got the same number of votes, return the lexicographically smaller name.

Example:
        Input => "votes": ["sam", "john", "jamie", "sam"]
        Output => "sam"

        Input => "votes": ["sam", "john", "sam", "john"]
        Output => "john"
"""


def find_winner_of_election_brute_force(votes: list[str]) -> str:
    vote_dict = dict()
    for vote in votes:
        if vote in vote_dict.keys():
            vote_dict[vote] += 1
        else:
            vote_dict[vote] = 1

    max_vote = 0
    winner = list()
    for candidate, number_of_votes in vote_dict.items():
        if number_of_votes > max_vote:
            winner.clear()
            max_vote = number_of_votes
            winner.append(candidate)
        elif number_of_votes == max_vote:
            winner.append(candidate)

    winner.sort()
    return winner[0] if len(winner) > 0 else ""


def find_winner_of_election_efficient_brute_force(votes: list[str]) -> str:
    vote_dict = dict()
    for vote in votes:
        if vote in vote_dict.keys():
            vote_dict[vote] += 1
        else:
            vote_dict[vote] = 1

    sorted_vote_dict = dict(sorted(vote_dict.items(), key=lambda x: x[1], reverse=True))
    max_vote = list(sorted_vote_dict.values())[0] if len(sorted_vote_dict) > 0 else 0
    max_votes_dict = dict(filter(lambda x: x[1] == max_vote, sorted_vote_dict.items()))
    winners = sorted(list(max_votes_dict.keys()))
    return winners[0] if len(winners) > 0 else ""
