name: str
age: int
score: float

def has_passed(score: float) -> bool:
    return score > 59
    
name = "John"
age = 19
score = 60.78

print(f"Name: {name}, age: {age}, Passed: {has_passed(score)}")