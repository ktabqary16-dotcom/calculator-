#!/usr/bin/env python3
# Scientific Calculator v1.0 – CLI Version

import math
import sys
from colorama import init, Fore, Style

init(autoreset=True)

class ScientificCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []
    
    def banner(self):
        print(Fore.CYAN + """
╔════════════════════════════════════════════════════════════════════╗
║                 SCIENTIFIC CALCULATOR v1.0                         ║
║              آلة حاسبة علمية متقدمة – CLI Version                  ║
╚════════════════════════════════════════════════════════════════════╝
""")
    
    def show_menu(self):
        print(Fore.YELLOW + """
┌─────────────────────────────────────────────────────────────────────┐
│                         MAIN MENU                                   │
├─────────────────────────────────────────────────────────────────────┤
│  📌 BASIC:                                                          │
│     [1] +     [2] -     [3] *     [4] /     [5] %                  │
│                                                                     │
│  🔬 SCIENTIFIC:                                                     │
│     [6] √x     [7] xⁿ    [8] ⁿ√x    [9] sin()   [10] cos()         │
│     [11] tan() [12] log() [13] ln()  [14] |x|                       │
│                                                                     │
│  💾 MEMORY:                                                         │
│     [15] M+    [16] M-    [17] MR     [18] MC                       │
│                                                                     │
│  📜 OTHER:                                                          │
│     [19] History   [20] Clear History   [21] About                  │
│     [0] Exit                                                        │
└─────────────────────────────────────────────────────────────────────┘
""")
    
    def basic_ops(self, a, b, op):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/':
            if b == 0: raise ValueError("Division by zero!")
            return a / b
        elif op == '%':
            if b == 0: raise ValueError("Division by zero!")
            return a % b
        return None
    
    def scientific_ops(self, num, op, n=2):
        if op == 'sqrt':
            if num < 0: raise ValueError("Cannot sqrt negative!")
            return math.sqrt(num)
        elif op == 'pow': return num ** n
        elif op == 'root':
            if num < 0: raise ValueError("Cannot root negative!")
            return num ** (1/n)
        elif op == 'sin': return math.sin(math.radians(num))
        elif op == 'cos': return math.cos(math.radians(num))
        elif op == 'tan': return math.tan(math.radians(num))
        elif op == 'log':
            if num <= 0: raise ValueError("Log only for positive numbers!")
            return math.log10(num)
        elif op == 'ln':
            if num <= 0: raise ValueError("Ln only for positive numbers!")
            return math.log(num)
        elif op == 'abs': return abs(num)
        return None
    
    def add_history(self, expr, result):
        from datetime import datetime
        self.history.append({
            'expr': expr,
            'result': result,
            'time': datetime.now().strftime("%H:%M:%S")
        })
    
    def show_history(self):
        if not self.history:
            print(Fore.YELLOW + "\n[-] No history!")
            return
        print(Fore.CYAN + "\n" + "="*60)
        print(Fore.CYAN + "                     HISTORY")
        print(Fore.CYAN + "="*60)
        for i, item in enumerate(self.history[-10:], 1):
            print(f"  {i}. {item['expr']} = {item['result']}  [{item['time']}]")
    
    def clear_history(self):
        self.history.clear()
        print(Fore.GREEN + "\n[+] History cleared!")
    
    def about(self):
        print(Fore.CYAN + """
╔════════════════════════════════════════════════════════════════════╗
║                         ABOUT                                      ║
╠════════════════════════════════════════════════════════════════════╣
║  Name: Scientific Calculator v1.0                                  ║
║  Language: Python 3                                                ║
║  Author: Mazen                                                    ║
║                                                                     ║
║  Features: Basic + Scientific + Memory + History                   ║
╚════════════════════════════════════════════════════════════════════╝
""")
    
    def get_number(self, prompt="Enter number: "):
        while True:
            try:
                return float(input(Fore.YELLOW + prompt + Style.RESET_ALL))
            except ValueError:
                print(Fore.RED + "[-] Invalid number!")
    
    def get_two_numbers(self):
        a = self.get_number("First number: ")
        b = self.get_number("Second number: ")
        return a, b
    
    def run(self):
        self.banner()
        
        while True:
            self.show_menu()
            choice = input(Fore.GREEN + "\n🔧 Choice [0-21]: " + Style.RESET_ALL).strip()
            
            if choice == '0':
                print(Fore.GREEN + "\n[+] Goodbye!")
                sys.exit(0)
            
            elif choice == '1':
                a, b = self.get_two_numbers()
                r = self.basic_ops(a, b, '+')
                print(Fore.GREEN + f"\n✅ {a} + {b} = {r}")
                self.add_history(f"{a} + {b}", r)
            
            elif choice == '2':
                a, b = self.get_two_numbers()
                r = self.basic_ops(a, b, '-')
                print(Fore.GREEN + f"\n✅ {a} - {b} = {r}")
                self.add_history(f"{a} - {b}", r)
            
            elif choice == '3':
                a, b = self.get_two_numbers()
                r = self.basic_ops(a, b, '*')
                print(Fore.GREEN + f"\n✅ {a} × {b} = {r}")
                self.add_history(f"{a} × {b}", r)
            
            elif choice == '4':
                a, b = self.get_two_numbers()
                try:
                    r = self.basic_ops(a, b, '/')
                    print(Fore.GREEN + f"\n✅ {a} ÷ {b} = {r}")
                    self.add_history(f"{a} ÷ {b}", r)
                except ValueError as e:
                    print(Fore.RED + f"\n[-] Error: {e}")
            
            elif choice == '5':
                a, b = self.get_two_numbers()
                try:
                    r = self.basic_ops(a, b, '%')
                    print(Fore.GREEN + f"\n✅ {a} % {b} = {r}")
                    self.add_history(f"{a} % {b}", r)
                except ValueError as e:
                    print(Fore.RED + f"\n[-] Error: {e}")
            
            elif choice == '6':
                n = self.get_number("Number: ")
                try:
                    r = self.scientific_ops(n, 'sqrt')
                    print(Fore.GREEN + f"\n✅ √{n} = {r}")
                    self.add_history(f"√{n}", r)
                except ValueError as e:
                    print(Fore.RED + f"\n[-] Error: {e}")
            
            elif choice == '7':
                a = self.get_number("Base: ")
                b = self.get_number("Exponent: ")
                r = self.scientific_ops(a, 'pow', b)
                print(Fore.GREEN + f"\n✅ {a}^{b} = {r}")
                self.add_history(f"{a}^{b}", r)
            
            elif choice == '8':
                n = self.get_number("Number: ")
                root = self.get_number("Root (n): ")
                try:
                    r = self.scientific_ops(n, 'root', root)
                    print(Fore.GREEN + f"\n✅ {root}√{n} = {r}")
                    self.add_history(f"{root}√{n}", r)
                except ValueError as e:
                    print(Fore.RED + f"\n[-] Error: {e}")
            
            elif choice == '9':
                n = self.get_number("Angle (degrees): ")
                r = self.scientific_ops(n, 'sin')
                print(Fore.GREEN + f"\n✅ sin({n}°) = {r:.6f}")
                self.add_history(f"sin({n}°)", f"{r:.6f}")
            
            elif choice == '10':
                n = self.get_number("Angle (degrees): ")
                r = self.scientific_ops(n, 'cos')
                print(Fore.GREEN + f"\n✅ cos({n}°) = {r:.6f}")
                self.add_history(f"cos({n}°)", f"{r:.6f}")
            
            elif choice == '11':
                n = self.get_number("Angle (degrees): ")
                r = self.scientific_ops(n, 'tan')
                print(Fore.GREEN + f"\n✅ tan({n}°) = {r:.6f}")
                self.add_history(f"tan({n}°)", f"{r:.6f}")
            
            elif choice == '12':
                n = self.get_number("Number: ")
                try:
                    r = self.scientific_ops(n, 'log')
                    print(Fore.GREEN + f"\n✅ log₁₀({n}) = {r:.6f}")
                    self.add_history(f"log₁₀({n})", f"{r:.6f}")
                except ValueError as e:
                    print(Fore.RED + f"\n[-] Error: {e}")
            
            elif choice == '13':
                n = self.get_number("Number: ")
                try:
                    r = self.scientific_ops(n, 'ln')
                    print(Fore.GREEN + f"\n✅ ln({n}) = {r:.6f}")
                    self.add_history(f"ln({n})", f"{r:.6f}")
                except ValueError as e:
                    print(Fore.RED + f"\n[-] Error: {e}")
            
            elif choice == '14':
                n = self.get_number("Number: ")
                r = self.scientific_ops(n, 'abs')
                print(Fore.GREEN + f"\n✅ |{n}| = {r}")
                self.add_history(f"|{n}|", r)
            
            elif choice == '15':
                n = self.get_number("Add to memory: ")
                self.memory += n
                print(Fore.GREEN + f"\n✅ Memory: {self.memory}")
            
            elif choice == '16':
                n = self.get_number("Subtract from memory: ")
                self.memory -= n
                print(Fore.GREEN + f"\n✅ Memory: {self.memory}")
            
            elif choice == '17':
                print(Fore.GREEN + f"\n✅ Memory: {self.memory}")
            
            elif choice == '18':
                self.memory = 0
                print(Fore.GREEN + "\n✅ Memory cleared!")
            
            elif choice == '19':
                self.show_history()
            
            elif choice == '20':
                self.clear_history()
            
            elif choice == '21':
                self.about()
            
            else:
                print(Fore.RED + "\n[-] Invalid choice!")
            
            input(Fore.CYAN + "\n[Press Enter to continue...]" + Style.RESET_ALL)
            print("\n" * 2)


if __name__ == "__main__":
    try:
        calc = ScientificCalculator()
        calc.run()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n[!] Interrupted")
        sys.exit(0)
