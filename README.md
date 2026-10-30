# Heroes and Crystals

A two-character arcade game built with Python and Pygame Zero.

## Gameplay

- Control two heroes independently on a tile-based map.
- Move the first hero with `W`, `A`, `S`, and `D`.
- Move the second hero with the arrow keys.
- Fight enemies by moving into them. Collisions damage both the hero and the enemy.
- Defeat enemies to earn experience.
- Collect dropped bonuses:
  - Hearts restore health.
  - Swords increase attack power.
- Enemy health and attack values are generated randomly.
- After 20 enemy defeats, the game advances to a harder level.
- Reach 5,000 experience with either hero to win.
- The game ends if either hero's health reaches zero.
- Press `Enter` on the end screen to restart.

## Requirements

- Python
- Pygame Zero

## Run

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Start the game from the project directory:

```bash
pgzrun main.pyw
```
