import write_bets
import display_bets


def menu():
    print("--- UCD Tipster Program ---")
    print("You may select an operation from the menu below:")
    print("1. Enter a new bet")
    print("2. Display all bets")
    print("3. Display yearly report")
    print("4. Display most popular race course")
    print("5. Display bets in order")
    print("6. Display highest bets won and lost")
    print("7. Display UCD Tipster success rate")
    print("8. Display average spent by year/month")
    print("9. Display average time between bets")

    choice  = input('Select operaton: ')
    if choice == "1":
        write_bets.record_new_bet()
    elif choice == "2":
        display_bets.all()
    elif choice == "3":
        display_bets.yearly_report()
    elif choice == "4":
        display_bets.most_popular_course()
    elif choice == "5":
        display_bets.bets_by_date()
    elif choice == "6":
        display_bets.highest_bets()
    elif choice == "7":
        display_bets.success_rate()
    elif choice == "8":
        display_bets.average_spent()
    elif  choice =="9":
        display_bets.average_time()
    menu()

menu()

