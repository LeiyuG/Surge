import os
import yaml

RULE_DIR = "rules"
OUTPUT_DIR = "clash"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    payload = []
    comment = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#") and not comment:
            comment = line  # 只保留第一行注释
        elif "," in line:
            parts = line.split(",", 1)
            rule_type = parts[0].strip().upper()
            value = parts[1].strip()
            if rule_type in ['DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD']:
                payload.append(f"{rule_type},{value},Proxy")

    yaml_data = {
        "payload": payload
    }

    with open(output_path, "w", encoding="utf-8") as f:
        if comment:
            f.write(comment + "\n")
        yaml.dump(yaml_data, f, allow_unicode=True, sort_keys=False)

    print(f"✅ {input_path} → {output_path}")

# 批量转换
for file in os.listdir(RULE_DIR):
    if file.endswith(".list"):
        input_file = os.path.join(RULE_DIR, file)
        output_file = os.path.join(OUTPUT_DIR, file.replace(".list", ".yaml"))
        convert_file(input_file, output_file)
