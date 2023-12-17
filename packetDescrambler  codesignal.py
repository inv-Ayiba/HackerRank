#( 1:45:05 )
def solution(seq, fragmentData, n):
    MAX_SEQ = 25000
    fragments = {}
    print("seq: ",seq,"fragmentData: ",fragmentData,"n: ",n)
    # Store fragments in a dictionary based on sequential number
    for i in range(len(seq)):
        currentSeq = seq[i]
        currentData = fragmentData[i]
        if currentSeq not in fragments:
            fragments[currentSeq] = []

        fragments[currentSeq].append(currentData)
        print("fragment",fragments)
        

    result = find_max_elements(fragments)
    myKeys=get_keys_as_list(result)
    myKeys.sort()
    data=''.join(get_values_by_keys(result,myKeys))
    print(result,myKeys,data)
    data1=''
    plug=get_max_element_counts3(fragments)
    for i in data:
        if(plug[i]/n>0.5):
            data1+=i
            print("plug[i]/n",plug[i]/n,"plug[i]: ",plug[i],"data1",data1)
    try:
        if('#'==data1[len(data1)-1] and '#'!=data1[0]):
            return data1
        else:
            return ""
    except(IndexError):
        return("")
    
    
    # result=[]
    # # Iterate through sequences
    # for i in range(MAX_SEQ):
    #     # Check if the sequential number is present in fragments
    #     if i in fragments:
    #         # Count occurrences of characters in the fragments
    #         counts = {}
    #         for char in fragments[i]:
    #             counts[char] = counts.get(char, 0) + 1

    #         # Check for more than 50% occurrence of characters (excluding '#')
    #         candidate_char = ''
    #         for char, count in counts.items():
    #             if char != '#' and count > n / 2:
    #                 candidate_char = char

    #         # Choose the character that is closer to the end of the fragments
    #         if candidate_char:
    #             result.append(candidate_char)

    # # Append '#' to the result only if it is non-empty
    # if result:
    #     result.append('#')

    # return ''.join(result)

def find_max_elements(dictionary):
    result = {}

    for key, elements in dictionary.items():
        counts = {}

        # Count occurrences of elements
        for element in elements:
            counts[element] = counts.get(element, 0) + 1

        # Find element with the maximum count
        max_element = max(counts, key=counts.get)
        result[key] = max_element

    return result

# Example usage
fragment_dict = {1: ['+', '+'], 2: ['A', 'A', 'B'], 0: ['#', '#', '#']}
max_elements = find_max_elements(fragment_dict)

# print("ppppppp",max_elements)

def get_keys_as_list(dictionary):
    return list(dictionary.keys())
def get_values_by_keys(dictionary, keys_list):
    return [dictionary[key] for key in keys_list if key in dictionary]

# Example usage
fragment_dict = {1: ['+', '+'], 2: ['A', 'A', 'B'], 0: ['#', '#', '#']}
keys_list = get_keys_as_list(fragment_dict)

# print("lllppp",keys_list)

def get_max_element_counts(dictionary):
    result = {}

    for key, elements in dictionary.items():
        counts = {}

        # Count occurrences of elements
        for element in elements:
            counts[element] = counts.get(element, 0) + 1

        # Find the maximum count
        max_count = max(counts.values())

        # Get elements with the maximum count
        max_elements = [element for element, count in counts.items() if count == max_count]

        result[key] = {element: max_count for element in max_elements}

    return result

# Example usage
fragment_dict = {1: ['+', '+'], 2: ['A', 'A', 'B'], 0: ['#', '#', '#']}
max_element_counts = get_max_element_counts(fragment_dict)
print(max_element_counts)#{1: {'+': 2}, 2: {'A': 2}, 0: {'#': 3}}


def get_max_element_counts1(dictionary):
    result = {}

    for key, elements in dictionary.items():
        counts = {}

        # Count occurrences of elements
        for element in elements:
            counts[element] = counts.get(element, 0) + 1

        # Find the maximum count
        max_count = max(counts.values())

        result[key] = max_count

    return result

# Example usage
fragment_dict = {1: ['+', '+'], 2: ['A', 'A', 'B'], 0: ['#', '#', '#']}
max_element_counts1 = get_max_element_counts1(fragment_dict)

print(max_element_counts1)#The output of this example would be {1: 2, 2: 2, 0: 3} based on the provided fragment_dict.

def get_max_element_counts3(dictionary):
    counts = {}

    for elements in dictionary.values():
        # Count occurrences of elements
        for element in set(elements):
            counts[element] = max(counts.get(element, 0), elements.count(element))

    return counts

# Example usage
# fragment_dict = {1: ['+', '+'], 2: ['A', 'A', 'B'], 0: ['#', '#', '#']}
# max_element_counts = get_max_element_counts3(fragment_dict)

# print(max_element_counts)
