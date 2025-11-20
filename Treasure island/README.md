## 🏝️ Treasure Island Adventure Game

This is a simple text-based "Choose Your Own Adventure" game written in **Python**. Your mission is to navigate the island's dangers by making the correct choices at each stage to find the hidden **treasure**!

---

### 🚀 How to Play

1.  **Run the Script:** Execute the Python code in your environment.
2.  **Follow the Prompts:** The game will ask you to make a choice (e.g., `l` or `r`) at each stage.
3.  **Enter the required letter** for your selection.
4.  **Find the correct path** to achieve the "You Win!" outcome.

---

### 🗺️ Game Logic and Winning Path

The game is structured as a **three-level decision tree**. Only one specific sequence of choices leads to victory. Making the wrong choice at any point results in a **"Game Over"**.

#### **Level 1: Direction**

| Prompt | Input | Outcome |
| :--- | :---: | :--- |
| `Choose a Direction l for Left and r for Right` | **`l`** | Continue to Level 2 (The River). |
| | `r` | Fall into a hole. **Game Over.** |

#### **Level 2: Action at the River**

*(Only available if you chose **Left**)*

| Prompt | Input | Outcome |
| :--- | :---: | :--- |
| `Choose Your Desicion s for Swim and w for Wait` | **`w`** | Continue to Level 3 (The Doors). |
| | `s` | Attacked by trout. **Game Over.** |

#### **Level 3: The Doors**

*(Only available if you chose **Wait**)*

| Prompt | Input | Outcome |
| :--- | :---: | :--- |
| `Choose a door now b for Blue, r for Red, y for Yellow` | **`y`** | **🏆 You Win!** |
| | `b` | Eaten by beasts. **Game Over.** |
| | `r` | Burned by fire. **Game Over.** |
| | *Any other input* | **Game Over.** |

---

### 💻 Code Snippet

The core logic is implemented using nested `if` statements:

```python
# The Winning Path: Left -> Wait -> Yellow
if left_right == "l":
    if swim_wait == "w":
        if door == "y":
            print("You Win!")
        # ... Losing doors (b, r, else)
    # ... Losing swim option (s)
# ... Losing right option (r)