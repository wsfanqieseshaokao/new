import streamlit as st

# 设置页面标题
st.title('SHAP解释和临床预测模型')

# 显示模型的局部解释
st.subheader('局部模型的SHAP解释')

# 显示特征和它们的影响
body_weight = st.number_input("Body weight (kg)", value=18.00, step=0.1)
prism_iii = st.number_input("Pediatric Risk of Mortality III (PRISM III)", value=8.00, step=0.1)
map_min = st.number_input("Minimum mean arterial pressure (MAP_min) (mmHg)", value=71.60, step=0.1)
aptt = st.number_input("Activated partial thromboplastin time (APTT) (sec)", value=23.60, step=0.1)
tbil = st.number_input("Total bilirubin (TBil) (µmol/L)", value=8.30, step=0.1)
egfr = st.number_input("Estimated glomerular filtration rate (eGFR) (mL/min/1.73m²)", value=60.60, step=0.1)
bun = st.number_input("Blood urea nitrogen (BUN) (mmol/L)", value=10.60, step=0.1)
uo = st.number_input("Urine output (UO) (mL/kg/h)", value=3.30, step=0.1)

# 显示预测结果
st.subheader('临床应用')
aki_prediction = 85.31  # 这里可以是模型预测的结果
st.write(f"根据特征值，预测AKI的可能性为{aki_prediction}%")

# 可以添加更多的交互元素，如按钮、选择框等
# 例如，添加一个按钮来触发预测
if st.button('预测'):
    # 这里可以添加模型预测的代码
    st.success(f'预测完成！AKI的可能性为{aki_prediction}%')

# 运行streamlit应用
if __name__ == '__main__':
    st.write("请在浏览器中查看此应用")