import os

RULE_DIR = "rules"
OUTPUT_DIR = "clash"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            output_lines.append("")  # 空行保留
        elif stripped.startswith("#"):
            output_lines.append(stripped)  # 注释保留
        elif "," in stripped:
            parts = stripped.split(",", 1)
            rule_type = parts[0].strip().upper()
            value = parts[1].strip()
            if rule_type in ['DOMAIN', 'DOMAIN-SUFFIX', 'DOMAIN-KEYWORD']:
                output_lines.append(f"- {rule_type},{value},Proxy")
            else:
                print(f"⚠️ Unsupported rule type in {input_path}: {rule_type}")
        else:
            print(f"⚠️ Skipping invalid line: {stripped}")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for line in output_lines:
            if line.startswith("-") or line.startswith("#"):
                f.write(f"  {line}\n")
            elif line.strip() == "":
                f.write("\n")  # 保留原始空行
            else:
                f.write(f"  # {line}  # preserved unknown line\n")

    print(f"✅ Converted: {input_path} → {output_path}")

# 批量处理
for filename in os.listdir(RULE_DIR):
    if filename.endswith(".list"):
        input_path = os.path.join(RULE_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename.replace(".list", ".yaml"))
        convert_file(input_path, output_path)
