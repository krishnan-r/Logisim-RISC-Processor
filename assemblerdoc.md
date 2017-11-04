# Assembler Documentation
## Assembling Programs
1. To run programs on the processor, first assemble the memory image.
```
python assembler.py inputfilename [outputfilename]
```
2. Load the memory image inside logism by right clicking on the RAM module and selecting `Load Image...`  
- The programs are loaded at starting address 0x0000
- Each instruction in the assembly language takes up one memory word of 32-bit.
## Assembler Language Commands
### Comments
Comments start with `#`. Any content after a `#` is ignored.
```
# This is a comment.
```
### Halt  
Halts the processor. To resume click the reset button.
```
halt
```

### Load  
Loads value from memory.
```
load [Destination] [Source]
load r3 r2

loadi [Destination] Immediate
loadi r3 0xabcd
```

### Store
Store a value into memory.
```
store [Data] [Address]
store r3 r2
```


### Mov  
Move data from one register to another.
```
mov [Destination] [Source]
mov r3 r2

movi [Destination] ImmediateValue
movi r3 0xabcd
```


### Jump  
Jump to particular address. 
```
jmp [Register with address]
jmp r5

jmpi ImmediateAddress
jmpi 0xabcd
```


### Jump if Zero  
Jump to particular address if zero flag is set.
```
jz [Register with address]
jz r6

jzi ImmediateAddress
jzi 0xabcd
```

### Jump if Carry  
Jump to particular address if carry flag is set.
```
jc [Register with address]
jc r7

jci ImmediateAddress
jci 0xabcd
```
### Nop  
Do Nothing
```
nop
```

### Add, Subtract, And, Or, XOR
Perform the arithmetic opration and store result to destination register

```
op [destination] [source1] [source2]

add r3 r1 r2 
sub r3 r1 r2
and r3 r1 r2
or  r3 r1 r2
xor r3 r1 r2

opi [destination] [source1] Immediate Value
subi r3 r1 0x12de
andi r3 r1 0x12de
ori  r3 r1 0x12de
xori r3 r1 0x12de
```

### Not
Invert bits and store to destination register.
```
not [destination] [source]
```

### Rnd
Generate a random number and store it to destination register
```
rnd [destination]
rnd r1
```

### Cmp
Compares two values and sets flag register. 
```
If Source1 > Source2 then Carry flag is set.
If Source1 == Source2 then Zero flag is set.
```
```
cmp [source1] [source2]
cmp r1 r2

cmpi [source1] [source2]
cmpi r1 0xffff
```