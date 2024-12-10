# Assumptions:
# 1. Seats are represented as a 2D list where each row corresponds to a row in the coach.
# 2. 0 indicates an available seat, and 1 indicates a booked seat.
# 3. Seat numbers are labeled sequentially from 1 to 80.

class TrainCoach:
    def __init__(self):
        self.rows = [[0] * 7 for _ in range(11)]  # 11 rows of 7 seats each
        self.rows[-1] = [0] * 3  # Last row with 3 seats
        self.total_seats = 80
        self.booked_seats = 0

    def display_seats(self):
        """Displays seat availability status."""
        for i, row in enumerate(self.rows):
            print(f"Row {i + 1}: {['B' if seat else 'A' for seat in row]}")

    def book_seats(self, num_seats):
        """Books seats based on the given number."""
        if self.booked_seats + num_seats > self.total_seats:
            print("Not enough seats available.")
            return []

        booked = []

        # Try to book in a single row first
        for row_index, row in enumerate(self.rows):
            if row.count(0) >= num_seats:  # Check if the row has enough space
                for seat_index in range(len(row)):
                    if row[seat_index] == 0 and len(booked) < num_seats:
                        row[seat_index] = 1
                        booked.append(row_index * 7 + seat_index + 1)
                self.booked_seats += len(booked)
                return booked

        # If not possible in one row, book nearby seats
        for row_index, row in enumerate(self.rows):
            for seat_index in range(len(row)):
                if row[seat_index] == 0 and len(booked) < num_seats:
                    row[seat_index] = 1
                    booked.append(row_index * 7 + seat_index + 1)
        
        self.booked_seats += len(booked)
        return booked

# Simulate seat booking
def main():
    coach = TrainCoach()

    # Pre-booked seats for testing
    coach.rows[0][:2] = [1, 1]  # First two seats in the first row are booked
    coach.rows[5][4] = 1  # A seat in the sixth row is booked

    print("Initial Seat Status:")
    coach.display_seats()

    while coach.booked_seats < coach.total_seats:
        try:
            num_seats = int(input("Enter the number of seats to book (0 to exit): "))
            if num_seats == 0:
                break

            booked_seats = coach.book_seats(num_seats)
            if booked_seats:
                print(f"Seats booked: {booked_seats}")
            else:
                print("Unable to book the requested number of seats.")

            print("Updated Seat Status:")
            coach.display_seats()
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()