import tkinter.ttk as ttk
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from docControll import docOneProgram, docThreeProgram, docTwoProgram
from sheetControll import sheetOneProgram
from mail.gmail import Gmail

#####################################################################################################

def format_cost(event):
    value = event.widget.get("1.0", "end-1c").strip().replace(",", "")
    if value.isdigit():
        formatted_value = f"{int(value):,}"
        event.widget.delete("1.0", "end")
        event.widget.insert("1.0", formatted_value)

root = Tk()
root.title("계획안 제작_어나더컴퍼니")

config_file_path_1 = os.path.join(os.path.expanduser('~'), '.plan_sheet_path.json')
config_file_path_2 = os.path.join(os.path.expanduser('~'), '.plan_sheet_path_2.json')
config_file_path_3 = os.path.join(os.path.expanduser('~'), '.plan_sheet_path_3.json')

try:
    with open(config_file_path_1, 'r') as f:
        pass
except FileNotFoundError:
    with open(config_file_path_1, 'w') as f:
        json.dump({'file_path': "폴더 경로를 입력해주세요"}, f)

try:
    with open(config_file_path_2, 'r') as f:
        pass
except FileNotFoundError:
    with open(config_file_path_2, 'w') as f:
        json.dump({'file_path': "폴더 경로를 입력해주세요"}, f)

try:
    with open(config_file_path_3, 'r') as f:
        pass
except FileNotFoundError:
    with open(config_file_path_3, 'w') as f:
        pass

def show_frame_1(event):
    selection_1 = cmb_grade.get()
    if selection_1 == "1개 학년":
        sub_frame_school_info2.pack(side="top", padx=5, pady=5, fill="both")
        sub_frame_school_info3.pack_forget()
        sub_frame_school_info4.pack_forget()
    elif selection_1 == "2개 학년":
        sub_frame_school_info2.pack(side="top", padx=5, pady=5, fill="both")
        sub_frame_school_info3.pack(side="top", padx=5, pady=5, fill="both")
        sub_frame_school_info4.pack_forget()
    elif selection_1 == "3개 학년":
        sub_frame_school_info2.pack(side="top", padx=5, pady=5, fill="both")
        sub_frame_school_info3.pack(side="top", padx=5, pady=5, fill="both")
        sub_frame_school_info4.pack(side="top", padx=5, pady=5, fill="both")

def show_frame_2(event):
    selection_2 = cmb_class.get()
    if selection_2 == "3차시" or selection_2 == "4차시":
        lbl_program_1_1.pack_forget()
        cmb_program_1_1.pack_forget()
        lbl_program_2_1.pack_forget()
        cmb_program_2_1.pack_forget()
        lbl_program_3_1.pack_forget()
        cmb_program_3_1.pack_forget()
    elif selection_2 == "5차시" or selection_2 == "6차시":
        lbl_program_1_1.pack(side="left", padx=5, pady=5)
        cmb_program_1_1.pack(side="left", padx=5, pady=5)
        lbl_program_2_1.pack(side="left", padx=5, pady=5)
        cmb_program_2_1.pack(side="left", padx=5, pady=5)
        lbl_program_3_1.pack(side="left", padx=5, pady=5)
        cmb_program_3_1.pack(side="left", padx=5, pady=5)

def add_manager(name, email, password, cmb_manager):
    if name == "" or email == "" or password == "":
        messagebox.showwarning("입력 오류", "모든 필수값을 입력해주세요!")
        return

    user_info = {
        "name": name,
        "id": email,
        "app_pass": password
    }

    with open(config_file_path_3, 'r') as f:
        try:
            existing_data = json.load(f)
            if not isinstance(existing_data, list):
                existing_data = [existing_data]
        except json.JSONDecodeError:
            existing_data = []
    
    existing_data.append(user_info)

    with open(config_file_path_3, 'w') as f:
        json.dump(existing_data, f, indent=4)

    update_manager_list(cmb_manager)
    
    messagebox.showinfo("추가 완료", "새로운 매니저가 등록되었습니다!")

    # 확인용으로 파일 내용 출력
    with open(config_file_path_3, 'r') as f:
        loaded_data = json.load(f)
        print(loaded_data)

def delete_manager(name, cmb_manager):
    try:
        with open(config_file_path_3, "r") as f:
            existing_data = json.load(f)

        updated_data = [manager for manager in existing_data if manager["name"] != name]

        with open(config_file_path_3, "w") as f:
            json.dump(updated_data, f, indent=4)
        
        messagebox.showinfo("삭제 성공", "매니저를 삭제했습니다")

        update_manager_list(cmb_manager)

        with open(config_file_path_3, 'r') as f:
            loaded_data = json.load(f)
            print(loaded_data)

    except Exception:
        messagebox.showerror("삭제 실패", "매니저 삭제에 실패했습니다!")

