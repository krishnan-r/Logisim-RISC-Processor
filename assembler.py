#!/usr/bin/python
"""
Assembler Program to convert highlevel assembly language into 
machine instruction of a simulated 32-Bit RISC Processor

Usage: python thisfile.py inputfilename outputfilename
"""
import sys

try:
    input_filename = sys.argv[1]
except IndexError:
    print('Usage: command inputfile outputfile \n\r')
    sys.exit()

try:
    output_filename = sys.argv[2]
except IndexError:
    output_filename = 'out.img'
    
op_codes = {
'halt'  :   '00000',
'load'  :   '00001',
'store' :   '00010',
'mov'  :   '00011',
'jmp'   :   '00100',
'jz'    :   '00101',
'jc'    :   '00110',
'nop'   :   '00111',
'add'   :   '01000',
'sub'   :   '01001',
'and'   :   '01010',
'or'    :   '01011',
'not'   :   '01100',
'xor'   :   '01101',
'rnd'   :   '01110',
'cmp'   :   '01111'
#Immediate Instructions   
}

def reg(code):
    """Converts ri into binary string."""
    if(code[0]!='r'): raise Exception('Not a register')
    rno = int(code[1:])
    if(rno < 0 or rno >=32): raise Exception('Only 32 Registers, but given: '+code+' '+rno )
    return '{:05b}'.format(rno)
def getImmediate(token):
    """Returns formatted binary string from input token of immediate value."""
    base=10
    if(token[:2]=='0x'): base=16
    elif(token[:2]=='0b'): base=2
    val=int(token,base)
    return '{:016b}'.format(val)

def convert_line(line):
    """Converts one line of assembly into a machine instruction"""
    if(line.find('#')>=0): line=line[:line.index('#')] #Ignore comments.
    line=line.strip().lower()
    tokens=line.split()
    op=tokens[0]
    immediate=False
    
    if(op[-1]=='i'):
        immediate=True
        op=op[:-1]
        
    if(not op in op_codes): raise Exception('Invalid Operation')    
    
    imm = '1' if immediate else '0'
    ra='00000'
    rb='00000'
    rc='00000'
    ending='0000000000000000' # 16bit
    empty='00000000000' #11 bit
    
    if(op in ['halt','nop']):
        pass
    
    elif immediate:
        if(op in ['not','rnd','store']): # Instructions of the form op RA Immediate
            raise Exception('Operation does not support Immediate Mode')
        elif(op in ['jump','jz','jc']): # Instructions of the form op RA Immediate
            ending=getImmediate(tokens[1])
        elif(op in ['add','sub','and','or','xor']):
            rc=reg(tokens[1])
            ra=reg(tokens[2])
            ending=getImmediate(tokens[3])
        elif(op in ['mov','load']):
            rc=reg(tokens[1])
            ending=getImmediate(tokens[2])
        elif(op in ['cmp']):
            ra=reg(tokens[1])
            ending=getImmediate(tokens[2])
            
    else:
        
        if(op in ['jump','jz','jc']): # Instructions of the form op RA Immediate
            rb=reg(tokens[1])
        elif(op in ['add','sub','and','or','xor']):
            rc=reg(tokens[1])
            ra=reg(tokens[2])
            rb=reg(tokens[3])
        elif(op in ['mov','not']):
            rc=reg(tokens[1])
            rb=reg(tokens[2])
        elif(op in ['cmp']):
            ra=reg(tokens[1])
            rb=reg(tokens[2])
        elif(op in ['store']):
            ra=reg(tokens[2])
            rb=reg(tokens[1])
        elif(op in ['rnd']):
            rc=reg(tokens[1])
        elif(op in ['load']):
            rc=reg(tokens[1])
            rb=reg(tokens[2])
        ending=rb+empty
        
    binary_opcode = op_codes[op]+ra+rc+ending+imm
    if(len(binary_opcode)!=32): raise Exception('Parse Error - Instruction smaller than 32bit')
    return '%08X' % int(binary_opcode, 2)



print('Starting assembling....'+input_filename+ ' '+ output_filename +'\n')
input = open(input_filename)
output = open(output_filename, mode='w')

output.write('v2.0 raw\n')
for line in input:
    if(len(line.strip())>0): 
        if(line.strip()[0]=='#'): continue
        binary=convert_line(line)
        output.write(binary+'\n')
        print(binary)

input.close()
output.close()