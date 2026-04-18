import sys
import time

def slow_print(text):
    """打印粉色文本，然后等待。
    如果用户在此期间按下 Ctrl+T，则等待0.1秒返回；否则1秒。
    兼容各种环境。
    """
    is_tty = sys.stdin.isatty()
    PINK = ""
    RESET = ""

    if is_tty:
        if sys.platform == "win32":
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                pass
        PINK = "\033[95m"
        RESET = "\033[0m"

    print(f"{PINK}{text}{RESET}")

    if not is_tty:
        time.sleep(1)
        return

    # 检测 Ctrl+T
    if sys.platform == 'win32':
        import msvcrt
        start = time.time()
        while time.time() - start < 1:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\x14':
                    time.sleep(0.1)
                    return
            time.sleep(0.02)
    else:
        import select
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            start = time.time()
            while time.time() - start < 1:
                rlist, _, _ = select.select([fd], [], [], 0.05)
                if rlist:
                    ch = sys.stdin.read(1)
                    if ord(ch) == 20:
                        time.sleep(0.1)
                        return
        finally:
            termios.tcsetattr(fd, termios.TCSANOW, old_settings)