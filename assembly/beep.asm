extern _MessageBeep@16

    global _main

        section .data
            uint db "0x00000000L", 0

        section .text
            _main:
                mov ebx, uint
                push ebx
                call _MessageBeep@16