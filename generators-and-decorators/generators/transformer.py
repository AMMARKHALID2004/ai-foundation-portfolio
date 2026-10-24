import source
import filter

def parse_lines(lines):
    for line in lines:
        print("[transformer testing]")
        yield line.split()

lines = source.read_large_file("Projects/file.txt")
filtered = filter.filter_lines(lines, filter.predicate)
parsed = parse_lines(filtered)

print(next(parsed))
print(next(parsed))
print(next(parsed))
print(next(parsed))
print(next(parsed))
print(next(parsed))