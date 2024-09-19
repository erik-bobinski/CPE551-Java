a = 0b11001010

output = 0

for i in range(8):
    print(f"a: {a:08b}")
    print(f"b: {output:08b}")
    current_bit = a & 1 # AND the input with the mask
    output = output << 1 # shift output left by 1
    output = output | current_bit # bitwise or
    a = a >> 1 # shift off whatever the rightmost bit is, effectively deleting it
print(f"output: {output:08b}") # final output
