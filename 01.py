import streamlit as st

# 设置页面标题
st.title('局部模型的SHAP解释和临床应用')

# 显示模型的局部解释
st.subheader('SHAP值解释')

# 显示特征及其影响
st.write('Body weight: 18.00 kg')
st.write('Pediatric Risk of Mortality III (PRISM III): 8.00, Impact: +')
st.write('Minimum mean arterial pressure (MAP_min): 71.60 mmHg')
st.write('Activated partial thromboplastin time (APTT): 23.60 sec')
st.write('Total bilirubin (TBil): 8.30 µmol/L, Impact: -')
st.write('Estimated glomerular filtration rate (eGFR): 60.60 mL/min/1.73m², Impact: -')
st.write('Blood urea nitrogen (BUN): 10.60 mmol/L')
st.write('Urine output (UO): 3.30 mL/kg/h')

# 显示预测结果
st.subheader('预测结果')
st.write('根据特征值，预测AKI的可能性是85.31%')

# 可以添加更多的交互元素，如按钮、选择框等
# 例如，添加一个按钮来触发预测
if st.button('重新预测'):
    # 这里可以添加模型预测的代码
    st.success('预测完成！AKI的可能性是85.31%')