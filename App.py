import streamlit as st
import random

st.set_page_config(page_title="តេស្តគណិតវិទ្យា", page_icon="📝", layout="centered")

st.title("📝 កម្មវិធីតេស្តគណិតវិទ្យាអនឡាញ")
st.write("សូមដោះស្រាយលំហាត់ខាងក្រោម រួចចុចប៊ូតុងផ្ទៀងផ្ទាត់ចម្លើយ។")

if 'questions' not in st.session_state:
    questions = []
    for i in range(5):
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        
        if operation == '+':
            correct = num1 + num2
        elif operation == '-':
            if num1 < num2: num1, num2 = num2, num1
            correct = num1 - num2
        else:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            correct = num1 * num2
            
        questions.append({"num1": num1, "num2": num2, "op": operation, "correct": correct})
    st.session_state.questions = questions

student_answers = []
for idx, q in enumerate(st.session_state.questions):
    st.markdown(f"### **សំណួរទី {idx+1}:** គណនា **{q['num1']} {q['op']} {q['num2']} = ?**")
    ans = st.number_input(f"វាយចម្លើយសំណួរទី {idx+1} នៅទីនេះ", key=f"q_{idx}", step=1, value=0)
    student_answers.append(ans)

if st.button("ផ្ញើចម្លើយ និងមើលពិន្ទុ 🎯", type="primary"):
    score = 0
    st.markdown("---")
    st.markdown("### 📊 **លទ្ធផលលម្អិត៖**")
    
    for idx, q in enumerate(st.session_state.questions):
        if student_answers[idx] == q['correct']:
            st.success(f"✅ សំណួរទី {idx+1}៖ ត្រឹមត្រូវ! (ចម្លើយគឺ {q['correct']})")
            score += 1
        else:
            st.error(f"❌ សំណួរទី {idx+1}៖ ខុសហើយ! ចម្លើយត្រឹមត្រូវគឺ {q['correct']}")
            
    st.balloons()
    st.metric(label="ពិន្ទុរបស់អ្នកសរុប", value=f"{score} / 5")
