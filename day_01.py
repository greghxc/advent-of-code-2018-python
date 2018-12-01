def part_one(int_list):
  return sum(int_list)

def part_two(int_list):
  seen_vals = { 0 }
  (i, agg) = 0, 0
  while (True):
    agg += int_list[i % len(int_list)]
    if agg in seen_vals:
      return agg
    seen_vals.add(agg)
    i += 1

if __name__ == "__main__":
  with open('day01.txt') as file:
    int_list = [int(i) for i in file]
    print(f'Part One: { part_one(int_list) }')
    print(f'Part Two: { part_two(int_list) }')