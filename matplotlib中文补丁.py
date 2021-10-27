from os import path, system
import matplotlib
s1 = "        self._fonts['regular'] = default_font"
s2 = "                return g"
t1 = s1+"""
        self._fonts['chinese'] = get_font(findfont("Simsun"))"""
t2 = s2+"""
            elif fontname != 'chinese':
                return self._get_glyph('chinese', font_class, sym, fontsize)
"""
print("本程序可以解决 matplotlib 中英文混排问题")
print("作者：https://github.com/flaribbit")
print("但并不保证一定不会出问题")
targetfile = path.join(matplotlib.__path__[0], "_mathtext.py")
with open(targetfile, "r") as f:
    data = f.read()
if data.find('findfont("Simsun")') < 0:
    userinput = input("输入y确认修改：")
    if userinput != "y":
        exit(0)
    with open(targetfile, "w") as f:
        f.write(data.replace(s1, t1).replace(s2, t2))
else:
    print("检测到已运行过本程序，已跳过操作")
print("""已修复中文问题，推荐配合以下语句使用
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'
如果遇到错误请卸载 matplotlib 重新安装
""")
system("pause")
