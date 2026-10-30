import json

with open("/home/v-kenanli/workspace/ablation/fork/SWE-agent-get-factor/analysis/loc.json") as f:
    d = json.load(f)
file_precision = 0.0
file_recall = 0.0
line_precision = 0.0
line_recall = 0.0
for k, v in d.items():
    file_precision += v["file_precision"]
    file_recall += v["file_recall"]
    line_precision += v["line_precision"]
    line_recall += v["line_recall"]
print("Localization...")
print("file precision", file_precision/len(d))
print("file recall", file_recall/len(d))
print("line precision", line_precision/len(d))
print("line recall", line_recall/len(d))
print()

with open("/home/v-kenanli/workspace/ablation/fork/SWE-agent-get-factor/analysis/con.json") as f:
    d = json.load(f)
file_precision = 0.0
file_recall = 0.0
func_precision = 0.0
func_recall = 0.0
for k, v in d.items():
    file_precision += v["file_precision"]
    file_recall += v["file_recall"]
    func_precision += v["func_precision"]
    func_recall += v["func_recall"]
print("Context...")
print("file precision", file_precision/len(d))
print("file recall", file_recall/len(d))
print("func precision", func_precision/len(d))
print("func recall", func_recall/len(d))
print()


with open("/home/v-kenanli/workspace/ablation/fork/SWE-agent-get-factor/analysis/api.json") as f:
    d = json.load(f)
func_precision = 0.0
func_recall = 0.0
num_valid = 0
def_overlap = 0
def_all = 0
for k, v in d.items():
    func_precision += v["func_precision"]
    func_recall += v["func_recall"]
    if v["overlap_func"] > 0:
        num_valid += 1
    def_overlap += v["overlap_def"]
    def_all += v["all_valid_def"]
print("API...")
print(num_valid, len(d))
print("func precision", func_precision/num_valid)
print("func recall", func_recall/num_valid)
print("def precision", def_overlap/def_all)
print()