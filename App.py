import streamlit as st
import random

st.set_page_config(page_title="តេស្តគណិតវិទ្យា", page_icon="📝", layout="centered")

st.title("📝 កម្មវិធីតេស្តគណិតវិទ្យាអនឡាញ")

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
    st.session_state.current_index = 0
    st.session_state.student_answers = [0] * 5
    st.session_state.quiz_submitted = False

if 'student_name' not in st.session_state:
    st.subheader("សូមបំពេញព័ត៌មានមុនពេលចាប់ផ្តើម")
    name = st.text_input("ឈ្មោះសិស្ស៖", placeholder="វាយឈ្មោះរបស់អ្នកនៅទីនេះ...")
    if st.button("ចាប់ផ្តើមធ្វើតេស្ត 🚀", type="primary"):
        if name.strip() != "":
            st.session_state.student_name = name
            st.rerun()
        else:
            st.warning("⚠️ សូមបញ្ចូលឈ្មោះរបស់អ្នកជាមុនសិន!")
else:
    if not st.session_state.quiz_submitted:
        idx = st.session_state.current_index
        q = st.session_state.questions[idx]
        
        st.write(f"🧑‍💻 សិស្សឈ្មោះ៖ **{st.session_state.student_name}**")
        st.markdown(f"## **សំណួរទី {idx + 1} / 5**")
        st.markdown(f"### គណនា៖ **{q['num1']} {q['op']} {q['num2']} = ?**")
        
        ans = st.number_input("វាយចម្លើយរបស់អ្នក៖", key=f"input_{idx}", step=1, value=st.session_state.student_answers[idx])
        st.session_state.student_answers[idx] = ans
        
        col1, col2 = st.columns(2)
        with col1:
            if idx > 0:
                if st.button("⬅️ ថយក្រោយ"):
                    st.session_state.current_index -= 1
                    st.rerun()
        with col2:
            if idx < 4:
                if st.button("បន្ទាប់ទៀត ➡️", type="primary"):
                    st.session_state.current_index += 1
                    st.rerun()
            else:
                if st.button("ផ្ញើវិញ្ញាសា និងមើលពិន្ទុ 🎯", type="primary"):
                    st.session_state.quiz_submitted = True
                    st.rerun()
    else:
        st.balloons()
        st.success(f"🎉 អបអរសាទរ សិស្សឈ្មោះ **{st.session_state.student_name}** បានបញ្ចប់ការធ្វើតេស្ត!")
        
        score = 0
        st.markdown("---")
        st.markdown("### 📊 **លទ្ធផលលម្អិត៖**")
        
        for idx, q in enumerate(st.session_state.questions):
            student_ans = st.session_state.student_answers[idx]
            if student_ans == q['correct']:
                st.write(f"✅ **សំណួរទី {idx+1}៖** ត្រឹមត្រូវ! (អ្នកឆ្លើយ {student_ans} = ចម្លើយពិត {q['correct']})")
                score += 1
            else:
                st.write(f"❌ **...សំណួរទី {idx+1}៖** ខុសហើយ! (អ្នកឆ្លើយ {student_ans} ៖ ចម្លើយពិតគឺ {q['correct']})")
                
        st.markdown("---")
        st.metric(label="ពិន្ទុសរុបទទួលបាន", value=f"{score} / 5")
        
        if st.button("🔄 ធ្វើតេស្តឡើងវិញជាថ្មី"):
            del st.session_state.questions
            del st.session_state.student_name
            st.rerun()
