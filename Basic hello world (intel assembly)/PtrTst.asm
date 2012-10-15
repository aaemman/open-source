;
;	SYSC2001 Lab1
;	Printing ASCII Strings
;
; This first statement defines a data variable and initializes it
; The variable has a symbolic address, a qualifier ('db) and a value.
;
; 'db' means 'define byte' and normally can contain one byte only.
; The value of this byte can be an 8-bit number or a string
; We can also use the qualifier 'dw' to reserve and initialize a 16-bit word
;
Message: db'Hello$'	; note '$' at end of string
Message2: db'World$'
;
;	This program calls a subroutine to print a text message
;
Start:
;	
	mov ax, message
	call PrtStr
	

	mov ax, message2	
	call PrtStr
	hlt			; done!
;
;	Insert your PrtStr subroutine here
;
	Display	EQU 04E9h	; address of Virgo display
	
	PrtStr:
		push dx		; save contents of DX register
		push bx		; save contents of other register(s) you use	
	
		mov dx, Display
		mov bx, ax

	PrtChar:

		mov al,[bx]

		cmp al,'$'	; is the character a '$' ?
		jz EndPrt	; if so, we are done

		out [dx],al	; print the char
		inc bx		; step along the string to the next character

		jmp PrtChar	; loop back

	

	EndPrt:
		mov al, 0Dh
		out [dx], al
		mov al, 0Ah
		out [dx], al
		pop bx		; restore contents of registers
		pop dx
		ret		; return to calling program

		
;
;
; This final statement is always required and tells the assembler 2 things
;  1) It's the end of the program listing and
;  2) The entry point of the program is the Symbol 'Start' (in this case)
; Note that the symbol 'Start' appears at the beginning of the program
;
END	Start