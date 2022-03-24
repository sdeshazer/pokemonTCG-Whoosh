# Samantha Deshazer
# CS 454 Assignment 4
# Declared data : please refer to CreateSchema class
# the schema is defined there.

# Use double quotes in your queries to use OR search,
# otherwise Whoosh defaults to AND search.

from server_whoosh import MyWhooshSearcher
from PrintResults import printPokemonSearchResults


def main():
    searchObject = MyWhooshSearcher()
    searchObject.index()

    # Queries, searches multiple fields (see schema) and top n results:
    # in this case top 10 results:
    returned_results = searchObject.search('Pikachu', 10)
    printPokemonSearchResults(returned_results)

    returned_results = searchObject.search('Snorlax Rare', 10)
    printPokemonSearchResults(returned_results)

    returned_results = searchObject.search('Secret Rare', 10)
    printPokemonSearchResults(returned_results)

    # OR search uses ""
    # for example: a card cannot be a secret and a promo
    # a card cannot be a common and a promo, promo is just promo
    # but a card can be a secret and a rare.
    returned_results = searchObject.search('"Promo Secret"', 10)
    printPokemonSearchResults(returned_results)

    # there are more commons than rares
    returned_results = searchObject.search('"Common Rare"', 10)
    printPokemonSearchResults(returned_results)

    returned_results = searchObject.search('Gengar rare', 10)
    printPokemonSearchResults(returned_results)

    # a good example of OR and AND :
    print("AND SEARCH:")
    returned_results = searchObject.search('Pikachu promo', 10)
    printPokemonSearchResults(returned_results)

    print("OR SEARCH:")
    returned_results = searchObject.search('"Pikachu promo"', 10)
    printPokemonSearchResults(returned_results)


if __name__ == '__main__':
    main()