def get_manager_list():
    try:
        with open(config_file_path_3, "r") as f:
            existing_data = json.load(f)

        manager_names = [manager["name"] for manager in existing_data]

        return manager_names
    except:
        messagebox.showerror("오류", "매니저 명단을 불러오는데 실패했습니다!")

def update_manager_list(dropdown):
    manager_names = get_manager_list()
    dropdown['values'] = manager_names

def save_config_1(file_path):
    # 설정을 JSON 파일에 저장
    with open(config_file_path_1, 'w') as f:
        json.dump({'file_path': file_path}, f)

def save_config_2(file_path):
    # 설정을 JSON 파일에 저장
    with open(config_file_path_2, 'w') as f:
        json.dump({'file_path': file_path}, f)

def load_config_1():
    # 설정 파일에서 파일 경로 불러오기
    try:
        with open(config_file_path_1, 'r') as f:
            config = json.load(f)
            return config.get('file_path')
    except FileNotFoundError:
        return None
    
def load_config_2():
    # 설정 파일에서 파일 경로 불러오기
    try:
        with open(config_file_path_2, 'r') as f:
            config = json.load(f)
            return config.get('file_path')
    except FileNotFoundError:
        return None
    
def browse_dest_path_1():
    initial_dir = load_config_1()
    folder_selected = filedialog.askdirectory(initialdir=initial_dir)
    if folder_selected == '': # 사용자가 취소를 누를 때
        return
    txt_dest_path_1.delete(0, END)
    txt_dest_path_1.insert(0, folder_selected)

    save_config_1(folder_selected)

def browse_dest_path_2():
    initial_dir = load_config_2()
    folder_selected = filedialog.askdirectory(initialdir=initial_dir)
    if folder_selected == '': # 사용자가 취소를 누를 때
        return
    txt_dest_path_2.delete(0, END)
    txt_dest_path_2.insert(0, folder_selected)

    save_config_2(folder_selected)

def to_raw(file_path):
    return fr"{file_path}"

def start():
    # 학년/차시 정보
    grade_num = cmb_grade.get() # 학년 수
    class_num = cmb_class.get() # 차시
    directory_path = txt_dest_path_1.get() # 양식 파일 경로
    save_path = txt_dest_path_2.get()

    # 수업 날짜 정보
    year = txt_year.get("1.0", END).strip()
    month = cmb_month.get()
    day = cmb_day.get()

    class_date = year + "년 " + month + "월 " + day + "일"

    # 학교명/반당 금액
    school_name = txt_school_name.get("1.0", END).strip()
    price = txt_cost.get("1.0", END).strip().replace(",", "")
    print("price: " + price)

    # 프로그램 정보
    first_program_1 = cmb_program_1.get()
    first_program_2 = cmb_program_1_1.get()
    first_grade = cmb_grade_1.get()
    first_class = cmb_ban_1.get()

    second_program_1 = cmb_program_2.get()
    second_program_2 = cmb_program_2_1.get()
    second_grade = cmb_grade_2.get()
    second_class = cmb_ban_2.get()

    last_program_1 = cmb_program_3.get()
    last_program_2 = cmb_program_3_1.get()
    last_grade = cmb_grade_3.get()
    last_class = cmb_ban_3.get()

    # 이메일 정보
    email_check = email_var.get()
    email = email_entry.get()
    teacher = teacher_entry.get()
    manager = cmb_manager.get()

    if grade_num == "1개 학년":
        doc = docOneProgram.Doc(first_grade, first_class, class_num, directory_path, save_path, class_date,
                        first_program_1, first_program_2,
                        school_name)
        doc_file_path = doc.makeDoc()

        sheet = sheetOneProgram.Sheet(first_grade, first_class, class_num, directory_path, save_path, class_date,
                        first_program_1, first_program_2,
                        school_name, price)
        
        sheet_file_path = sheet.makeSheet()
        
    elif grade_num == "2개 학년":
        doc = docTwoProgram.Category(class_num, directory_path, class_date,
                         first_program_1, first_program_2, first_grade, first_class,
                         second_program_1, second_program_2, second_grade, second_class,
                         school_name)
        doc_file_path = doc.makeDoc()
    elif grade_num == "3개 학년":
        doc = docThreeProgram.Category(class_num, directory_path, class_date,
                         first_program_1, first_program_2, first_grade, first_class,
                         second_program_1, second_program_2, second_grade, second_class,
                         last_program_1, last_program_2, last_grade, last_class,
                         school_name)
        doc_file_path = doc.makeDoc()

    file_list = []
    file_list.append(doc_file_path)
    file_list.append(sheet_file_path)

    if email_check:
        gmail = Gmail(filenames=file_list, grade_num=grade_num, school_name=school_name,
                      email=email, teacher=teacher, class_date=class_date, class_num=class_num,
                      first_program_1=first_program_1, first_grade=first_grade, first_class=first_class,
                      second_program_1=second_program_1, second_grade=second_grade, second_class=second_class,
                      last_program_1=last_program_1, last_grade=last_grade, last_class=last_class)
        gmail.send_gmail()

