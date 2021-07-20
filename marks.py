a=[{"maths":90,"science":40,"marathi":70},{"maths":40,"science":50,"marathi":60},
    {"maths":50,"science":60,"marathi":70}]
subject=(input("enter a subject: "))
i=0
while i<len(a):
    k=a[i]
    if subject in k:
        print(a[i][subject],k)
    i=i+1