import os
import pickle


print(f"Highest Protocol: {pickle.HIGHEST_PROTOCOL} (Python {pickle.format_version})")

data = {"name": "MyName", "age": 25}

# Pickling (serialization)
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Unpickling (deserialization)
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)


def expensive_function():
    return [x**2 for x in range(10**6)]


if os.path.exists("cache.pkl"):
    with open("cache.pkl", "rb") as f:
        result = pickle.load(f)
        print(result.__len__(), "items are cached")
        print("Loaded from cache")
else:
    result = expensive_function()
    print("Computed result")
    # Save the result to cache
    with open("cache.pkl", "wb") as f:
        pickle.dump(result, f)
        print(f"{result.__len__()} items are saved to cache")


class GameState:
    def __init__(self, level, score):
        self.level = level
        self.score = score


game = GameState(level=5, score=4200)

with open("saved_game.bin", "wb") as f:
    pickle.dump(game, f)

with open("saved_game.bin", "rb") as f:
    loaded_game = pickle.load(f)
    print(f"Level: {loaded_game.level}, Score: {loaded_game.score}")
