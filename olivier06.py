import tkinter.filedialog
import matplotlib.pyplot as plt
import os

res = []

# Opent file explorer en vraagt voor een .matrxT file
file = tkinter.filedialog.askopenfilename(title='Select .matrxT file',
                                          filetypes=(("matrxT files", ".matrxT"), ("all files", ".*")))
f = open(file, "r")

# Voegt alle lines van het gekozen .matrxT toe aan een bestand
for x in f:
    res.append(x.split())
matrix = res[0][1]

# Zoekt de Size van de matrix op doormiddel van een join functie
# Deze join functie haalt alle getallen op uit bijvoorbeeld de string <MATRIX size=300>
length = int("".join(x for x in matrix if x.isdigit()))

# Haalt de eerste en laatste lijn uit de lijst weg dit zijn de <MATRIX> lines
res = res[1:-1]

# Als er geen waarde voor x3 bestaat in de lijst wordt x3 1
# Als x3 wel in de lijst bestaat wordt er gezocht naar de maximale waarde van x3 in de lijst
if len(res[0]) == 3:
    max3 = int(max(int(sub[-1]) for sub in res))
else:
    for sublist in res:
        sublist.append(1)
    max3 = 1

# Haalt de X en Y waarden op vanuit de gegeven lijst
x = [int(x[0]) for x in res]
y = [int(x[1]) for x in res]

# Plot de grafiek
plt.figure(facecolor='floralwhite')
colors = [(1 - int(x[2]) / max3, 1 - int(x[2]) / max3, 1 - int(x[2]) / max3) for x in res]
plt.rc('grid', linestyle="-", color='lavender')
plt.scatter(x, y, marker="s", c=colors)
plt.grid(True)
plt.autoscale(enable=True, axis='y')
plt.margins(0)
plt.ylim(1, length + length // 100)
plt.xlim(1, length + length // 100)
plt.title(os.path.basename(file))
plt.show()
