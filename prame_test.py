import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("계획안 제작_어나더컴퍼니")

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
    if selection_2 == "3차시":
        lbl_program_1_1.pack_forget()
        cmb_program_1_1.pack_forget()
        lbl_program_2_1.pack_forget()
        cmb_program_2_1.pack_forget()
        lbl_program_3_1.pack_forget()
        cmb_program_3_1.pack_forget()
    elif selection_2 == "4차시":
        lbl_program_1_1.pack_forget()
        cmb_program_1_1.pack_forget()
        lbl_program_2_1.pack_forget()
        cmb_program_2_1.pack_forget()
        lbl_program_3_1.pack_forget()
        cmb_program_3_1.pack_forget()
    elif selection_2 == "6차시":
        lbl_program_1_1.pack(side="left", padx=5, pady=5)
        cmb_program_1_1.pack(side="left", padx=5, pady=5)
        lbl_program_2_1.pack(side="left", padx=5, pady=5)
        cmb_program_2_1.pack(side="left", padx=5, pady=5)
        lbl_program_3_1.pack(side="left", padx=5, pady=5)
        cmb_program_3_1.pack(side="left", padx=5, pady=5)

def grade_commit():
    pass

def load_config_1():
    pass

def browse_dest_path_1():
    pass

def load_config_2():
    pass

def browse_dest_path_2():
    pass

def load_config_3():
    pass

def browse_dest_path_3():
    pass

def start():
    pass


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
opt_class = ["3차시", "4차시", "6차시"]
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
opt_month = [i for i in range(1, 13)]
cmb_month = ttk.Combobox(frame_option_sub_2, state="readonly", values=opt_month, width=4)
cmb_month.pack(side="left", padx=5, pady=5)

# 수업 날짜 - 월 레이블
lbl_month = Label(frame_option_sub_2, text="월", width=3)
lbl_month.pack(side="left", pady=5)

# 수업 날짜 - 일 콤보박스
opt_day = [i for i in range(1, 32)]
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
opt_program_1 = ["코드5", "DISC"]
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
# txt_dest_path_1.insert(0, load_config_1())
txt_dest_path_1.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path_1 = Button(path_frame_1, text="찾아보기", width=10, command=browse_dest_path_1)
btn_dest_path_1.pack(side="right", padx=5, pady=5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()