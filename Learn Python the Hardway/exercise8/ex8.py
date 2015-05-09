# EXERCISE 8 - Kiswanto_D #

# Make Formatter Variable
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

# Formatter dalam Formater "YO DAWG"
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# STUDY DRILLS 
# 2. Karena ada single quotes pada output, sehingga python mengganti secara otomatis ke double-quotes 
# untuk format variable string tersebut
