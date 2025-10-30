from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    N = int(input("Enter how many numbers you want to input (positive integer): "))
    processor.insert_numbers(N)

    X = int(input("Enter the number to search: "))
    result = processor.search_number(X)
    print(result)

if __name__ == "__main__":
    main()
