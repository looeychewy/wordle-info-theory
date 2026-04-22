# Background colors
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"
BG_GREY    = "\033[100m"

# Text colors
FG_BLACK = "\033[30m"
FG_WHITE = "\033[97m"

# Clear terminal colors
RESET = "\033[0m"

print(f"{BG_YELLOW}{FG_BLACK} highlighted text {RESET}{BG_GREY}normal text{RESET}")
print(f"{BG_CYAN}{FG_BLACK} another highlight {RESET}")
print(f"hello {BG_YELLOW}w{RESET}orld")