########################################################################################################

# 옵션 프레임
frame_option = Frame(root)
frame_option.pack(padx=5, pady=5, ipady=5, fill="both")

frame_option_sub_1 = LabelFrame(frame_option, text="학년/차시")
frame_option_sub_1.pack(side="top", padx=5, fill="both")

frame_option_sub_2 = LabelFrame(frame_option, text="수업 날짜")
frame_option_sub_2.pack(side="bottom", padx=5, fill="both")

# 1. 제작 옵션
# 학년 레이블
lbl_grade_1 = Label(frame_option_sub_1, text="학년 수", width=8)
lbl_grade_1.pack(side="left", padx=5, pady=5)

# 학년 콤보
opt_grade = ["1개 학년", "2개 학년", "3개 학년"]
cmb_grade = ttk.Combobox(frame_option_sub_1, state="readonly", values=opt_grade, width=10)
cmb_grade.pack(side="left", padx=5, pady=5)
cmb_grade.bind("<<ComboboxSelected>>", show_frame_1)

# 차시 레이블
lbl_class = Label(frame_option_sub_1, text="차시", width=8)
lbl_class.pack(side="left", padx=5, pady=5)

# 차시 콤보
opt_class = ["3차시", "4차시", "5차시", "6차시"]
cmb_class = ttk.Combobox(frame_option_sub_1, state="readonly", values=opt_class, width=10)
cmb_class.pack(side="left", padx=5, pady=5)
cmb_class.bind("<<ComboboxSelected>>", show_frame_2)

# 수업 날짜 - 년도 텍스트박스
txt_year = Text(frame_option_sub_2, width=8, height=1)
txt_year.pack(side="left", padx=10, pady=5)

# 수업 날짜 - 년도 레이블
lbl_year = Label(frame_option_sub_2, text="년", width=4)
lbl_year.pack(side="left", padx=5, pady=5)

# 수업 날짜 - 월 콤보박스
opt_month = [f"{i:02d}" for i in range(1, 13)]
cmb_month = ttk.Combobox(frame_option_sub_2, state="readonly", values=opt_month, width=4)
cmb_month.pack(side="left", padx=5, pady=5)

# 수업 날짜 - 월 레이블
lbl_month = Label(frame_option_sub_2, text="월", width=3)
lbl_month.pack(side="left", pady=5)

# 수업 날짜 - 일 콤보박스
opt_day = [f"{i:02d}" for i in range(1, 32)]
cmb_day = ttk.Combobox(frame_option_sub_2, state="readonly", values=opt_day, width=6)
cmb_day.pack(side="left", padx=5, pady=5)

# 수업 날짜 - 일 레이블
lbl_day = Label(frame_option_sub_2, text="일", width=3)
lbl_day.pack(side="left", pady=5)

# 학교 정보 프레임
frame_school_info = LabelFrame(root, text="학교 정보")
frame_school_info.pack(padx=5, pady=5, fill="both")

# 학교 정보 서브 프레임 1
sub_frame_school_info1 = Frame(frame_school_info)
sub_frame_school_info1.pack(side="top", padx=5, fill="both")

# 1. 학교명 옵션
# 학교명 레이블
lbl_school_name = Label(sub_frame_school_info1, text="학교명", width=5)
lbl_school_name.pack(side="left", padx=5, pady=5)

# 학교명 텍스트박스
txt_school_name = Text(sub_frame_school_info1, width=73, height=1)
txt_school_name.pack(side="left", padx=5, pady=5)

# 반당 금액 레이블
lbl_cost = Label(sub_frame_school_info1, text="반당 금액", width=15)
lbl_cost.pack(side="left", padx=5, pady=5)

