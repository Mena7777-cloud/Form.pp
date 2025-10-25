import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="استمارة تدريب الحميدي",
    page_icon="📄",
    layout="centered"
)

# --- دالة لرسم خط فاصل ذهبي ---
def golden_line():
    """هذه الدالة ترسم خطًا أفقيًا ذهبيًا باستخدام HTML و CSS"""
    st.markdown("<hr style='border: none; height: 2px; background: linear-gradient(to left, #b8860b, #f0e68c); margin: 20px 0;'/>", unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.title("📄 استمارة تدريب في شركة الحميدي")
golden_line() # خط ذهبي بعد العنوان الرئيسي

# --- بناء الاستمارة ---
with st.form(key="training_form", clear_on_submit=True):
    
    # --- كل الحقول مدمجة معًا ---
    full_name = st.text_input("الاسم الكامل", placeholder="اكتب اسمك الثلاثي هنا")
    golden_line() # خط ذهبي

    email = st.text_input("البريد الإلكتروني", placeholder="example@email.com")
    golden_line() # خط ذهبي

    phone = st.text_input("رقم الهاتف", placeholder="01xxxxxxxxx")
    golden_line() # خط ذهبي

    national_id = st.text_input("الرقم القومي (14 رقم)", max_chars=14)
    golden_line() # خط ذهبي

    education = st.text_input("الجامعة / المؤهل الدراسي")
    golden_line() # خط ذهبي

    major = st.text_input("التخصص")
    golden_line() # خط ذهبي

    grad_year = st.number_input("سنة التخرج (المتوقعة)", min_value=2010, max_value=2030, step=1)
    golden_line() # خط ذهبي
    
    personal_photo = st.file_uploader("ارفع صورتك الشخصية هنا", type=['png', 'jpg', 'jpeg'])
    golden_line() # خط ذهبي
    
    id_photo = st.file_uploader("ارفع صورة البطاقة الشخصية (وجه أمامي)", type=['png', 'jpg', 'jpeg', 'pdf'])
    golden_line() # خط ذهبي
    
    why_training = st.text_area("لماذا ترغب في الحصول على هذا التدريب؟")
    golden_line() # خط ذهبي

    skills = st.text_area("ما هي أبرز المهارات التي تتقنها؟")
    golden_line() # خط ذهبي

    training_goal = st.text_area("ما هو هدفك الرئيسي من هذا التدريب؟")
    
    # مسافة فارغة قبل الزر ليكون شكله أفضل
    st.write("") 
    
    # زر الإرسال
    submitted = st.form_submit_button("إرسال الطلب الآن")

# --- ماذا يحدث بعد الضغط على الزر ---
if submitted:
    if not full_name or not email or not national_id:
        st.warning("يرجى ملء الحقول الأساسية: الاسم، البريد الإلكتروني، والرقم القومي.")
    else:
        st.success(f"شكرًا لك، {full_name}! تم استلام طلبك بنجاح.")
        st.balloons()
        
        # (لا يزال هذا الجزء لا يحفظ البيانات، سنعود إليه بعد الموافقة على التصميم)
