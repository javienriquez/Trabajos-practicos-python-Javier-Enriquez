import matplotlib.pyplot as plt
import random

plt.plot([00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],[12, 11, 10, 8, 8, 7, 7, 9, 10, 12, 14, 15, 16, 18, 19, 20, 20, 19, 18, 16, 15, 13, 12, 10], marker='o')
plt.plot([00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],[2, 2, 1, 1, 2, 2, 3, 4, 5, 4, 5, 6, 8, 9, 10, 9, 9, 8, 7, 6, 5, 4, 2, 2], marker='o')
plt.title('Comparación de la temperatura durante un día entre Mendoza y Santa Cruz')
plt.xlabel('Hora del día')
plt.ylabel('Temperatura (°C)')
plt.show()
