import csv
Csv = open(r"C:\Users\Nazar\OneDrive\Desktop\number.csv", "w", newline="", encoding="utf-8")
article = open(r"C:\Users\Nazar\OneDrive\Desktop\article.txt", "r", encoding="utf-8")
text = article.read()
article.close()
words = text.split()
a = input("Введіть ключові слова: ").split()
writer = csv.writer(Csv)
writer.writerow(["Слово", "Кількість"])
for key in a:
    count = 0
    for i in words:
        if key == i:
            count += 1
    print(key, ":", count)
    writer.writerow([key, count])
Csv.close()
