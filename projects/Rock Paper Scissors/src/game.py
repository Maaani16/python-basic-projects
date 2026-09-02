import random
class RockPaperScissors :
   def __init__ (self, name: str) -> None : 
      self.name = name
      self.choices = ["rock", "paper", "scissor"]
      self.user_score = 0
      self.comp_score = 0

   def get_user_choice(self) -> str :
      user_choice = input(f"please enter your choice ({self.choices})").lower()
      if user_choice in self.choices :
         return user_choice
      return self.get_user_choice()
   
   def get_comp_choice(self) -> str :
      return random.choice(self.choices)

   def decide_winner(self, user, comp) -> str :
      #item in dict is winner and value is losser
      win_rule = {"rock" : "scissor", "paper": "rock" , "scissor" : "paper"}
      if win_rule[user] == comp :
         return "user"
      if win_rule[comp] == user :
         return "comp"
      return 0

   def play(self) -> None:
      print("lets play :)")
      
      user = self.get_user_choice()
      comp = self.get_comp_choice()
      winner = self.decide_winner(user, comp)
      print(f"{self.name}'s choice = {user}  computer's choice = {comp}")
      print(f"{winner} won. ")
      if winner == "user" :
         self.user_score += 1
      elif winner == "comp":
         self.comp_score += 1
      else:
         print("It's a draw!")
      print(f"{self.name}_score = {self.user_score}   computer_score = {self.comp_score}")
      flag = input("do you want continue this game? (y/n)").lower()
      if flag == "y":
         self.play()
      else :
         print("Goodbye.")


if __name__ == "main.py" :
   user_name = input("please enter your name: ")
   game = RockPaperScissors(user_name)
   game.get_comp_choice()
   game.play()