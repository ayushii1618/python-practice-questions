def parse_csv(filename):
    with open(filename, 'r') as f:
        return [line.strip().split(',') for line in f.readlines()]

# Example (Assumes CSV file present)
# print(parse_csv("data.csv"))