# 반당 금액 텍스트박스
txt_cost = Text(sub_frame_school_info1, width=22, height=1)
txt_cost.pack(side="left", padx=5, pady=5)
txt_cost.bind("<KeyRelease>", format_cost)

# 학교 정보 서브 프레임 2
sub_frame_school_info2 = Frame(frame_school_info)

# 학년 레이블
lbl_grade_1 = Label(sub_frame_school_info2, text="학년", width=5)
lbl_grade_1.pack(side="left", padx=5, pady=5)

# 학년 콤보박스
opt_grade = [str(i) + "학년" for i in range(1, 4)]
cmb_grade_1 = ttk.Combobox(sub_frame_school_info2, state="readonly", values=opt_grade, width=8)
cmb_grade_1.pack(side="left", padx=5, pady=5)

# 반 레이블
lbl_ban_1 = Label(sub_frame_school_info2, text="반", width=5)
lbl_ban_1.pack(side="left", padx=5, pady=5)

# 반 콤보박스
opt_ban = [i for i in range(1, 21)]

cmb_ban_1 = ttk.Combobox(sub_frame_school_info2, state="readonly", values=opt_ban, width=8)
cmb_ban_1.pack(side="left", padx=5, pady=5)

# 1~4차시 프로그램 옵션
lbl_program_1 = Label(sub_frame_school_info2, text="1~4차시 프로그램", width=15)
lbl_program_1.pack(side="left", padx=5, pady=5)

# 프로그램 콤보박스
opt_program = ["수상한스튜디오", "어나더랜드", "취업조작단", "비밀상담소", "코드5"]
cmb_program_1 = ttk.Combobox(sub_frame_school_info2, state="readonly", values=opt_program, width=20, height=5)
cmb_program_1.pack(side="left", padx=5, pady=5)

# 5~6차시 프로그램 옵션
lbl_program_1_1 = Label(sub_frame_school_info2, text="5~6차시 프로그램", width=15)

# 프로그램 콤보박스
opt_program_1 = ["코드5", "DISC", "취업조작단1~6차시"]
cmb_program_1_1 = ttk.Combobox(sub_frame_school_info2, state="readonly", values=opt_program_1, width=20, height=1)

# 학교 정보 서브 프레임 3
sub_frame_school_info3 = Frame(frame_school_info)

# 학년 레이블
lbl_grade_2 = Label(sub_frame_school_info3, text="학년", width=5)
lbl_grade_2.pack(side="left", padx=5, pady=5)

# 학년 콤보박스
cmb_grade_2 = ttk.Combobox(sub_frame_school_info3, state="readonly", values=opt_grade, width=8)
cmb_grade_2.pack(side="left", padx=5, pady=5)

# 반 레이블
lbl_ban_2 = Label(sub_frame_school_info3, text="반", width=5)
lbl_ban_2.pack(side="left", padx=5, pady=5)

# 반 콤보박스
cmb_ban_2 = ttk.Combobox(sub_frame_school_info3, state="readonly", values=opt_ban, width=8)
cmb_ban_2.pack(side="left", padx=5, pady=5)

# 1~4차시 프로그램 옵션
lbl_program_2 = Label(sub_frame_school_info3, text="1~4차시 프로그램", width=15)
lbl_program_2.pack(side="left", padx=5, pady=5)

# 프로그램 콤보박스
cmb_program_2 = ttk.Combobox(sub_frame_school_info3, state="readonly", values=opt_program, width=20, height=5)
cmb_program_2.pack(side="left", padx=5, pady=5)

# 5~6차시 프로그램 옵션
lbl_program_2_1 = Label(sub_frame_school_info3, text="5~6차시 프로그램", width=15)

# 프로그램 콤보박스
cmb_program_2_1 = ttk.Combobox(sub_frame_school_info3, state="readonly", values=opt_program_1, width=20, height=1)

# 학교 정보 서브 프레임 4
sub_frame_school_info4 = Frame(frame_school_info)

# 학년 레이블
lbl_grade_3 = Label(sub_frame_school_info4, text="학년", width=5)
lbl_grade_3.pack(side="left", padx=5, pady=5)

# 학년 콤보박스
cmb_grade_3 = ttk.Combobox(sub_frame_school_info4, state="readonly", values=opt_grade, width=8)
cmb_grade_3.pack(side="left", padx=5, pady=5)

# 반 레이블
lbl_ban_3 = Label(sub_frame_school_info4, text="반", width=5)
lbl_ban_3.pack(side="left", padx=5, pady=5)

