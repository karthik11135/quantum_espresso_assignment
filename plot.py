import matplotlib.pyplot as plt

volumes = [
23.1033	,
24.3415	,
25.4451	,
26.7990	,
27.8881 ,
30.1481	]  
energies = [
-111.60700210,
-111.40848402,
-111.38068540,
-111.34744505,
-111.32172380,
-111.27567777]  # Energies in Ry

plt.figure(figsize=(8, 6))
plt.plot(volumes, energies, marker='o', linestyle='-', color='b', label='Si')

plt.title('Energy vs. Volume for Si')
plt.xlabel('Volume (Bohr³ or Å³)')
plt.ylabel('Total Energy (Ry or eV)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('energy_vs_volume_fe.png', dpi=300)
plt.show()
