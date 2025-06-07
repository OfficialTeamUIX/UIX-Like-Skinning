import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from tkinter import ttk
import configparser
import re
# This is in-progress, and some of these may not even be used.
# The goal is to allow editing of the UIX skin INI file, which is used by Rocky's Xbox Colourizer Python script.
DEFAULTS = {
    "pulse_highlight": "B2D000",
    "pulsing_selection": "FFFF80",
    "egg_button_press": "FEFFBC",
    "kb_button_focus": "B2D000",
    "kb_button_focus_highlight": "FFB2D000",
    "kb_button_large_no_focus_highlight": "FFF3FF6B",
    "kb_button_large_no_focus": "19E100",
    "kb_button_no_focus_highlight": "DEF3FF6B",
    "kb_button_no_focus": "14C000",
    "kb_letters_no_focus": "BEFA5E",
    "innerwall_01_transition": "FFF3FF6B",
    "innerwall_01": "1428D414",
    "innerwall_02": "1414C000",
    "material_#1334": "FF0B2000",
    "xboxgreendark": "FF062100",
    "egg_xboxgreen_sub": "8CC919",
    "xboxgreen2": "8BC818",
    "gamehilite33": "DDD078",
    "nothing": "808080",
    "navtype": "BEFA5E",
    "orangenavtype": "F99819",
    "egg_xboxgreen": "8BC818",
    "type": "64C819",
    "typesdsafsda": "FFFFFF",
    "material_#1335": "FF4CA200",
    "material_#133511": "FF295700",
    "hilightedtype": "FF032C00",
    "xboxgreenq": "8BC818",
    "cellegg_partsw": "4DE039",
    "material_#108": "FFA0FC00",
    "itemstype": "B6F560",
    "gamehilitememory": "FFB2D000",
    "white": "FFFFFF",
    "solid_green_1": "11FF22",
    "solid_green_2": "12C10A",
    "solid_green_3": "0A751C",
    "solid_green_4": "FF123700",
    "dark_green_panels": "FF092900",
    "flatsurfaces_highlights": "C0F3FF6B",
    "flatsurfaces_back": "14C000",
    "flatsurfacesselected": "801EFF00",
    "flatsurfacesmemory": "801EA000",
    "darksurfaces": "5ACBCD55",
    "dark_green_panels_falloff": "FF052305",
    "grey_1": "475345",
    "grey_2": "FF566452",
    "grill_grey_1": "202020",
    "grill_grey_2": "FF404040",
    "wireframe_1": "00000003",
    "wireframe_2": "647DC622",
    "wireframe_3": "7DC622",
    "tubes_1": "D7F2FA99",
    "tubes_2": "25076800",
    "memoryheader": "7A3CC643",
    "memoryheaderhilite_1": "F0C7E800",
    "memoryheaderhilite_2": "82617200",
    "eggglow_1": "E4FEFFBC",
    "eggglow_2": "FCFF00",
    "gradient_1": "33BFFF6B",
    "gradient_2": "00FF12",
    "cellegg_parts_1": "B2F3FF6B",
    "cellegg_parts_2": "1EFF00",
    "flatsurfaces2sided3_1": "FFFD1E00",
    "flatsurfaces2sided3_2": "F21C00",
    "console_hilite_1": "FFFFAD6B",
    "console_hilite_2": "F6FF00",
    "metal_chrome_1": "E5E5E5",
    "metal_chrome_2": "FFE5E5E5",
    "panelbacking_01": "FF041400",
    "panelbacking_03": "FF041400",
    "panelbacking_04": "0E2E07",
    "darkenbacking": "FF041400",
    "button": "9D6DC2",
    "image": "FF041400",
    "live_header": "FF041400",
    "highlight": "9D6DC2",
    "footer": "9D6DC2",
    "livechrome": "9D6DC2",
    "gamehilite": "FFFFFF",
    "panelbacking": "FF041400",
}
COLOR_TYPES = {
    "pulse_highlight": "RGB",
    "pulsing_selection": "RGB",
    "egg_button_press": "RGB",
    "kb_button_focus": "RGB",
    "kb_button_focus_highlight": "ARGB",
    "kb_button_large_no_focus_highlight": "ARGB",
    "kb_button_large_no_focus": "RGB",
    "kb_button_no_focus_highlight": "ARGB",
    "kb_button_no_focus": "RGB",
    "kb_letters_no_focus": "RGB",
    "innerwall_01_transition": "ARGB",
    "innerwall_01": "ARGB",
    "innerwall_02": "ARGB",
    "material_#1334": "ARGB",
    "xboxgreendark": "ARGB",
    "egg_xboxgreen_sub": "RGB",
    "xboxgreen2": "RGB",
    "gamehilite33": "RGB",
    "nothing": "RGB",
    "navtype": "RGB",
    "orangenavtype": "RGB",
    "egg_xboxgreen": "RGB",
    "type": "RGB",
    "typesdsafsda": "RGB",
    "material_#1335": "ARGB",
    "material_#133511": "ARGB",
    "hilightedtype": "ARGB",
    "xboxgreenq": "RGB",
    "cellegg_partsw": "RGB",
    "material_#108": "ARGB",
    "itemstype": "RGB",
    "gamehilitememory": "ARGB",
    "white": "RGB",
    "solid_green_1": "RGB",
    "solid_green_2": "RGB",
    "solid_green_3": "RGB",
    "solid_green_4": "ARGB",
    "dark_green_panels": "ARGB",
    "flatsurfaces_highlights": "ARGB",
    "flatsurfaces_back": "RGB",
    "flatsurfacesselected": "ARGB",
    "flatsurfacesmemory": "ARGB",
    "darksurfaces": "ARGB",
    "dark_green_panels_falloff": "ARGB",
    "grey_1": "RGB",
    "grey_2": "ARGB",
    "grill_grey_1": "RGB",
    "grill_grey_2": "ARGB",
    "wireframe_1": "ARGB",
    "wireframe_2": "ARGB",
    "wireframe_3": "RGB",
    "tubes_1": "ARGB",
    "tubes_2": "ARGB",
    "memoryheader": "ARGB",
    "memoryheaderhilite_1": "ARGB",
    "memoryheaderhilite_2": "ARGB",
    "eggglow_1": "ARGB",
    "eggglow_2": "RGB",
    "gradient_1": "ARGB",
    "gradient_2": "RGB",
    "cellegg_parts_1": "ARGB",
    "cellegg_parts_2": "RGB",
    "flatsurfaces2sided3_1": "ARGB",
    "flatsurfaces2sided3_2": "ARGB",
    "console_hilite_1": "ARGB",
    "console_hilite_2": "RGB",
    "metal_chrome_1": "RGB",
    "metal_chrome_2": "ARGB",
    "panelbacking_01": "ARGB",
    "panelbacking_03": "ARGB",
    "panelbacking_04": "RGB",
    "darkenbacking": "ARGB",
    "button": "RGB",
    "image": "ARGB",
    "live_header": "ARGB",
    "highlight": "RGB",
    "footer": "RGB",
    "livechrome": "RGB",
    "gamehilite": "RGB",
    "panelbacking": "ARGB"
}
# Define the patch keys with their properties - These should match Rocky's patch keys.
PATCH_KEYS = [
    {'name': 'pulse_highlight', 'patch_type': 0, 'argb': False},
    {'name': 'pulsing_selection', 'patch_type': 0, 'argb': False},
    {'name': 'egg_button_press', 'patch_type': 0, 'argb': False},
    {'name': 'kb_button_focus', 'patch_type': 0, 'argb': False},
    {'name': 'kb_button_focus_highlight', 'patch_type': 0, 'argb': True},
    {'name': 'kb_button_large_no_focus_highlight', 'patch_type': 0, 'argb': True},
    {'name': 'kb_button_large_no_focus', 'patch_type': 0, 'argb': False},
    {'name': 'kb_button_no_focus_highlight', 'patch_type': 0, 'argb': True},
    {'name': 'kb_button_no_focus', 'patch_type': 0, 'argb': False},
    {'name': 'kb_letters_no_focus', 'patch_type': 0, 'argb': False},
    {'name': 'innerwall_01_transition', 'patch_type': 0, 'argb': True},
    {'name': 'innerwall_01', 'patch_type': 0, 'argb': True},
    {'name': 'innerwall_02', 'patch_type': 0, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'material_#1334', 'patch_type': 2, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'xboxgreendark', 'patch_type': 2, 'argb': True},
    {'name': 'egg_xboxgreen_sub', 'patch_type': 1, 'argb': False},
    {'name': 'xboxgreen2', 'patch_type': 1, 'argb': False},
    {'name': 'gamehilite33', 'patch_type': 1, 'argb': False},
    {'name': 'nothing', 'patch_type': 1, 'argb': False},
    {'name': 'navtype', 'patch_type': 1, 'argb': False},
    {'name': 'orangenavtype', 'patch_type': 1, 'argb': False},
    {'name': 'egg_xboxgreen', 'patch_type': 1, 'argb': False},
    {'name': 'type', 'patch_type': 1, 'argb': False},
    {'name': 'typesdsafsda', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'material_#1335', 'patch_type': 2, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'material_#133511', 'patch_type': 2, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'hilightedtype', 'patch_type': 2, 'argb': True},
    {'name': 'xboxgreenq', 'patch_type': 1, 'argb': False},
    {'name': 'cellegg_partsw', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'material_#108', 'patch_type': 2, 'argb': True},
    {'name': 'itemstype', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'gamehilitememory', 'patch_type': 2, 'argb': True},
    {'name': 'white', 'patch_type': 1, 'argb': False},
    {'name': 'solid_green_1', 'patch_type': 1, 'argb': False},
    {'name': 'solid_green_2', 'patch_type': 1, 'argb': False},
    {'name': 'solid_green_3', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'solid_green_4', 'patch_type': 2, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'dark_green_panels', 'patch_type': 2, 'argb': True},
    {'name': 'flatsurfaces_highlights', 'patch_type': 0, 'argb': True},
    {'name': 'flatsurfaces_back', 'patch_type': 0, 'argb': False},
    {'name': 'flatsurfacesselected', 'patch_type': 0, 'argb': True},
    {'name': 'flatsurfacesmemory', 'patch_type': 0, 'argb': True},
    {'name': 'darksurfaces', 'patch_type': 0, 'argb': True},
    {'name': 'dark_green_panels_falloff', 'patch_type': 0, 'argb': True},
    {'name': 'grey_1', 'patch_type': 0, 'argb': False},
    {'name': 'grey_2', 'patch_type': 0, 'argb': True},
    {'name': 'grill_grey_1', 'patch_type': 0, 'argb': False},
    {'name': 'grill_grey_2', 'patch_type': 0, 'argb': True},
    {'name': 'wireframe_1', 'patch_type': 0, 'argb': True},
    {'name': 'wireframe_2', 'patch_type': 0, 'argb': True},
    {'name': 'wireframe_3', 'patch_type': 0, 'argb': False},
    {'name': 'tubes_1', 'patch_type': 0, 'argb': True},
    {'name': 'tubes_2', 'patch_type': 0, 'argb': True},
    {'name': 'memoryheader', 'patch_type': 0, 'argb': True},
    {'name': 'memoryheaderhilite_1', 'patch_type': 0, 'argb': True},
    {'name': 'memoryheaderhilite_2', 'patch_type': 0, 'argb': True},
    {'name': 'eggglow_1', 'patch_type': 0, 'argb': True},
    {'name': 'eggglow_2', 'patch_type': 0, 'argb': False},
    {'name': 'gradient_1', 'patch_type': 0, 'argb': True},
    {'name': 'gradient_2', 'patch_type': 0, 'argb': False},
    {'name': 'cellegg_parts_1', 'patch_type': 0, 'argb': True},
    {'name': 'cellegg_parts_2', 'patch_type': 0, 'argb': False},
    {'name': 'flatsurfaces2sided3_1', 'patch_type': 0, 'argb': True},
    {'name': 'flatsurfaces2sided3_2', 'patch_type': 0, 'argb': False},
    {'name': 'console_hilite_1', 'patch_type': 0, 'argb': True},
    {'name': 'console_hilite_2', 'patch_type': 0, 'argb': False},
    {'name': 'metal_chrome_1', 'patch_type': 0, 'argb': False},
    {'name': 'metal_chrome_2', 'patch_type': 0, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'panelbacking_01', 'patch_type': 2, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'panelbacking_03', 'patch_type': 2, 'argb': True},
    {'name': 'panelbacking_04', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'darkenbacking', 'patch_type': 2, 'argb': True},
    {'name': 'button', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'image', 'patch_type': 2, 'argb': True},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'live_header', 'patch_type': 2, 'argb': True},
    {'name': 'highlight', 'patch_type': 1, 'argb': False},
    {'name': 'footer', 'patch_type': 1, 'argb': False},
    {'name': 'livechrome', 'patch_type': 1, 'argb': False},
    {'name': 'gamehilite', 'patch_type': 1, 'argb': False},
    {'name': '', 'patch_type': 0, 'argb': False},
    {'name': 'panelbacking', 'patch_type': 2, 'argb': True},
]


