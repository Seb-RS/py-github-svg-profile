class Color:
    @staticmethod
    def darken(hex_color, factor=0.7):
        hex_color = hex_color.lstrip("#")
        rgb = [int(hex_color[i : i + 2], 16) for i in (0, 2, 4)]
        darkened_rgb = [int(component * factor) for component in rgb]
        darkened_hex = "#{:02x}{:02x}{:02x}".format(*darkened_rgb)
        return darkened_hex