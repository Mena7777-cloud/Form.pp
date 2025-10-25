import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="استمارة تدريب الحميدي",
    page_icon="📄",
    layout="centered"
)

# --- دالة لتطبيق CSS المخصص (خلفية ذهبية وبطاقة بيضاء) ---
def add_custom_css():
    st.markdown(
        """
        <style>
        /* الخلفية الذهبية المتدرجة للصفحة كلها */
        .stApp {
            background: linear-gradient(to bottom, #b8860b, #f0e68c);
            background-attachment: fixed;
            background-size: cover;
        }
        
        /* البطاقة البيضاء التي تحتوي على الاستمارة */
        .main .block-container {
            background-color: white;
            padding: 2rem 2rem 3rem 2rem; /* مساحات داخلية لتبدو أفضل */
            border-radius: 15px; /* حواف دائرية */
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.18); /* ظل خفيف */
            margin-top: -50px; /* لرفع البطاقة للأعلى قليلاً */
        }

        /* لون العنوان الرئيسي */
        h1 {
            color: white;
            text-shadow: 2px 2px 4px #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- تطبيق الـ CSS ---
add_custom_css()

# --- العنوان الرئيسي (سيكون فوق البطاقة البيضاء) ---
st.title("📄 استمارة تدريب في شركة الحميدي")

# --- بناء الاستمارة داخل حاوية بيضاء ---
with st.container():
    with st.form(key="training_form", clear_on_submit=True):
        
        # --- كل الحقول مدمجة معًا ---
        full_name = st.text_input("الاسم الكامل", placeholder="اكتب اسمك الثلاثي هنا")
        email = st.text_input("البريد الإلكتروني", placeholder="example@email.com")
        phone = st.text_input("رقم الهاتف", placeholder="01xxxxxxxxx")
        national_id = st.text_input("الرقم القومي (14 رقم)", max_chars=14)
        education = st.text_input("الجامعة / المؤهل الدراسي")
        major = st.text_input("التخصص")
        grad_year = st.number_input("سنة التخرج (المتوقعة)", min_value=2010, max_value=2030, step=1)
        
        personal_photo = st.file_uploader("ارفع صورتك الشخصية هنا", type=['png', 'jpg', 'jpeg'])
        id_photo = st.file_uploader("ارفع صورة البطاقة الشخصية (وجه أمامي)", type=['png', 'jpg', 'jpeg', 'pdf'])
        
        why_training = st.text_area("لماذا ترغب في الحصول على هذا التدريب؟")
        skills = st.text_area("ما هي أبرز المهارات التي تتقنها؟")
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
        
        # (لا يزال هذا الجزء لا يحفظ البيانات، سنعود إليه لاحقًا)
