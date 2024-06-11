import fileinput
from collections import defaultdict


def contain_shiny_gold(instructions):
    graph = defaultdict(set)
    bag_colors = set()
    for instruction in instructions:
        label, bags = parse_instruction(instruction)
        graph[label] = bags
    for node in list(graph.keys()):
        print("node", node)
        if dfs(graph, node) and node != ('shiny', 'gold'):
            print("count")
            bag_colors.add(node)
    print(bag_colors)
    return len(bag_colors)

def dfs(graph, node):
    if node == ('shiny', 'gold'):
        print('shinygold')
        return True
    for n in graph[node]:
        if dfs(graph, n[0]):
            return True
    return False

def parse_instruction(line):
    bags = []
    line = line.strip()
    left, right = line.split(' contain ')
    left_parts = [part for part in left.split(' ')]
    content = right.split(',')
    for parts in content:
        parts = parts.strip()
        right_parts = [part for part in parts.split(' ')]
        bags.append([(right_parts[1], right_parts[2]), right_parts[0]])
    return (left_parts[0], left_parts[1]), bags

INSTRUCTIONS = [i.strip() for i in fileinput.input()]

print(f"Number of bag colors that can contain at least on shiny bag: {contain_shiny_gold(INSTRUCTIONS)}")
