import sys

def determine_winner(n, m):
    if n == m:
        return "draw"
    elif n == 3 or (m != 3 and n > m):
        return "win"
    else:
        return "lose"

def main(lines):
    n = lines[0]
    m = lines[1]

    result = determine_winner(n,m)
    print(result)

if __name__ == '__main__':
     lines = []
     a = int(input("enter your dice"))
     b = int(input("enter opponent dice"))
     lines.append(a)
     lines.append(b)
     main(lines)

# def main():
#     input_data = input("Enter a line: ")
#     output = f"Hello {input_data}!"
#     print(output)

# if __name__ == '__main__':
#     main()
