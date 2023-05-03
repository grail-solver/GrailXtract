from xtractor.core.helper import grail_extractor

problem = """
A farmer has $1000. With the $1000, he wishes to buy 100 animals of different species: 
chicks, pigs, and cows. It is assumed that a chick costs $5, a pig costs $50, and a cow 
costs $100. He wants to have at least 1 animal of each species and wants to spend all of 
the $1000 he has. How many chicks, pigs, and cows should he buy?
"""

if __name__ == '__main__':
    output = grail_extractor(problem)
    print(output)
