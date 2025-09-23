import json, pandas as pd

with open("questionnaire_schema.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def extract(lang="en"):
    rows = []
    for item in data:
        q = next((t["value"] for t in item.get("text", []) if t.get("lang")==lang), None)
        answers = []
        for ans in item.get("answers", []):
            a = next((t["value"] for t in ans.get("text", []) if t.get("lang")==lang), None)
            if a: answers.append(a)
        if q:
            rows.append({"position": item.get("position"), "question": q, "answers": answers})
    return pd.DataFrame(rows).sort_values("position").reset_index(drop=True)

# English-only
df_en = extract("en")
# Russian-only
df_ru = extract("ru")
# Bilingual side-by-side
df_bi = df_en[["position","question","answers"]].merge(
    df_ru.rename(columns={"question":"question_ru","answers":"answers_ru"}),
    on="position", how="left"
)

# Save if you want CSVs
df_en.to_csv("questionnaire_en_wide.csv", index=False)
df_ru.to_csv("questionnaire_ru_wide.csv", index=False)
df_bi.to_csv("questionnaire_bilingual_wide.csv", index=False)