### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)

Link: https://github.com/emilybache/Tennis-Refactoring-Kata/blob/main/python/tennis2.py

I found the code on GitHub in a repository for coding exercises. I was looking for something that has something to 
do with the topic of my final project.
I chose it because my final project is a Tennis LK-Calculator. 
This specific file implements the scoring system of a tennis match (Love, Fifteen, Thirty, Deuce, Advantage) 
using Object-Oriented Programming in Python. Analyzing how another developer translated complex sports 
scoring rules into code is incredibly helpful for my own project.


---

2. What does the program do? What's the general structure of the program? 

The program itself is designed to track the live score of a single tennis match. It registers whenever a player wins a point 
and converts the current numeric score into traditional tennis terms like Love, Fifteen, Deuce, or Advantage. Structurally, 
the entire script is built using object-oriented programming. Everything is encapsulated inside a central class called "TennisGame2", 
where the constructor takes the names of both players upon initialization and sets their point counters to 0. 
Alongside a few small helper methods that increment the points, the core of the program is a very long method called score(), 
which uses many sequential conditions to determine and return the current score as text.


---

3. Function analysis: pick one function and analyze it in detail:

- What does this function do?
- What are the inputs and outputs?
- How does it work (step by step)?

Looking focused at the main method "score()" it reads the internal attributes for the players' points and outputs the matching score as a string. 
The process is structured in a logical way (step by step): first, the function checks if the score is tied. If it is a tie with fewer than three points, 
the word "All" is appended to the score, whereas a tie of three or more points directly sets the output to "Deuce". 
Following that, there are blocks to handle unequal scores and catch combinations like "Forty-Love". 
At the end of the method, it checks if a player has a lead of exactly one point to trigger the "Advantage" status, 
or if the lead is two or more points with at least four points scored, which then results in a win ("Win").


---

4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)


I think there are two main takeaways from this code that I can learn from and eventually apply to my final project. 
First: It shows very well how irregular sports rules, where numeric values map to specific terms, 
can be cleanly managed using conditional statements.
Second: The encapsulation of data serves as a great model: because the points and the calculation logic live together inside the same class, 
the program stays organized. 
I plan to do the same thing for my LK-calculator to directly link player data with the calculations. Hope it works for me.

---

5. What parts of the code were confusing or difficult at the beginning to understand? Were you able to understand what it is doing after your own research?

At first, the code was quite confusing for me because it relies on extremely often repetitive if-conditions. 
Instead of using "elif" or "else", it just places countless individual if-statements right after one another, 
and the won_point() method strangely checks for the hardcoded text string "player1" instead of utilizing the actual attribute for the player's name. 
However, after researching a bit about the repository itself and the functions, I found out that this is a so-called "Refactoring Kata." 
I think it means the code was intentionally written in a messy and repetitive way so that other programmers (maybe students) can practice cleaning/organizing it.
Realizing this design intent was super helpful because it made me notice how important it is to keep code compact and avoid repeating yourself all the time.

---

Extra notes:

This file is relevant for me and my project because my calculator will also need to compare scores and results and map them to dynamic outcomes.