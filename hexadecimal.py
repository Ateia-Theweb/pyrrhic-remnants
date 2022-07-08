def row(intaddress, bytesread, /):
    """Left and center (1)"""
    return (
            f'{intaddress:08X}'

            ' '
            +
            ' '.join(f'{i:02X}' for i in bytesread)
    )
