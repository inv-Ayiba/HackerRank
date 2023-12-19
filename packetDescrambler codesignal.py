#tryna understand this one
def count_characters(seq, fragmentData):
    idx_to_chars = {}
    for idx, char in enumerate(fragmentData):
        if seq[idx] not in idx_to_chars:
            idx_to_chars[seq[idx]] = {char: 1}
        else:
            if char not in idx_to_chars[seq[idx]]:
                idx_to_chars[seq[idx]][char] = 1
            else:
                idx_to_chars[seq[idx]][char] += 1
    return idx_to_chars

def check_gaps(idx_to_chars, max_seq_idx):
    if len(idx_to_chars) < max_seq_idx + 1:
        return True
    return False

def check_start_with_hash(data1):
    if len(data1) > 1 and data1[0] == '#':
        return True
    return False

def reconstruct_message(idx_to_chars, max_seq_idx, n):
    output = [0] * (max_seq_idx + 1)

    for seq_idx, char_map in idx_to_chars.items():
        if char_map is None:
            return ""

        for char, count in char_map.items():
            if count > n / 2:
                if seq_idx == max_seq_idx and char != "#":
                    return ""
                elif seq_idx < max_seq_idx and char == "#":
                    return ""
                else:
                    output[seq_idx] = ord(char)

        if output[seq_idx] == 0:
            return ""

    return "".join(chr(char) for char in output)

def solution(seq, fragmentData, n):
    max_seq_idx = max(seq)
    idx_to_chars = count_characters(seq, fragmentData)

    if check_gaps(idx_to_chars, max_seq_idx):
        return ""

    result = reconstruct_message(idx_to_chars, max_seq_idx, n)

    if check_start_with_hash(result):
        return ""
    
    return result