# 반 콤보박스
cmb_ban_3 = ttk.Combobox(sub_frame_school_info4, state="readonly", values=opt_ban, width=8)
cmb_ban_3.pack(side="left", padx=5, pady=5)

# 1~4차시 프로그램 옵션
lbl_program_3 = Label(sub_frame_school_info4, text="1~4차시 프로그램", width=15)
lbl_program_3.pack(side="left", padx=5, pady=5)

# 프로그램 콤보박스
cmb_program_3 = ttk.Combobox(sub_frame_school_info4, state="readonly", values=opt_program, width=20, height=5)
cmb_program_3.pack(side="left", padx=5, pady=5)

# 5~6차시 프로그램 옵션
lbl_program_3_1 = Label(sub_frame_school_info4, text="5~6차시 프로그램", width=15)

# 프로그램 콤보박스
cmb_program_3_1 = ttk.Combobox(sub_frame_school_info4, state="readonly", values=opt_program_1, width=20, height=1)

# 양식 폴더경로 프레임
path_frame_1 = LabelFrame(root, text="양식 폴더경로")
path_frame_1.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path_1 = Entry(path_frame_1)
txt_dest_path_1.insert(0, load_config_1())
txt_dest_path_1.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path_1 = Button(path_frame_1, text="찾아보기", width=10, command=browse_dest_path_1)
btn_dest_path_1.pack(side="right", padx=5, pady=5)

# 파일 저장할 경로 프레임
path_frame_2 = LabelFrame(root, text="파일 저장할 폴더경로")
path_frame_2.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path_2 = Entry(path_frame_2)
txt_dest_path_2.insert(0, load_config_2())
txt_dest_path_2.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path_2 = Button(path_frame_2, text="찾아보기", width=10, command=browse_dest_path_2)
btn_dest_path_2.pack(side="right", padx=5, pady=5)

# 이메일 전송 여부
frame_email = LabelFrame(root, text="이메일 전송")
frame_email.pack(fill="x", padx=5, pady=5, ipady=5)

email_var = IntVar()
email_var.set(1)

email_checkBox = Checkbutton(frame_email, text="이메일 보내기", variable=email_var)
email_checkBox.pack(side="left", padx=5, pady=5)

email_label = Label(frame_email, text="받을 메일")
email_label.pack(side="left", padx=5, pady=5)

email_entry = Entry(frame_email, width=30)
email_entry.pack(side="left", padx=5, pady=5, ipady=4)

teacher_label = Label(frame_email, text="부장님 성함")
teacher_label.pack(side="left", padx=5, pady=5)

teacher_entry = Entry(frame_email, width=20)
teacher_entry.pack(side="left", padx=5, pady=5, ipady=4)

manager_label = Label(frame_email, text="매니저")
manager_label.pack(side="left", padx=5, pady=5)

manager_names = get_manager_list()

cmb_manager = ttk.Combobox(frame_email, values=manager_names, width=10)
cmb_manager.pack(side="left", padx=5, pady=5, ipady=4)

# 매니저 관리
frame_manager = LabelFrame(root, text="매니저 관리")
frame_manager.pack(fill="x", padx=5, pady=5, ipady=5)

manager_name_label = Label(frame_manager, text="이름")
manager_name_label.pack(side="left", padx=5, pady=5)

manager_name_entry = Entry(frame_manager, width=20)
manager_name_entry.pack(side="left", padx=5, pady=5, ipady=4)

manager_email_label = Label(frame_manager, text="메일 주소")
manager_email_label.pack(side="left", padx=5, pady=5)

manager_email_entry = Entry(frame_manager, width=20)
manager_email_entry.pack(side="left", padx=5, pady=5, ipady=4)

manager_password_label = Label(frame_manager, text="앱 비밀번호")
manager_password_label.pack(side="left", padx=5, pady=5)

manager_password_entry = Entry(frame_manager, width=20)
manager_password_entry.pack(side="left", padx=5, pady=5, ipady=4)

btn_delete = Button(frame_manager, padx=5, pady=5, text="삭제", width=8, command=lambda: delete_manager(manager_name_entry.get(), cmb_manager))
btn_delete.pack(side="right", padx=5, pady=5)

btn_add = Button(frame_manager, padx=5, pady=5, text="추가", width=8, command=lambda: add_manager(manager_name_entry.get(), manager_email_entry.get(), manager_password_entry.get(), cmb_manager))
btn_add.pack(side="right", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()