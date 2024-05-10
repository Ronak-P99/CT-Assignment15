class BudgetCategory:
    def __init__(self, category_name, budget):
        self.__category = category_name
        if budget > 0:
            self.__budget = budget
        self.total = 0
        
    def get_category_name(self):
        return self.__category
    
    def get_budget(self):
        return self.__budget
        
    def set_budget(self, new_budget):
        if new_budget > 0:
            self.__budget = new_budget
        else:
            print("Make sure your new budget is a positive number!")

    def add_expense(self, amount):
       try:
            if self.__budget > 0:
                self.total = self.__budget - amount
                return self.total
       except AttributeError:
            print(f"\nPlease make sure your budget is a positive number!\n")

    
    def display_category_summary(self):
        try:
            if self.__budget > 0:
                print("\nYour budget details:")
                print(f"\nCategory: {self.__category} - Budget: ${self.__budget} ")
                print(f"Total left over after including expenses is {self.total}\n")
        except AttributeError:
            pass

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()