; see a list here for shutdown types
; https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-exitwindowsex#parameters

; extern _ExitWindowsEx@16

; global _main:

;     section .data
;         msg: db "You're pc is about to restart", 0

;     section .text
;         _main:

;             mov ebx, 0x00400000
;             push ebx
;             push ebx
;             call _ExitWindowsEx@16




            
extern _InitiateSystemShutdownA@16

global _main:

    section .data
        msg: db "Bye-Bye", 0

    section .text
        _main:

            xor ebx, ebx
            push ebx ; reboot => FALSE

            mov ebx, 1
            push ebx ; ForceAppsClosed => FALSE

            mov ebx, 5
            push ebx ; Timeout => 5

            mov ebx, msg
            push ebx ; Message => msg
            
            xor ebx, ebx
            push ebx ; MachineName => NULL

            call _InitiateSystemShutdownA@16