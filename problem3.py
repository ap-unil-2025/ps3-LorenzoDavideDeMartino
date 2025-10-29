import statistics
def get_numbers_from_user():
    numbers = []
    # Your code here
    user = 0 
    while True : 
        user =input("Give me another number.")
        if user == "done" : 
            break 
        
        else :
            number = int(user)
            numbers.append(number)

    return numbers

def analyze_numbers(numbers):
    if not numbers:
        return None

    analysis = {}

    counts = len(numbers)
    Sum = sum(numbers)
    Average = statistics.mean(numbers)
    Minimum = min(numbers)
    Maximum = max(numbers)

    even_count = []
    odd_count = []
    for i in numbers : 
        if i % 2 == 0: 
            even_count.append(i)
        else :
            odd_count.append(i) 

    analysis.update({"count":counts, 
                     "sum":Sum,
                     "average":Average,
                     "minimum":Minimum,
                     "maximum":Maximum,
                     "even_count":even_count,
                     "odd_count":odd_count
                     })

    # Your code here
    return analysis

def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    # Your code here
    print(analysis)
    pass

def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")

    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)

if __name__ == "__main__":
    main()