
def best_score(a_dictionary):
    for i in a_dictionary:
        if not i:
            return None
        else:
            ans = a_dictionary[[0]]
            if a_dictionary[i] > a_dictionary[ans]:
                a_dictionary[ans] = a_dictionary[i]
    return ans


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))


