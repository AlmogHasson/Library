The Projects subject its managing a book library
1. # Create 3 Tables in sqlite:
    **Books**:
            [v] - id(PK)
            [v] - Name
            [v] - Author
            [v] - Year published
            [v] - Type (1/2/3)

    **Customers**:
            [v] - id(PK) 
            [v] - Name
            [v] - CityS
            [v] - Age

    **Loans**:
            [v] - CustomerID
            [v] - BookID
            [v] - Loandate
            [v] - Returndate

2.    # Create book type that sets the time limit of a loan:
    - 1 - upto 10 days
    - 2 - upto 20 days
    - 3 - upto 30 days
3. # Create the DAL:
    [v] - build a class for each entity
    [v] - create a separate module for each class
    [x] - build a test unit

4. # Build a client app that uses the DAL. add a menu:
    [v] - Add a new customer
    [x] - Add a new book
    [x] - Loan a book
    [x] - Return a book
    [v] - Display all books
    [v] - Display all customers
    [x] - Display late loans
    [x] - Find customer by name
    [x] - Remove book
    [x] - Remove customer