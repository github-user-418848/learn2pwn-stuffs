extern _MessageBoxA@16

global _main

    section .data
        msg: db "Body Message", 0
        ttl: db "Message Title", 0

    section .text
        _main:

            xor ebx, ebx
            push ebx

            mov ebx, msg
            push ebx

            mov ebx, ttl
            push ebx

            xor ebx, ebx
            push ebx

            call _MessageBoxA@16