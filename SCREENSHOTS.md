# Application Screenshots and Visual Guide

## Application Launch

When you run `python3 pdf_color_converter.py`, the following window appears:

### Initial State
```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║              PDF Color Converter                      ║
║             ────────────────────                      ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  ┌─────────────────────────────┐  ┌──────────┐       ║
║  │ No file selected            │  │ Select   │       ║
║  └─────────────────────────────┘  │   PDF    │       ║
║                                   └──────────┘       ║
║                                                       ║
║  Selected Color:  ┌────────┐  ┌──────────┐          ║
║                   │░░░░░░░░│  │ Choose   │          ║
║                   │░░░░░░░░│  │  Color   │          ║
║                   └────────┘  └──────────┘          ║
║                   (Black)                            ║
║                                                       ║
║           ┌────────────────────────┐                 ║
║           │                        │                 ║
║           │    Convert PDF         │                 ║
║           │    [GREEN BUTTON]      │                 ║
║           └────────────────────────┘                 ║
║                                                       ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

### After Selecting a File
```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║              PDF Color Converter                      ║
║             ────────────────────                      ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  ┌─────────────────────────────┐  ┌──────────┐       ║
║  │ my_document.pdf             │  │ Select   │       ║
║  └─────────────────────────────┘  │   PDF    │       ║
║                                   └──────────┘       ║
║                                                       ║
║  Selected Color:  ┌────────┐  ┌──────────┐          ║
║                   │░░░░░░░░│  │ Choose   │          ║
║                   │░░░░░░░░│  │  Color   │          ║
║                   └────────┘  └──────────┘          ║
║                   (Black)                            ║
║                                                       ║
║           ┌────────────────────────┐                 ║
║           │                        │                 ║
║           │    Convert PDF         │                 ║
║           │    [GREEN BUTTON]      │                 ║
║           └────────────────────────┘                 ║
║                                                       ║
║           File selected successfully                 ║
╚═══════════════════════════════════════════════════════╝
```

### After Selecting a Color (Red)
```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║              PDF Color Converter                      ║
║             ────────────────────                      ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  ┌─────────────────────────────┐  ┌──────────┐       ║
║  │ my_document.pdf             │  │ Select   │       ║
║  └─────────────────────────────┘  │   PDF    │       ║
║                                   └──────────┘       ║
║                                                       ║
║  Selected Color:  ┌────────┐  ┌──────────┐          ║
║                   │████████│  │ Choose   │          ║
║                   │████████│  │  Color   │          ║
║                   └────────┘  └──────────┘          ║
║                   (Red)                              ║
║                                                       ║
║           ┌────────────────────────┐                 ║
║           │                        │                 ║
║           │    Convert PDF         │                 ║
║           │    [GREEN BUTTON]      │                 ║
║           └────────────────────────┘                 ║
║                                                       ║
║           Color selected: #FF0000                    ║
╚═══════════════════════════════════════════════════════╝
```

### During Conversion
```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║              PDF Color Converter                      ║
║             ────────────────────                      ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  ┌─────────────────────────────┐  ┌──────────┐       ║
║  │ my_document.pdf             │  │ Select   │       ║
║  └─────────────────────────────┘  │   PDF    │       ║
║                                   └──────────┘       ║
║                                                       ║
║  Selected Color:  ┌────────┐  ┌──────────┐          ║
║                   │████████│  │ Choose   │          ║
║                   │████████│  │  Color   │          ║
║                   └────────┘  └──────────┘          ║
║                   (Red)                              ║
║                                                       ║
║           ┌────────────────────────┐                 ║
║           │                        │                 ║
║           │    Convert PDF         │                 ║
║           │    [GREEN BUTTON]      │                 ║
║           └────────────────────────┘                 ║
║                                                       ║
║           Converting PDF... Please wait...           ║
╚═══════════════════════════════════════════════════════╝
```

### Success Dialog
```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║              PDF Color Converter                      ║
║             ────────────────────                      ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║         ┌──────────────────────────┐                 ║
║         │ ╔══════════════════════╗ │                 ║
║         │ ║ Success          [X] ║ │                 ║
║         │ ╠══════════════════════╣ │                 ║
║         │ ║                      ║ │                 ║
║         │ ║ PDF converted        ║ │                 ║
║         │ ║ successfully!        ║ │                 ║
║         │ ║                      ║ │                 ║
║         │ ║ Saved as:            ║ │                 ║
║         │ ║ my_document_colored  ║ │                 ║
║         │ ║        .pdf          ║ │                 ║
║         │ ║                      ║ │                 ║
║         │ ║      [   OK   ]      ║ │                 ║
║         │ ╚══════════════════════╝ │                 ║
║         └──────────────────────────┘                 ║
║                                                       ║
║           Conversion complete!                       ║
╚═══════════════════════════════════════════════════════╝
```

## Color Picker Dialog

When you click "Choose Color", the system's native color picker appears:

### Windows Color Picker (Example)
```
╔════════════════════════════════════════╗
║ Choose a color                    [X] ║
╠════════════════════════════════════════╣
║                                        ║
║  ┌────────────────┐  ┌──────────┐     ║
║  │                │  │          │     ║
║  │  Rainbow       │  │ Selected │     ║
║  │  Spectrum      │  │  Color   │     ║
║  │  Grid          │  │ Preview  │     ║
║  │                │  │          │     ║
║  └────────────────┘  └──────────┘     ║
║                                        ║
║  Hue:        ▐████████▌                ║
║  Sat:        ▐████░░░░▌                ║
║  Lum:        ▐██████░░▌                ║
║                                        ║
║  Red:    255 ▐████████▌                ║
║  Green:    0 ▐░░░░░░░░▌                ║
║  Blue:     0 ▐░░░░░░░░▌                ║
║                                        ║
║  Hex: #FF0000  [_______]               ║
║                                        ║
║         [   OK   ]  [ Cancel ]         ║
╚════════════════════════════════════════╝
```

### macOS Color Picker (Example)
```
╔════════════════════════════════════════╗
║ Colors                            [X] ║
╠════════════════════════════════════════╣
║  [Wheel] [Sliders] [Palette] [More]   ║
╠════════════════════════════════════════╣
║                                        ║
║            ┌──────────┐                ║
║            │  Color   │                ║
║            │  Wheel   │                ║
║            │          │                ║
║            └──────────┘                ║
║                                        ║
║         Selected: #FF0000              ║
║                                        ║
║              ┌────────┐                ║
║              │████████│                ║
║              │████████│                ║
║              └────────┘                ║
║                                        ║
╚════════════════════════════════════════╝
```

### Linux Color Picker (GTK Example)
```
╔════════════════════════════════════════╗
║ Pick a Color                      [X] ║
╠════════════════════════════════════════╣
║                                        ║
║  ┌──────────────────────────────┐     ║
║  │░░░░░░▓▓▓▓▓▓████████████▓▓▓▓░░│     ║
║  │░░░░░░▓▓▓▓▓▓████████████▓▓▓▓░░│     ║
║  │░░░░░░▓▓▓▓▓▓████████████▓▓▓▓░░│     ║
║  │░░░░░░▓▓▓▓▓▓████████████▓▓▓▓░░│     ║
║  └──────────────────────────────┘     ║
║             ▲ (Click to select)       ║
║                                        ║
║  Current Color: ┌────────┐            ║
║                 │████████│            ║
║                 └────────┘            ║
║                                        ║
║  HTML notation: #FF0000                ║
║                                        ║
║         [   OK   ]  [ Cancel ]         ║
╚════════════════════════════════════════╝
```

## File Selection Dialog

When you click "Select PDF", the file browser appears:

```
╔════════════════════════════════════════════╗
║ Select a PDF file                     [X] ║
╠════════════════════════════════════════════╣
║ Look in: [Documents         ▼]       🔍   ║
╠════════════════════════════════════════════╣
║ Name                    Size      Type     ║
║ ─────────────────────────────────────────  ║
║ 📁 My Folder            --        Folder  ║
║ 📄 document.pdf         245 KB    PDF     ║
║ 📄 invoice.pdf          128 KB    PDF     ║
║ 📄 report.pdf           1.2 MB    PDF     ║
║ 📄 thesis.pdf           3.4 MB    PDF     ║
║                                            ║
║                                            ║
╠════════════════════════════════════════════╣
║ File name: [________________]              ║
║ Files of type: [PDF files (*.pdf)    ▼]   ║
╠════════════════════════════════════════════╣
║              [   Open   ]  [ Cancel ]      ║
╚════════════════════════════════════════════╝
```

## Before and After Examples

### Example 1: Black and White Document → Red

**Before (Original PDF):**
```
┌────────────────────────┐
│                        │
│  Document Title        │ (Black text)
│  ═══════════           │ (Black line)
│                        │
│  This is some text     │ (Black text)
│  with content that     │ (Black text)
│  will be converted.    │ (Black text)
│                        │
│  ┌──────────┐          │
│  │  Table   │          │ (Black borders)
│  └──────────┘          │
│                        │
└────────────────────────┘
```

**After (Converted to Red):**
```
┌────────────────────────┐
│                        │
│  Document Title        │ (Red text)
│  ═══════════           │ (Red line)
│                        │
│  This is some text     │ (Red text)
│  with content that     │ (Red text)
│  will be converted.    │ (Red text)
│                        │
│  ┌──────────┐          │
│  │  Table   │          │ (Red borders)
│  └──────────┘          │
│                        │
└────────────────────────┘
```

### Example 2: Colorful Document → Blue

**Before (Original PDF with colors):**
```
┌────────────────────────┐
│                        │
│  Title                 │ (Red text)
│  ══════                │ (Green line)
│                        │
│  Some text here        │ (Black text)
│                        │
│  ████████              │ (Orange box)
│                        │
│  ●●●●                  │ (Purple circles)
│                        │
└────────────────────────┘
```

**After (Converted to Blue):**
```
┌────────────────────────┐
│                        │
│  Title                 │ (Blue text)
│  ══════                │ (Blue line)
│                        │
│  Some text here        │ (Blue text)
│                        │
│  ████████              │ (Blue box)
│                        │
│  ●●●●                  │ (Blue circles)
│                        │
└────────────────────────┘
```

## Real-World Usage Flow

1. **User opens application** → Main window appears
2. **User clicks "Select PDF"** → File dialog opens
3. **User navigates to PDF** → Browses folders
4. **User selects file** → Filename appears in app
5. **User clicks "Choose Color"** → Color picker opens
6. **User selects red color** → Color preview updates
7. **User clicks "Convert PDF"** → Status shows "Converting..."
8. **Processing happens** → 2-5 seconds per page
9. **Success dialog appears** → Shows output filename
10. **User clicks OK** → Can convert another file

## Visual Feedback Elements

### Status Messages
- `""` - Initial state (no message)
- `"File selected successfully"` - After file selection
- `"Color selected: #RRGGBB"` - After color selection
- `"Converting PDF... Please wait..."` - During conversion
- `"Conversion complete!"` - After success
- `"Error during conversion"` - If error occurs

### Button States
- **Enabled** - Normal, clickable
- **Hover** - Slightly highlighted
- **Pressed** - Darker appearance
- **Disabled** - Grayed out (not used in this app)

### Color Display States
- **Default** - Black (#000000)
- **After Selection** - Shows chosen color
- **Hover** - No change (canvas, not interactive)

This visual guide helps users understand what to expect when using the PDF Color Converter application!
