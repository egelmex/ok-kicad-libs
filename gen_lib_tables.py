import os

print("generating lib tables...")

print("------------------")
sym_lib = []
for x in os.listdir("symbols"):
    if x.endswith(".kicad_sym"):
        sym_lib.append(x)

print(sym_lib)

sym_lib_table = "(sym_lib_table\n"
for sym in sym_lib:
    lib = sym.replace(".kicad_sym", "")
    sym_lib_table += f'  (lib (name "{lib}")(type "KiCad")'
    sym_lib_table += f'(uri "${{OK_LIB_DIR}}/symbols/{sym}")(options "")'
    sym_lib_table += f'(descr ""))\n'
sym_lib_table += ")"
print(sym_lib_table)

f = open("templates\\ok_project\\sym-lib-table", "w")
f.write(sym_lib_table)
f.close()

print("------------------")
fp_lib = []
for x in os.listdir("footprints"): 
    if x.endswith(".pretty"):
        fp_lib.append(x)

print(fp_lib)
fp_lib_table = "(fp_lib_table\n"
for fp in fp_lib:
    lib = fp.replace(".pretty", "")
    fp_lib_table += f'  (lib (name "{lib}")(type "KiCad")'
    fp_lib_table += f'(uri "${{OK_LIB_DIR}}/footprints/{fp}")(options "")'
    fp_lib_table += f'(descr ""))\n'
fp_lib_table += ")"
print(fp_lib_table)

f = open("templates\\ok_project\\fp-lib-table", "w")
f.write(fp_lib_table)
f.close()

print("\ndone.")
