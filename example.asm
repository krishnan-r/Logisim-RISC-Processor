# Example Assembler Program to Sum 1 to f
movi r1 0x0
movi r2 0xf
subi r2 r2 0x1
add r1 r1 r2
cmpi r2 0x1
jci 0x2
halt