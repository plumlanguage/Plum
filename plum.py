# 导入所需模块
import os
import sys
import re

def print_err(err_lines, string):
    global run_pass
    global ERR_SL
    print(f"ERR[003][line:{err_lines}]=>{string}")
    run_pass = False
    ERR_SL += 1

def get_content_between_fun_and_parenthesis(input_string):
    # 使用正则表达式匹配从'fun'到第一个'('之间的内容
    match = re.search(r'fun(.*?)\(', input_string)

    # 如果找到匹配项，则返回匹配的内容
    if match:
        return match.group(1)  # group(1)表示第一个括号中匹配的内容
    else:
        return "No match found."

def get_content_between_fun_and_parenthesis_in_class(input_string):
    # 使用正则表达式匹配从'fun'到第一个'('之间的内容
    match = re.search(r'stc(.*?)\(', input_string)

    # 如果找到匹配项，则返回匹配的内容
    if match:
        return match.group(1)  # group(1)表示第一个括号中匹配的内容
    else:
        return "No match found."

def is_only_spaces(s):
    return s.isspace()

def run_code (js_file_name):
    os.system(f"node {js_file_name}")

def get_content_between_parentheses(s):
    start = s.find('(')
    end = s.rfind(')')

    if start != -1 and end != -1 and start < end:
        return s[start + 1:end]  # 返回第一个左括号和最后一个右括号之间的内容，不包括括号本身
    else:
        return None  # 如果没有找到括号，返回 None
ERR_SL = 0
run_pass = True
# 解释函数
def code_analysis(code_file_path, js_file_path):
    lines = 0
    global ERR_SL
    global run_pass
    chang = 0
    chang_cun = 0
    run = open(js_file_path, "r" , encoding='utf-8')
    run.close()
    run = open(js_file_path, "a" , encoding='utf-8')
    # 打开文件，使用'with'语句确保文件正确关闭
    with open(code_file_path, 'r', encoding='utf-8') as file:
        # 逐行读取
        for line in file:
            lines += 1
            # 去除行尾的换行符，并检查是否为空白行
            stripped_line = line.strip()
            if stripped_line:  # 如果行不为空
                x = stripped_line.split()  # 以空格分割
                if x[0] == 'using':  # 如果第一项为using
                    # 获取用户主目录的路径
                    home_dir = os.path.expanduser('~')

                    # 获取用户文档目录的路径
                    # 在Windows系统中，这通常是'C:\Users\用户名\Documents'
                    # 在macOS和Linux系统中，这通常是'/home/用户名/Documents'
                    docs_dir = os.path.join(home_dir, 'Documents')

                    print(f"Import Module: {docs_dir}/Plum.Build/{x[1]}.js")

                    run.write(open(f"{docs_dir}/Plum.Build/{x[1]}.js", 'r', encoding="utf-8").read())
                elif x[0] == "fun": # fun name()
                    if len(x) <= 2:
                        print_err(lines,"此处函数声明错误！")
                        continue
                    val = get_content_between_parentheses(stripped_line)
                    val_name = get_content_between_fun_and_parenthesis(stripped_line)
                    while chang >= 1:
                        run.write("\t")
                        chang -= 1
                    chang = chang_cun
                    run.write(f"function {val_name}({val})\n")
                elif x[0] == "class":
                    try:
                        class_name = x[1]
                    except:
                        print_err(lines,"新创建的类好似没有正确命名。")
                    while chang>=1:
                        run.write("\t")
                        chang-=1
                    chang = chang_cun
                    run.write(f"class {class_name}")
                elif x[0] == "import":  # import pkg.pkg
                    # 获取地址
                    try:
                        pkg_path_temp = x[1]
                    except:
                        print_err(lines, "无法正确的获取到您要导入的模块。")
                        continue
                    pkg_path = "pkg/" + pkg_path_temp.replace("::", "/")
                    code_analysis(pkg_path + ".pl", file_name+".js")
                elif x[0] == "object": # object My give my
                    YUAN_obj = x[1]
                    if x[2] == "give":
                        MUBIAO_obj = x[3]
                        while chang >= 1:
                            run.write("\t")
                            chang -= 1
                        chang = chang_cun
                        run.write(f"const {x[3]} = new {x[1]}();\n")
                    else:
                        print_err(lines, "创建对象语法错误!")
                elif x[0] == "give": # give name val
                    while chang>=1:
                        run.write("\t")
                        chang-=1
                    chang = chang_cun
                    try:
                        if len(x) < 3:
                            print_err(lines, "错误的赋值语句!妄想用空格迷惑我！！")
                            continue
                        else:
                            run.write(f"var {x[1]} = {''.join(x[2::])};\n")
                    except:
                        print_err(lines, "错误的赋值语句!")
                elif x[0] == "{":
                    while chang >= 1:
                        run.write("\t")
                        chang -= 1
                    chang = chang_cun
                    run.write("{\n")
                    chang += 1
                    chang_cun += 1
                elif x[0] == "}":
                    chang -= 1
                    chang_cun -= 1
                    while chang >= 1:
                        run.write("\t")
                        chang -= 1
                    chang = chang_cun
                    run.write("}\n")
                elif x[0] == "stc": # stc name ()
                    if len(x) <= 2:
                        print_err(lines, "此处类中方法声明错误！")
                        continue
                    val = get_content_between_parentheses(stripped_line)
                    val_name = get_content_between_fun_and_parenthesis_in_class(stripped_line)
                    while chang >= 1:
                        run.write("\t")
                        chang -= 1
                    chang = chang_cun
                    run.write(f"{val_name}({val})\n")
                else:
                    while chang >= 1:
                        run.write("\t")
                        chang -= 1
                    chang = chang_cun
                    run.write(line.strip() + ";\n")

    run.close()

# 函数对接
if __name__ == '__main__':
    # 获取指令参数并判断是否有参数
    try:
        zl = sys.argv[1::]
    except:
        print("ERR")
    # 判断指令知否为`运行`
    if zl[0] == 'run':
        # 获取文件路径
        file_path = zl[1]
        # 使用os.path.basename获取文件名和扩展名
        file_name_with_extension = os.path.basename(file_path)

        # 使用os.path.splitext分离文件名和扩展名
        file_name, file_extension = os.path.splitext(file_name_with_extension)

        if ".pl" not in file_extension:
            print("Error: File extension is not '.pl'.")
            sys.exit()

        # 生成js文件路径
        run = open(file_name+".js", "w+" , encoding='utf-8')
        run.close()
        # 调用解释函数
        code_analysis(file_path, file_name+".js")
        print("==========================================================\n")
        if run_pass:
            # 调用运行函数
            run_code(file_name+".js")
        else:
            print(f"ERR:{ERR_SL}")
        # 删除js文件
        os.remove(file_name+".js")
    elif zl[0] == "build":
        # 获取文件路径
        file_path = zl[1]
        # 使用os.path.basename获取文件名和扩展名
        file_name_with_extension = os.path.basename(file_path)

        # 使用os.path.splitext分离文件名和扩展名
        file_name, file_extension = os.path.splitext(file_name_with_extension)

        if ".pl" not in file_extension:
            print("Error: File extension is not '.pl'.")
            sys.exit()

        # 生成js文件路径
        run = open(file_name + ".js", "w+", encoding='utf-8')
        run.close()
        # 调用解释函数
        code_analysis(file_path, file_name + ".js")
        print("==========================================================\n")
        if run_pass:
            # 调用运行函数
            run_code(file_name + ".js")
        else:
            print(f"ERR:{ERR_SL}")
            # 删除js文件
            os.remove(file_name + ".js")
    else:
        print("ERR")
