import pandas as pd

def load_test_cases_from_excel(file_path, sheet_name):
    # 读取 Excel 文件到 DataFrame，并跳过第一行
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 将 DataFrame 转换为测试用例数据驱动的格式
    test_cases = []
    for index, row in df.iterrows():
        # 创建一个字典来表示每个测试用例
        test_case = {}
        for col_name, value in row.items():
            # 使用列名作为键，对应列的值作为值，构建测试用例字典
            test_case[col_name] = value
        test_cases.append(test_case)

    print(df.head())

    return test_cases

# 使用示例
excel_file_path = '../data/excel/test_case.xlsx'
path_2 = '../../data/excel/test_case.xlsx'
sheet_name = '项目下单'

test_cases = load_test_cases_from_excel(excel_file_path, sheet_name)

# 现在 test_cases 中包含了从 Excel 转换为测试用例数据驱动的数据
# 可以在这里使用这些数据，例如执行测试
