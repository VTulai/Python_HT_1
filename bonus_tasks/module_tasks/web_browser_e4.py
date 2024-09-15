import webbrowser

use_term = input("Enter a search: ").replace(" ", "+")

webbrowser.open(f"https://google.com/search?q={use_term}")