def hex_to_rgb(hexval: str) -> tuple:
    """Convert a 6- or 8-digit hex string (no '#') into an RGB tuple."""
    hex_digits = hexval[-6:]
    return tuple(int(hex_digits[i : i + 2], 16) for i in (0, 2, 4))


class SkinEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UIX Visual Skin Editor")

        style = ttk.Style(self.root)
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("TButton", padding=4)
        style.configure("TEntry", relief="flat")
        style.map("TButton",
                  background=[("active", "#e0e0e0")],
                  foreground=[("active", "black")])

        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.entries = {}
        self.alpha_sliders = {}
        self.swatches = {}
        self.labels = {}

        main_frame = ttk.Frame(root, padding=(10, 10))
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Allow main_frame to expand when root is resized
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(main_frame, borderwidth=0, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.scrollable_frame.columnconfigure(1, weight=1)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=(8, 0))

        btn_load = ttk.Button(button_frame, text="Load INI", command=self.load_ini)
        btn_save = ttk.Button(button_frame, text="Save INI", command=self.save_ini)
        btn_quit = ttk.Button(button_frame, text="Quit", command=self.root.quit)

        btn_load.pack(side="left", padx=10)
        btn_save.pack(side="left", padx=10)
        btn_quit.pack(side="left", padx=10)

        self.create_widgets()

    def create_widgets(self):
        """
        Build each patch row. If name == "", insert a separator.
        """
        row = 0
        for patch in PATCH_KEYS:
            name = patch["name"]
            argb = patch["argb"]

            if not name:
                # Insert a Separator instead of a blank row
                sep = ttk.Separator(self.scrollable_frame, orient="horizontal")
                sep.grid(row=row, column=0, columnspan=6, sticky="ew", pady=6)
                row += 1
                continue

            # Column 0: Label
            lbl = ttk.Label(self.scrollable_frame, text=name)
            lbl.grid(row=row, column=0, sticky="w", padx=(2, 10), pady=2)
            self.labels[name] = lbl

            # Column 1: Entry
            entry = ttk.Entry(self.scrollable_frame, width=10)
            entry.grid(row=row, column=1, padx=(0, 10), sticky="ew")
            self.entries[name] = entry

            default_val = DEFAULTS.get(name, "").upper()
            if default_val:
                entry.insert(0, default_val)

            # Column 2: Color swatch (tk.Label for direct bg control)
            swatch = tk.Label(self.scrollable_frame, bg="#000000", width=4, relief="ridge", borderwidth=1)
            swatch.grid(row=row, column=2, padx=(0, 10))
            self.swatches[name] = swatch
            self.update_swatch(name, default_val)

            # Column 3: “Pick” button
            btn_pick = ttk.Button(
                self.scrollable_frame,
                text="Pick",
                command=lambda n=name, a=argb: self.pick_color(n, a)
            )
            btn_pick.grid(row=row, column=3, padx=(0, 10))

            # Column 4: Alpha slider (if argb=True)
            if argb:
                slider = ttk.Scale(
                    self.scrollable_frame,
                    from_=0,
                    to=255,
                    orient="horizontal",
                    length=100,
                    command=lambda val, n=name: self.update_alpha(n, val)
                )
                init_alpha = int(default_val[:2], 16) if len(default_val) == 8 else 255
                slider.set(init_alpha)
                slider.grid(row=row, column=4, padx=(0, 10))
                self.alpha_sliders[name] = slider

            # Column 5: “Reset” button
            btn_reset = ttk.Button(
                self.scrollable_frame,
                text="Reset",
                command=lambda n=name, d=default_val: self.reset_to_default(n, d)
            )
            btn_reset.grid(row=row, column=5, padx=(0, 10))

            row += 1

    def update_swatch(self, key, hexval):
        if not hexval:
            return
        try:
            rgb = hex_to_rgb(hexval)
            self.swatches[key].config(bg="#%02x%02x%02x" % rgb)
        except:
            pass

    def update_alpha(self, key, alpha_val):
        current = self.entries[key].get().strip().upper()
        if not current:
            return
        alpha_hex = f"{int(float(alpha_val)):02X}"
        if len(current) == 6:
            newval = alpha_hex + current
        elif len(current) == 8:
            newval = alpha_hex + current[2:]
        else:
            return
        self.entries[key].delete(0, tk.END)
        self.entries[key].insert(0, newval)
        self.update_swatch(key, newval)
        self.highlight_if_modified(key)

    def pick_color(self, key, argb):
        color_code = colorchooser.askcolor(title=f"Pick color for {key}")
        if not color_code or not color_code[1]:
            return
        hexval = color_code[1].lstrip("#").upper()
        current = self.entries[key].get().strip().upper()
        alpha = current[:2] if (argb and len(current) == 8) else "FF"
        newval = alpha + hexval if argb else hexval
        self.entries[key].delete(0, tk.END)
        self.entries[key].insert(0, newval)
        self.update_swatch(key, newval)
        self.highlight_if_modified(key)

    def reset_to_default(self, key, default_val):
        self.entries[key].delete(0, tk.END)
        self.entries[key].insert(0, default_val)
        self.update_swatch(key, default_val)
        if key in self.alpha_sliders and len(default_val) == 8:
            self.alpha_sliders[key].set(int(default_val[:2], 16))
        self.highlight_if_modified(key)

    def load_ini(self):
        path = filedialog.askopenfilename(filetypes=[("INI files", "*.ini")])
        if not path:
            return

        entries = {}
        with open(path, "r") as file:
            for line in file:
                line = re.split(r"[;#]", line, 1)[0].strip()
                if not line or line.startswith("["):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().upper()
                    entries[key] = val

        for key, entry in self.entries.items():
            if key in entries:
                val = entries[key]
                entry.delete(0, tk.END)
                entry.insert(0, val)
                self.update_swatch(key, val)
                if key in self.alpha_sliders and len(val) == 8:
                    self.alpha_sliders[key].set(int(val[:2], 16))
                self.highlight_if_modified(key)

    def save_ini(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".ini", filetypes=[("INI files", "*.ini")])
        if not save_path:
            return

        parser = configparser.ConfigParser()
        parser.optionxform = str
        parser.add_section("These are mandatory")
        parser.set("These are mandatory","colour", "stock", "brightness", "0.5")

        parser.add_section("Override colours with your own")
        for key, entry in self.entries.items():
            value = entry.get().strip().upper()
            if value:
                parser.set("Override colours with your own", key, value)

        with open(save_path, "w") as configfile:
            parser.write(configfile)
        messagebox.showinfo("Saved", f"Skin saved to {save_path}")

    def highlight_if_modified(self, key):
        entry_val = self.entries[key].get().strip().upper()
        default_val = DEFAULTS.get(key, "").strip().upper()
        if entry_val != default_val:
            self.labels[key].config(foreground="red")
        else:
            self.labels[key].config(foreground="black")


def launch_skin_editor():
    root = tk.Tk()
    root.geometry("740x640")
    root.minsize(600, 400)
    app = SkinEditorApp(root)
    root.mainloop()


if __name__ == "__main__":
    launch_skin_editor()