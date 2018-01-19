import heapq

def stallselection():
    N, K = map(int, input().split())
    sequence_queue = [-N] # sequence represents continguous unoccupied stalls
    freestall_sequences = {N : 1}
    while True:
        sequence = -heapq.heappop(sequence_queue)  # taking the next sequence
        sequence_frequency = freestall_sequences[sequence]
        left_sequence = (sequence + 1)//2 - 1
        right_sequence = sequence - 1 - left_sequence
            
        if K <= sequence_frequency:
            return "{} {}".format(right_sequence,left_sequence)
        else:
            K -= sequence_frequency
            for s in [right_sequence, left_sequence]:
                if s not in freestall_sequences:
                    freestall_sequences[s] = 0
                    heapq.heappush(sequence_queue, -s)
                freestall_sequences[s] += sequence_frequency

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, stallselection()))
