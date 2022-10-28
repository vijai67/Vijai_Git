myd = {"bag":"Taila",
"apple" : "Sheb",
"mother" : "Maatha",
"cat" : "Billi"
}

# print("The Entered Key Word Is Translated To Hindi : ")
try:
    print(myd.keys())
    a = input(("Enter The Word To Get Hindi Meaning : "))
    print("Your Word's Meaning Is : ", myd.get(a))

except:
    print("[Entered Key Is Not Available Or Wrong]")