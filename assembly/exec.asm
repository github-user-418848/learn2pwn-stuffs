; KERNEL32 address in memory: 0x758B0000
; ExitProcess address in memory is: 0x758D8630
; WinExec address in memory is: 0x7590F740


section .data

section .bss

section .text

    global _main
    
    _main:
        xor ecx, ecx
        push ecx
        push 0x6578652e
        push 0x636c6163

        mov eax, esp
        
        inc ecx
        push ecx
        push eax
        mov ebx, 0x7590F740
        call ebx

        xor eax, eax
        push eax
        mov eax, 0x758D8630
        jmp eax