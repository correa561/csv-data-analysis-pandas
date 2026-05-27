import pandas as pd

df = pd.read_csv("arquivo-estudo.csv")

df["pontuacao"] = pd.to_numeric(df["pontuacao"], errors="coerce")
df = df.dropna(subset=["pontuacao"])
media_geral = df["pontuacao"].mean()
top_100 = df.sort_values("pontuacao", ascending=False).head(100)
media_top_100 = top_100["pontuacao"].mean()
print(f"Média geral: {media_geral:.2f}")
print(f"Média top 100: {media_top_100:.2f}")

print(top_100[["candidato", "pontuacao"]])
