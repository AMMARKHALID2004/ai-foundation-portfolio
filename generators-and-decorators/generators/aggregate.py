import source,filter,transformer
def count_words(parsed):
    count=0
    for _ in parsed:
        count=count+1
    return count

lines = source.read_large_file("Projects/file.txt")
filtered = filter.filter_lines(lines, filter.predicate)
parsed = transformer.parse_lines(filtered)

print(count_words(parsed))