
hex_to_int_lookup = {
    '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15
}
def hex1_to_int(hex:str):
    hex = hex.upper()
    return hex_to_int_lookup[hex]
def generate_hex3_spectrum(hex3_0:str, hex3_1:str):
    hex3_0, hex3_1 = hex3_0[1:], hex3_1[1:]
    hex0 = (hex1_to_int(hex3_0[0]), hex1_to_int(hex3_0[1]), hex1_to_int(hex3_0[2]))
    hex1 = (hex1_to_int(hex3_1[0]), hex1_to_int(hex3_1[1]), hex1_to_int(hex3_1[2]))

    sample_count = min(abs(hex1[0]-hex0[0]), abs(hex1[1]-hex0[1]), abs(hex1[1]-hex0[1]))
    spectrum = []
    for i in range(1, sample_count):
        new_hex3 = str(hex0[0]+i) +str(hex0[1]+i) +str(hex0[2]+i)
        spectrum.append(new_hex3)

    return spectrum

    

class Theme:
    def __init__(self, id:str, bg_color:str, fg_color:str, text_color:str):
        self.id = id
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text_color = text_color
        self.color_spectrum = None

        color_spectrum = generate_hex3_spectrum(bg_color, fg_color)
        print(color_spectrum)
        self.color_spectrum = color_spectrum
