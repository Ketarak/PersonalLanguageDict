# Practice to better understand constructors
class Friend:
    job = "none"
    def __init__(self):
        self.job

bob= Friend()

print(bob.job)
bob.job = "builder"
print(bob.job)

