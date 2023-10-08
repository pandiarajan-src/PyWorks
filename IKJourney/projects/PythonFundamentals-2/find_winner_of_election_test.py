import unittest
from find_winner_of_election import find_winner_of_election_brute_force, \
    find_winner_of_election_efficient_brute_force


class TestFindWinnerOfElection(unittest.TestCase):
    def test_find_winner_of_election_brute_force(self):
        self.assertEqual(find_winner_of_election_brute_force(["sam", "john", "jamie", "sam"]), "sam")
        self.assertEqual(find_winner_of_election_brute_force(["sam", "john", "sam", "john"]), "john")
        self.assertEqual(find_winner_of_election_brute_force(["sam"]), "sam")
        self.assertEqual(find_winner_of_election_brute_force(["sam", "sam"]), "sam")
        self.assertEqual(find_winner_of_election_brute_force(["sam", "jamie", "sam", "aon"]), "sam")

    def test_find_winner_of_election_efficient_brute_force(self):
        self.assertEqual(find_winner_of_election_efficient_brute_force(["sam", "john", "jamie", "sam"]), "sam")
        self.assertEqual(find_winner_of_election_efficient_brute_force(["sam", "john", "sam", "john"]), "john")
        self.assertEqual(find_winner_of_election_efficient_brute_force(["sam"]), "sam")
        self.assertEqual(find_winner_of_election_efficient_brute_force(["sam", "sam"]), "sam")
        self.assertEqual(find_winner_of_election_efficient_brute_force(["sam", "jamie", "sam", "aon"]), "sam")


if __name__ == '__main__':
    unittest.main()
