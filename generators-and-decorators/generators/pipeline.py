import source,transformer,filter
import sys


lines = source.read_large_file("Projects/file.txt")
filtered = filter.filter_lines(lines, filter.predicate)
parsed = transformer.parse_lines(filtered)

# Testing the pipeline
# for item in parsed:
#     print(f"[main] got: {item}")
#     print("---")

filtered_expression=(i for i in lines if filter.predicate(i))

print(next(filtered_expression))
print(next(filtered_expression))



print(sys.getsizeof(filtered_expression))
print(sys.getsizeof(filter.filter_lines(lines, filter.predicate)))