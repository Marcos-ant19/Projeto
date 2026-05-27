import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("resultados", exist_ok=True)

dados = [
    {"Senha": "9999", "Tentativas": 1679616, "CPU_s": 3.568623, "CUDA_s": 0.006609},
    {"Senha": "67au", "Tentativas": 934341,  "CPU_s": 1.937868, "CUDA_s": 0.004336},
    {"Senha": "zz11", "Tentativas": 1295630, "CPU_s": 2.926859, "CUDA_s": 0.005460},
    {"Senha": "if26", "Tentativas": 1529469, "CPU_s": 3.221772, "CUDA_s": 0.006195},
    {"Senha": "bra6", "Tentativas": 1493606, "CPU_s": 3.155814, "CUDA_s": 0.006803},
]

df = pd.DataFrame(dados)

df["Speedup"] = df["CPU_s"] / df["CUDA_s"]

df.to_csv("resultados/benchmark_resultados.csv", index=False)

plt.figure(figsize=(10, 6))
plt.bar(df["Senha"], df["CPU_s"], label="CPU")
plt.bar(df["Senha"], df["CUDA_s"], label="CUDA")

plt.yscale("log")
plt.xlabel("Senha testada")
plt.ylabel("Tempo de execução (segundos)")
plt.title("Benchmark SHA-256: CPU vs CUDA")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.savefig("resultados/benchmark_cpu_cuda_sha256.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(df["Senha"], df["Speedup"])

plt.xlabel("Senha testada")
plt.ylabel("Speedup CPU/CUDA")
plt.title("Ganho de desempenho da CUDA em relação à CPU")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.savefig("resultados/speedup_cpu_cuda_sha256.png", dpi=300, bbox_inches="tight")
plt.show()

print("Tempo médio CPU:", df["CPU_s"].mean())
print("Tempo médio CUDA:", df["CUDA_s"].mean())
print("Speedup médio:", df["Speedup"].mean())