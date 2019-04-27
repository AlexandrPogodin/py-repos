with open('dataset.txt', 'r') as infile:
    for line in infile:
        line.append(line.strip())
print(line)