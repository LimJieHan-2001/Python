import matplotlib.pyplot as plt

def scan_algorithm(requests, head, direction, disk_size=200):
    requests.sort()
    left = [r for r in requests if r <= head]
    right = [r for r in requests if r > head]

    if direction == "left":
        sequence = left[::-1] + [0] + right
    else:
        sequence = right + [disk_size - 1] + left[::-1]
    
    return sequence

def plot_sequence(sequence, initial_head):
    plt.figure(figsize=(10, 5))
    plt.plot(sequence, marker='o')
    plt.axhline(initial_head, color='red', linestyle='--', label='Initial Head Position')
    plt.title("SCAN Disk Scheduling")
    plt.xlabel("Sequence")
    plt.ylabel("Track Number")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
requests = [55, 58, 39, 18, 90, 160, 150, 38, 184]
initial_head = 50
direction = "right"
sequence = scan_algorithm(requests, initial_head, direction)
plot_sequence(sequence, initial_head)
